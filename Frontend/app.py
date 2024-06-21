# from flask import Flask, request, jsonify, render_template
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# class QuantumSimulator:
#     def __init__(self) -> None:
#         self.state = None
#         self.num_qubits = 0

#     def reset(self, num_qubits):  # tạo thanh ghi trống với numqubit ban đầu
#         self.num_qubits = num_qubits
#         self.state = np.zeros((2 ** num_qubits,), dtype=complex)
#         self.state[0] = 1

#     def apply_gate(self, gate, target_qubits):  # áp dụng các cổng
#         full_gate = np.eye(1)
#         for qubit in range(self.num_qubits):
#             if qubit in target_qubits:
#                 full_gate = np.kron(full_gate, gate)
#             else:
#                 full_gate = np.kron(full_gate, np.eye(2))
#         self.state = np.dot(full_gate, self.state)

#     def write(self, value, target_qubits):  # tạo trạng thái
#         for i in range(self.num_qubits):
#             if (target_qubits == []) or (i in target_qubits):
#                 if value & (1 << i):
#                     self.apply_gate(np.array([[0, 1], [1, 0]]), [i])

#     def not_gate(self, target_qubits):  # cổng not
#         self.apply_gate(np.array([[0, 1], [1, 0]]), target_qubits)

#     def cnot_gate(self, target_qubits, condition_qubits):  # cổng cnot
#         for tq in target_qubits:
#             for cq in condition_qubits:
#                 self._apply_cnot(tq, cq)

#     def _apply_cnot(self, target, control):
#         new_state = self.state.copy()
#         for i in range(len(self.state)):
#             if (i >> target) & 1:
#                 if (i >> control) & 1:
#                     new_state[i ^ (1 << target)] = self.state[i]
#                     new_state[i] = self.state[i ^ (1 << target)]
#         self.state = new_state

#     def hadamard(self, target_qubits):  # cổng hadamard
#         h_gate = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
#         self.apply_gate(h_gate, target_qubits)

#     def chadamard(self, target_qubits, condition_qubits):  # hadamard có điều kiện
#         for tq in target_qubits:
#             for cq in condition_qubits:
#                 self._apply_cnot(tq, cq)
#                 self.hadamard([tq])
#                 self._apply_cnot(tq, cq)

#     def phase(self, theta_degrees, target_qubits):  # cổng xoay trục Z
#         theta_radians = np.deg2rad(theta_degrees)
#         phase_gate = np.array([[1, 0], [0, np.exp(1j * theta_radians)]])
#         self.apply_gate(phase_gate, target_qubits)

#     def swap(self, qubit1, qubit2, condition_qubits):  # swap
#         for cq in condition_qubits:
#             self._apply_swap(qubit1, qubit2, cq)

#     def _apply_swap(self, qubit1, qubit2, control):
#         new_state = self.state.copy()
#         for i in range(len(self.state)):
#             if (i >> control) & 1:
#                 if ((i >> qubit1) & 1) != ((i >> qubit2) & 1):
#                     new_i = i ^ (1 << qubit1) ^ (1 << qubit2)
#                     new_state[new_i] = self.state[i]
#         self.state = new_state

#     def rotatex(self, theta_degrees, target_qubits):  # xoay trục X
#         theta_radians = np.deg2rad(theta_degrees)
#         rx_gate = np.array([[np.cos(theta_radians / 2), -1j * np.sin(theta_radians / 2)],
#                             [-1j * np.sin(theta_radians / 2), np.cos(theta_radians / 2)]])
#         self.apply_gate(rx_gate, target_qubits)

#     def rotatey(self, theta_degrees, target_qubits):  # xoay trục Y
#         theta_radians = np.deg2rad(theta_degrees)
#         ry_gate = np.array([[np.cos(theta_radians / 2), -np.sin(theta_radians / 2)],
#                             [np.sin(theta_radians / 2), np.cos(theta_radians / 2)]])
#         self.apply_gate(ry_gate, target_qubits)

#     def measure(self):
#         probabilities = np.abs(self.state) ** 2
#         measurement_results = {bin(i)[2:].zfill(self.num_qubits)[::-1]: round(probabilities[i], 3) for i in
#                                range(len(probabilities))}
#         return dict(sorted(measurement_results.items()))

