FINALPROJECT-SQA2025-AUBURN

Team Members:
SRI LAKSHMI MANASWINI MUDIVARTI
SHIVA TEJA PANJALA
ABHIPSHA SAHOO
YESHASWEE SAI GANESH VOLETY
---

# Activities Completed

1. Git Hook - Bandit Security Analysis

Implemented a 'pre-commit' Git hook located at '.git/hooks/pre-commit'.
This hook automatically runs 'bandit' and generates a report named 'bandit_report.csv' for static analysis.
If critical issues are detected, the commit is blocked.
Bandit Output Format: CSV
Example Hook Command:
  '''bash
  bandit -r . -f csv -o bandit_report.csv

2. Fuzz Testing -  fuzz.py

Developed a fuzzer script fuzz.py to automatically test 5 python methods using random or malformed inputs.
Targeted functions:
- isValidUserName() - from scanner.py
- isValidPasswordName() - from scanner.py
- checkIfValidSecret() - from scanner.py
- checkIfWeirdYAML() - from parser.py
- checkIfValidHelm() - from parser.py

Errors are caught and printed, such as TypeError, NoneType crashes, and edge case mismatches.

GitHub Actions Integration

- Created GitHb Actions workflow .github/workflows/fuzz.yml to run fuzz.py on every push and pull request.
- Dependencies like ruamel.yml, sarif-om, and jschema-to-python are installed automatically.

3. Forensics Logging- 5 Instrumented Functions

Added detailed forensic logging to track input, output, and execution behavior in:
- isValidUserName() - from scanner.py
- isValidPasswordName() - from scanner.py
- checkIfValidSecret() - from scanner.py
- checkIfWeirdYAML() - from parser.py
- checkIfValidHelm() - from parser.py

Logging Details:
- Logs are written to a file named forensics.log
- Logger implementation is located in forensic_logger.py
- Example log entry:
  2025-04-15 17:45:00 - INFO - checkIfValidHelm() called with: script.py
  2025-04-15 17:45:00 - INFO - checkIfValidHelm result: False

Lessons Learned:

- Understood the integration of Git hooks to enforce code quality before commits
- Gained practical experience with fuzz testing and random input generation for real functions
- Learned how to add forensic-level logging for critical software methods
- Practiced automated CI workflows using GitHub Actions for continuous testing
