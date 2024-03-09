# our-own-compiler-squirtle-squad

Go into the directory test and run the code using this method

```
go run testingLexer.go -input=<input_file_name>
```

Before testing the parser, please switch to the branch **Parser**. 

To run the parser:

```
Step1: cd Parser/test
Step2: go run testingParser.go -input="<input-file>"
// The generated input file will be in test folder with the name output_<test_case>.scp
Step3: cd ..
Step4: python pyParser.py test/output_<test_case>.scp
```