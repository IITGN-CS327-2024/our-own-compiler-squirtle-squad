import subprocess
import sys

lexer_dir = "Parser/test"
output_dir = "outputs"
# Get the testcase name from command line arguments
testcase = sys.argv[1]

# Execute the first command: go run $(LEXER_DIR)/testingParser.go --input=$(testcase))
command1 = f"go run {lexer_dir}/testingParser.go --input=testcases/{testcase} --output={output_dir}"

# Run the first command
result_lexer = subprocess.run(command1, shell=True)

# Check if the first command terminated abnormally
if result_lexer.returncode != 0:
    print("Error detected in lexing stage.")
    sys.exit()

# Execute the second command: python Parser/pyParser.py Parser/test/output_test_case_1.scp
command2 = f"python Parser/pyParser.py {output_dir}/output_{testcase}"
result_parser = subprocess.run(command2, shell=True)

# Check if the first command terminated abnormally
if result_parser.returncode != 0:
    print("Error detected in parsing stage.")
    sys.exit()

# Check if the first command terminated abnormally
if result_parser.returncode != 0:
    print("Error detected in parsing stage.")
    sys.exit()