# qs = QuantumSimulator()

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = []
#     input_test_cases = ''
#     if request.method == 'POST':
#         input_test_cases = request.form['test_cases']
#         test_cases = input_test_cases.split('\n')
#         qs = QuantumSimulator()
#         for line in test_cases:
#             parts = line.strip().split()
#             if not parts:
#                 continue
#             command = parts[0]
#             try:
#                 if command == 'reset':
#                     qs.reset(int(parts[1]))
#                 elif command == 'write':
#                     qs.write(int(parts[1]), [])
#                 elif command == 'not':
#                     qs.not_gate([int(parts[1])])
#                 elif command == 'cnot':
#                     qs.cnot_gate([int(parts[1])], [int(parts[2])])
#                 elif command == 'hadamard':
#                     qs.hadamard([int(parts[1])])
#                 elif command == 'chadamard':
#                     qs.chadamard([int(parts[1])], [int(parts[2])])
#                 elif command == 'phase':
#                     qs.phase(float(parts[1]), [int(parts[2])])
#                 elif command == 'swap':
#                     qs.swap(int(parts[1]), int(parts[2]), [])
#                 elif command == 'rotatex':
#                     qs.rotatex(float(parts[1]), [int(parts[2])])
#                 elif command == 'rotatey':
#                     qs.rotatey(float(parts[1]), [int(parts[2])])
#                 elif command == 'measure':
#                     result = qs.measure()
#                 else:
#                     result.append(f"Unknown command: {command}")
#             except Exception as e:
#                 result.append(f"Error executing {command}: {str(e)}")
#         result = [f"State: {state}, Probability: {prob}" for state, prob in result.items()]

#     return render_template('home.html', result=result, input_test_cases=input_test_cases)


# @app.route('/run_code', methods=['POST'])
# def run_code():
#     data = request.get_json()
#     code = data['code']

#     qs = QuantumSimulator()
#     output = []
#     test_cases = code.split('\n')
#     for line in test_cases:
#         parts = line.strip().split()
#         if not parts:
#             continue
#         command = parts[0]
#         try:
#             if command == 'reset':
#                 qs.reset(int(parts[1]))
#             elif command == 'write':
#                 qs.write(int(parts[1]), [])
#             elif command == 'not':
#                 qs.not_gate([int(parts[1])])
#             elif command == 'cnot':
#                 qs.cnot_gate([int(parts[1])], [int(parts[2])])
#             elif command == 'hadamard':
#                 qs.hadamard([int(parts[1])])
#             elif command == 'chadamard':
#                 qs.chadamard([int(parts[1])], [int(parts[2])])
#             elif command == 'phase':
#                 qs.phase(float(parts[1]), [int(parts[2])])
#             elif command == 'swap':
#                 qs.swap(int(parts[1]), int(parts[2]), [])
#             elif command == 'rotatex':
#                 qs.rotatex(float(parts[1]), [int(parts[2])])
#             elif command == 'rotatey':
#                 qs.rotatey(float(parts[1]), [int(parts[2])])
#             elif command == 'measure':
#                 result = qs.measure()
#                 output = [f"State: {state}, Probability: {prob}" for state, prob in result.items()]
#             else:
#                 output.append(f"Unknown command: {command}")
#         except Exception as e:
#             output.append(f"Error executing {command}: {str(e)}")

