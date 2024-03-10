import subprocess
import sys

lexer_dir = "Parser/test"
output_dir = "outputs"
# Get the testcase name from command line arguments
testcase = sys.argv[1]

# Execute the first command: go run $(LEXER_DIR)/testingParser.go --input=$(testcase))
command1 = f"go run {lexer_dir}/testingParser.go --input=testcases/{testcase} --output={output_dir}"
subprocess.run(command1, shell=True)


# Execute the second command: python Parser/pyParser.py Parser/test/output_test_case_1.scp
command2 = f"python Parser/pyParser.py {output_dir}/output_{testcase}"
subprocess.run(command2, shell=True)