import random
import os

# Định nghĩa các lệnh và định dạng của chúng
commands = [
    "reset",
    "write",
    "not",
    "cnot",
    "hadamard",
    "chadamard",
    "phase",
    "swap",
    "rotatex",
    "rotatey",
    "measure"
]


def generate_command(command, num_bit):
    if command == "reset":
        num_bit = random.randint(1, 5)  # Số bit ngẫu nhiên từ 1 đến 5
        return f"reset {num_bit}", num_bit

    if command == "write":
        value = random.randint(0, 2 ** num_bit - 1)  # Giá trị nhị phân của số bit hiện tại
        return f"write {value}"

    if command in ["not", "hadamard", "rotatex", "rotatey", "phase"]:
        target_bit = random.randint(0, num_bit - 1)
        if command in ["rotatex", "rotatey", "phase"]:
            theta_degrees = random.choice([0, 45, 90, 135, 180, 225, 270, 315, 360])
            return f"{command} {theta_degrees} {target_bit}"
        return f"{command} {target_bit}"

    if command in ["cnot", "chadamard"]:
        target_bit = random.randint(0, num_bit - 1)
        condition_bit = random.randint(0, num_bit - 1)
        while condition_bit == target_bit:
            condition_bit = random.randint(0, num_bit - 1)
        return f"{command} {target_bit} {condition_bit}"

    if command == "swap":
        bit1 = random.randint(0, num_bit - 1)
        bit2 = random.randint(0, num_bit - 1)
        while bit1 == bit2:
            bit2 = random.randint(0, num_bit - 1)
        return f"swap {bit1} {bit2}"

    if command == "measure":
        return "measure"


def generate_test_case():
    num_bit = random.randint(1, 5)
    test_case = []
    reset_command, num_bit = generate_command("reset", num_bit)
    test_case.append(reset_command)
    write_command = generate_command("write", num_bit)
    test_case.append(write_command)
    num_commands = random.randint(1, 10)  # Số lệnh ngẫu nhiên từ 1 đến 10
    for _ in range(num_commands):
        command = random.choice(commands[:-1])  # Loại bỏ lệnh "measure" để thêm vào cuối
        generated_command = generate_command(command, num_bit)
        if isinstance(generated_command, tuple):
            generated_command = generated_command[0]
        test_case.append(generated_command)
    test_case.append("measure")
    return "\n".join(test_case)


def generate_and_save_test_cases(n, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(1, n + 1):
        test_case = generate_test_case()
        with open(os.path.join(directory, f"testcase{i}.txt"), "w") as file:
            file.write(test_case)


# Số lượng test case cần tạo
n = 10
directory = "testcase"
generate_and_save_test_cases(n, directory)