#     return jsonify({'output': output})

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, render_template
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class QuantumSimulator:
    def __init__(self) -> None:
        self.state = None
        self.num_qubits = 0

    def reset(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros((2 ** num_qubits,), dtype=complex)
        self.state[0] = 1

    def apply_gate(self, gate, target_qubits):
        full_gate = np.eye(1)
        for qubit in range(self.num_qubits):
            if qubit in target_qubits:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, np.eye(2))
        self.state = np.dot(full_gate, self.state)

    def write(self, value, target_qubits):
        for i in range(self.num_qubits):
            if (target_qubits == []) or (i in target_qubits):
                if value & (1 << i):
                    self.apply_gate(np.array([[0, 1], [1, 0]]), [i])

    def not_gate(self, target_qubits):
        self.apply_gate(np.array([[0, 1], [1, 0]]), target_qubits)

    def cnot_gate(self, target_qubits, condition_qubits):
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

    def hadamard(self, target_qubits):
        h_gate = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
        self.apply_gate(h_gate, target_qubits)

    def chadamard(self, target_qubits, condition_qubits):
        for tq in target_qubits:
            for cq in condition_qubits:
                self._apply_cnot(tq, cq)
                self.hadamard([tq])
                self._apply_cnot(tq, cq)

    def phase(self, theta_degrees, target_qubits):
        theta_radians = np.deg2rad(theta_degrees)
        phase_gate = np.array([[1, 0], [0, np.exp(1j * theta_radians)]])
        self.apply_gate(phase_gate, target_qubits)

    def swap(self, qubit1, qubit2, condition_qubits):
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

    def rotatex(self, theta_degrees, target_qubits):
        theta_radians = np.deg2rad(theta_degrees)
        rx_gate = np.array([[np.cos(theta_radians / 2), -1j * np.sin(theta_radians / 2)],
                            [-1j * np.sin(theta_radians / 2), np.cos(theta_radians / 2)]])
        self.apply_gate(rx_gate, target_qubits)

    def rotatey(self, theta_degrees, target_qubits):
        theta_radians = np.deg2rad(theta_degrees)
        ry_gate = np.array([[np.cos(theta_radians / 2), -np.sin(theta_radians / 2)],
                            [np.sin(theta_radians / 2), np.cos(theta_radians / 2)]])
        self.apply_gate(ry_gate, target_qubits)

    def measure(self):
        probabilities = np.abs(self.state) ** 2
        measurement_results = {bin(i)[2:].zfill(self.num_qubits)[::-1]: round(probabilities[i], 3) for i in
                               range(len(probabilities))}
        sorted_results = dict(sorted(measurement_results.items()))
        formatted_results = [f"State: {state}, Probability: {prob}" for state, prob in sorted_results.items()]
        return formatted_results

qs = QuantumSimulator()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    input_test_cases = ''
    if request.method == 'POST':
        input_test_cases = request.form['test_cases']
        test_cases = input_test_cases.split('\n')
        qs = QuantumSimulator()
        for line in test_cases:
            parts = line.strip().split()
            if not parts:
                continue
            command = parts[0]
            try:
                if command == 'reset':
                    qs.reset(int(parts[1]))
                elif command == 'write':
                    qs.write(int(parts[1]), [])
                elif command == 'not':
                    qs.not_gate([int(parts[1])])
                elif command == 'cnot':
                    qs.cnot_gate([int(parts[1])], [int(parts[2])])
                elif command == 'hadamard':
                    qs.hadamard([int(parts[1])])
                elif command == 'chadamard':
                    qs.chadamard([int(parts[1])], [int(parts[2])])
                elif command == 'phase':
                    qs.phase(float(parts[1]), [int(parts[2])])
                elif command == 'swap':
                    qs.swap(int(parts[1]), int(parts[2]), [])
                elif command == 'rotatex':
                    qs.rotatex(float(parts[1]), [int(parts[2])])
                elif command == 'rotatey':
                    qs.rotatey(float(parts[1]), [int(parts[2])])
                elif command == 'measure':
                    result = qs.measure()
                else:
                    result.append(f"Unknown command: {command}")
            except Exception as e:
                result.append(f"Error executing {command}: {str(e)}")

    return render_template('home.html', result='\n'.join(result), input_test_cases=input_test_cases)

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data['code']

    qs = QuantumSimulator()
    output = []
    test_cases = code.split('\n')
    for line in test_cases:
        parts = line.strip().split()
        if not parts:
            continue
        command = parts[0]
        try:
            if command == 'reset':
                qs.reset(int(parts[1]))
            elif command == 'write':
                qs.write(int(parts[1]), [])
            elif command == 'not':
                qs.not_gate([int(parts[1])])
            elif command == 'cnot':
                qs.cnot_gate([int(parts[1])], [int(parts[2])])
            elif command == 'hadamard':
                qs.hadamard([int(parts[1])])
            elif command == 'chadamard':
                qs.chadamard([int(parts[1])], [int(parts[2])])
            elif command == 'phase':
                qs.phase(float(parts[1]), [int(parts[2])])
            elif command == 'swap':
                qs.swap(int(parts[1]), int(parts[2]), [])
            elif command == 'rotatex':
                qs.rotatex(float(parts[1]), [int(parts[2])])
            elif command == 'rotatey':
                qs.rotatey(float(parts[1]), [int(parts[2])])
            elif command == 'measure':
                result = qs.measure()
                output.extend(result)
            else:
                output.append(f"Unknown command: {command}")
        except Exception as e:
            output.append(f"Error executing {command}: {str(e)}")

    return jsonify({'output': '\n'.join(output)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
