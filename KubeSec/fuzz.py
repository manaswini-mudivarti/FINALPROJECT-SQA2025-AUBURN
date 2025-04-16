import random
import string
import scanner
import parser

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fuzz_methods():
    for _ in range(100):
        # Fuzz isValidUserName
        try:
            input_val = random.choice([random_string(), 123, None, True, "", [], {}])
            result = scanner.isValidUserName(input_val)
            print(f"isValidUserName({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in isValidUserName({input_val}): {e}")

        # Fuzz isValidPasswordName
        try:
            input_val = random.choice([random_string(), 456, None, False, "pass", [], {}])
            result = scanner.isValidPasswordName(input_val)
            print(f"isValidPasswordName({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in isValidPasswordName({input_val}): {e}")

        # Fuzz checkIfValidSecret
        try:
            input_val = random.choice(["token123", "admin", "", " ", 1234, None, random_string()])
            result = scanner.checkIfValidSecret(input_val)
            print(f"checkIfValidSecret({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in checkIfValidSecret({input_val}): {e}")

        # Fuzz checkIfWeirdYAML
        try:
            input_val = random.choice([
                ".github/workflows/config.yml",
                "/my/app/config.yaml",
                "not_a_path",
                12345,
                None
            ])
            result = parser.checkIfWeirdYAML(input_val)
            print(f"checkIfWeirdYAML({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in checkIfWeirdYAML({input_val}): {e}")

        # Fuzz checkIfValidHelm
        try:
            input_val = random.choice([
                "charts/helm/values.yaml",
                "services.yaml",
                "/chart/configs/deploy/values.yaml",
                "script.py",
                "",
                None
            ])
            result = parser.checkIfValidHelm(input_val)
            print(f"checkIfValidHelm({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in checkIfValidHelm({input_val}): {e}")

if __name__ == "__main__":
    fuzz_methods()
