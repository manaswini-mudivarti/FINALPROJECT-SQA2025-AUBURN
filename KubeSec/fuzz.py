import random
import string
import scanner  # Importing the scanner module which contains validation methods
import parser   # Importing the parser module which contains YAML and Helm check methods

# Function to generate a random alphanumeric string of given length (default = 10)
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Main fuzzing function that tests various methods with randomized and edge-case inputs
def fuzz_methods():
    # Loop to run 100 iterations of fuzzing for each method
    for _ in range(100):

        # --- Fuzz isValidUserName ---
        try:
            # Randomly select a fuzzed input value from a variety of data types
            input_val = random.choice([random_string(), 123, None, True, "", [], {}])
            # Call the function with fuzzed input and store result
            result = scanner.isValidUserName(input_val)
            # Print the input and corresponding output
            print(f"isValidUserName({input_val}) -> {result}")
        except Exception as e:
            # Catch and print any crash details
            print(f"Crash in isValidUserName({input_val}): {e}")

        # --- Fuzz isValidPasswordName ---
        try:
            input_val = random.choice([random_string(), 456, None, False, "pass", [], {}])
            result = scanner.isValidPasswordName(input_val)
            print(f"isValidPasswordName({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in isValidPasswordName({input_val}): {e}")

        # --- Fuzz checkIfValidSecret ---
        try:
            input_val = random.choice(["token123", "admin", "", " ", 1234, None, random_string()])
            result = scanner.checkIfValidSecret(input_val)
            print(f"checkIfValidSecret({input_val}) -> {result}")
        except Exception as e:
            print(f"Crash in checkIfValidSecret({input_val}): {e}")

        # --- Fuzz checkIfWeirdYAML ---
        try:
            # Test paths that resemble YAML config files or invalid inputs
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

        # --- Fuzz checkIfValidHelm ---
        try:
            # Test strings that may or may not be Helm-related paths
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

# Run the fuzzing process if this script is executed as the main program
if __name__ == "__main__":
    fuzz_methods()
