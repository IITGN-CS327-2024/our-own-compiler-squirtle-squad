# our-own-compiler-squirtle-squad

Go into the directory test and run the code using this method

```
go run testingLexer.go -input=<input_file_name>
```

Before testing the parser, please switch to the branch **Parser**. 

To run the parser with semantic analysis:

```
Step1: python runningscript.py test_case_7.scp
Step2: To check the tree check the tree.png generated in the same folder.
```
**Note**: We have 8 test cases for which we have already generated the trees for the same in the **trees** folder. Testcases 0,7 will throw error because function not defined, TC 5,6 will throw error because closures and exception handling is not supported in current version.