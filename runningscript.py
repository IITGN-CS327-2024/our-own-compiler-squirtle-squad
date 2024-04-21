import subprocess
import sys

lexer_dir = "Parser/test"
output_dir = "outputs"
wat_dir1 = "question/wat"
wat_dir2 = "question/wasm"

# Get the testcase name from command line arguments
testcase = sys.argv[1]

program_name = testcase.split('.')
program_name = program_name[0]

# Execute the first command: go run $(LEXER_DIR)/testingParser.go --input=$(testcase))
command1 = f"go run {lexer_dir}/testingParser.go --input=testcases/{testcase} --output={output_dir}"

# Run the first command
result_lexer = subprocess.run(command1, shell=True)

# Check if the first command terminated abnormally
if result_lexer.returncode != 0:
    print("Error detected in lexing stage.")
    sys.exit()

# Execute the second command: python Parser/pyParser.py Parser/test/output_test_case_1.scp
command2 = f"python3 Parser/pyParser.py {output_dir}/output_{testcase}"
result_parser = subprocess.run(command2, shell=True)

# Check if the first command terminated abnormally
if result_parser.returncode != 0:
    print("Error detected in later stage.")
    sys.exit()

# Execute the third command: wat2wasm question/wat/{program_name}.wat -o {program_name}.wasm
command3 = f"wat2wasm {wat_dir1}/{program_name}.wat -o {wat_dir2}/{program_name}.wasm"

# Run the third command
result_wat2wasm = subprocess.run(command3, shell=True)

# Check if the third command terminated abnormally
if result_wat2wasm.returncode != 0:
    print("Error detected in converting .wat to .wasm.")
    sys.exit()