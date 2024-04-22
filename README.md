# our-own-compiler-squirtle-squad

To compile any code, create a .scp file in _testcases_. The required testcases for the assignment are already there in the folder. Follow the steps to compile them:
The possible testcases are: 'arthimetic', 'caesar', 'sort'

```
Step1: python runningscript.py {name_of_testcase}.scp
[Eg: python runningscript.py sort.scp]
Step2: To check the tree check the tree.png generated in the same folder.
Step3: cd question
Step4: ./test.sh
```

**Note:** The compiler implementation requires both *Go lang* and *Python*. Also, use `pip install -r requirements.txt` to setup. 

**Note**: We have 8 test cases for which we have already generated the trees for the same in the **trees** folder. Testcases 0,7 will throw error because function not defined, TC 5,6 will throw error because closures and exception handling is not supported in current version.
