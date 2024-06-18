import numpy as np
import os
import re


class QuantumSimulator:
    def __init__(self) -> None:
        self.state = None
        self.num_qubits = 0

    def reset(self, num_qubits):  # tạo thanh ghi trống với numqubit ban đầu
        self.num_qubits = num_qubits
        self.state = np.zeros((2 ** num_qubits,), dtype=complex)
        self.state[0] = 1

    def apply_gate(self, gate, target_qubits):  # áp dụng các cổng
        full_gate = np.eye(1)
        for qubit in range(self.num_qubits):
            if qubit in target_qubits:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, np.eye(2))
        self.state = np.dot(full_gate, self.state)

    def write(self, value, target_qubits):  # tạo trạng thái
        for i in range(self.num_qubits):
            if (target_qubits == []) or (i in target_qubits):
                if value & (1 << i):
                    self.apply_gate(np.array([[0, 1], [1, 0]]), [i])

    def not_gate(self, target_qubits):  # cổng not
        self.apply_gate(np.array([[0, 1], [1, 0]]), target_qubits)

    def cnot_gate(self, target_qubits, condition_qubits):  # cổng cnot
        for tq in target_qubits:
            for cq in condition_qubits:
                self._apply_cnot(tq, cq)

    def _apply_cnot(self, target, control):
        new_state = self.state.copy()
        for i in range(len(self.state)):
            if (i >> target) & 1:
                if (i >> control) & 1:
                    new_state[i ^ (1 << target)] = self.state[i]
                    new_state[i] = self.state[i ^ (1 << target)]
        self.state = new_state

    def hadamard(self, target_qubits):  # cổng hadamard
        h_gate = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
        self.apply_gate(h_gate, target_qubits)

    def chadamard(self, target_qubits, condition_qubits):  # hadamard có điều kiện
        for tq in target_qubits:
            for cq in condition_qubits:
                self._apply_cnot(tq, cq)
                self.hadamard([tq])
                self._apply_cnot(tq, cq)

    def phase(self, theta_degrees, target_qubits):  # cổng xoay trục Z
        theta_radians = np.deg2rad(theta_degrees)
        phase_gate = np.array([[1, 0], [0, np.exp(1j * theta_radians)]])
        self.apply_gate(phase_gate, target_qubits)

    def swap(self, qubit1, qubit2, condition_qubits):  # swap
        for cq in condition_qubits:
            self._apply_swap(qubit1, qubit2, cq)

    def _apply_swap(self, qubit1, qubit2, control):
        new_state = self.state.copy()
        for i in range(len(self.state)):
            if (i >> control) & 1:
                if ((i >> qubit1) & 1) != ((i >> qubit2) & 1):
                    new_i = i ^ (1 << qubit1) ^ (1 << qubit2)
                    new_state[new_i] = self.state[i]
        self.state = new_state

    def rotatex(self, theta_degrees, target_qubits):  # xoay trục X
        theta_radians = np.deg2rad(theta_degrees)
        rx_gate = np.array([[np.cos(theta_radians / 2), -1j * np.sin(theta_radians / 2)],
                            [-1j * np.sin(theta_radians / 2), np.cos(theta_radians / 2)]])
        self.apply_gate(rx_gate, target_qubits)

    def rotatey(self, theta_degrees, target_qubits):  # xoay trục Y
        theta_radians = np.deg2rad(theta_degrees)
        ry_gate = np.array([[np.cos(theta_radians / 2), -np.sin(theta_radians / 2)],
                            [np.sin(theta_radians / 2), np.cos(theta_radians / 2)]])
        self.apply_gate(ry_gate, target_qubits)

    def measure(self):
        probabilities = np.abs(self.state) ** 2
        measurement_results = {bin(i)[2:].zfill(self.num_qubits)[::-1]: round(probabilities[i], 3) for i in
                               range(len(probabilities))}
        return dict(sorted(measurement_results.items()))


def read_test_cases(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith('#')]


def run_test_cases(file_path):
    commands = read_test_cases(file_path)
    qs = QuantumSimulator()
    output = []
    output.append(f"Running test cases from {file_path}")
    for command in commands:
        parts = command.split()
        operation = parts[0]
        args = list(map(int, parts[1:])) if len(parts) > 1 else []
        if operation == 'reset':
            qs.reset(*args)
        elif operation == 'write':
            qs.write(*args, [])
        elif operation == 'not':
            qs.not_gate(args)
        elif operation == 'cnot':
            qs.cnot_gate([args[0]], [args[1]])
        elif operation == 'hadamard':
            qs.hadamard(args)
        elif operation == 'chadamard':
            qs.chadamard([args[0]], [args[1]])
        elif operation == 'phase':
            qs.phase(args[0], [args[1]])
        elif operation == 'swap':
            qs.swap(args[0], args[1], [])
        elif operation == 'rotatex':
            qs.rotatex(args[0], [args[1]])
        elif operation == 'rotatey':
            qs.rotatey(args[0], [args[1]])
        elif operation == 'measure':
            results = qs.measure()
            for state, prob in results.items():
                output.append(f"State: {state}, Probability: {prob}")
    return output


def run_all_test_cases_in_directory(testcase_directory, output_directory):
    testcase_files = [f for f in os.listdir(testcase_directory) if re.match(r'^testcase\d+\.txt$', f)]
    os.makedirs(output_directory, exist_ok=True)
    for file in sorted(testcase_files):
        result = run_test_cases(os.path.join(testcase_directory, file))
        output_number = re.search(r'\d+', file).group()
        output_filename = f"output{output_number}.txt"
        output_filepath = os.path.join(output_directory, output_filename)
        with open(output_filepath, 'w') as result_file:
            for line in result:
                result_file.write(line + '\n')


##kiểm tra kết quả (chưa làm được)
# Example usage
testcase_directory = 'testcase'
output_directory = 'result'
run_all_test_cases_in_directory(testcase_directory, output_directory)
