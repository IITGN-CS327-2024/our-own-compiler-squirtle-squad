# Scorpion Syntax

This document describes the syntax of our language. Some basic syntax rules are that for line termination you are supposed to put _semicolon(;),_ and _brackets : "{}"_ are to be used for _if_ conditions, _while_ loops, _function_ definitions.

### Reserved Keywords

The reserved keywords for our language are as follows:

```cpp
var char int bool string const arr tuple if elseif else void
func cfunc try throw catch print
```

### Basic Data Types

Following are the data types used in our language and their small description:

```cpp
int : used to define integers variable size 4 bytes, range -2,147,483,648 to 2,147,483,647

bool : used to define boolean values can have only true or false as values, 1 bit data type

char : used to define character data type. Variable size 1 byte range -128 to 127.

string: used to define strings.
```

We chose C style variable declaration where the data type has to be specified because it makes the code more readable and easy to understand. Also the development of our compiler would be easy if the data type is specified explicitly.

### Variable Declaration

This section contains the description as to how to define variables in our language.

```cpp
var - This keyword has to be used to define variable data types. For example to define a variable of type int the use will be:

var int myInteger;

you can also assign value to the variable at the time of variable defination

var int myInteger = 10;

const - This keyword has to be used to define constant datatypes, its values can't be changed in the program. example:

const int myInteger = 10;

the basic structure is as follows :

<var/const> <datatype> <name of datatype> = <value> ;
```

We chose the keyword var for data types whose values can be changed and const whose values cannot be changed because we wanted to be as explicit as possible in our language so the code generated is readable, and also it may be easy to make parser this way.

### Compound Data Types

This section contains the declaration of arrays and tuples, the compound data types.

#### Array declaration

To declare an array _arr_ keyword has to be used at the starting of the declaration.
There are three ways in which you can define an array:

```cpp
1. arr <datatype> <name of variable> = [data1, data2, ...] ;

2. arr <datatype> <name of variable> : <size of array> ;

3. arr <datatype> <name of variable> : <size of array> : <default value of array>;
```

#### Tuple Declaration

To declare a tuple, _tuple_ keyword has to be used at the starting of the declaration.
A tuple can be defined in the following way:

```python
tuple <datatype> <name of tuple> = [data1, data2, ...] ;
```

The user does not need to specify the _var, const keyword_ _before array or tuple_ declaration because we wanted to avoid redundancy, if a user wants a const array they can use tuple, similarly if the user wants a variable array they should use arr. Also as tuples are immutable we allowed only single type of declaration.

### Mutable Variables

Do define mutable variables we defined the _keyword var_ for basic data types, while for non mutable datatypes we defined the _keyword const_. Similarly mutable compound variables are arrays and non mutable data types are tuples.

## Conditionals

Conditional statements in this language, like in any other, allow us to _control the flow of execution_ based on different conditions, providing a structured decision-making mechanism.

We plan to use _<i>if</i>_ keyword for the first conditional statement, <i>elseif</i> (note- without space) for subsequent cases, and <i>else</i> keyword for last declaration. <br>
_Curly braces_ <b>{}</b> is to be used after every declaration of a conditional statement and to mark the start and close of that block of code. <br>
**Note**: We will put brackets even if only one statement is under a condition (unlike in C) to make it uniform and simpler. <br>

#### Syntax:

```go
if (<condition>) {
    <statements> ; (semicolon after each statement)
}
elseif (<condition>) {
    <statements> ; (semicolon after each statement)
}
else {
    <statements> ; (semicolon after each statement)
}
```

#### Example:

```go
var int myInteger = 12;
if (myInteger < 5) {
    print: "number less than 5" ;
}
elseif (myInteger < 10) {
    print: "number less than 10" ;
}
elseif (myInteger <= 15) {
    print: "number less than 16" ;
}
else {
    print: "number greater than 15" ;
}
```

## Loops:

The language supports both _while_ and _for_ loops, enabling execution of repetitive code. <br>

#### Syntax:

```c++
while (<conditions>) {
    <statements> ; (semicolon after each statement)
}

for ( <initialisation>; <condition> ; <iteration update>){
    <statements>
}
```

We've maintained a syntax closely resembling that of C/C++ because we found their syntax to be effective and saw no need for significant alterations. <br>
Inside the for loop we have chosen _semicolon_ so that we may use multiple iteration variables by separating them with commas. <br>
Like conditionals, we here too follow a _strict opening and closing_ **{}** rule for both types of loop.<br>

#### Example

```go
var int i = 5;
while (i){
    print: i ;
    i--;
}

for (i=0 ; i<5; i++){
    print: i;
}
```

## Functions:

All function definitions start with the keyword _func_. After that we mention the function name which is then followed by _parenthesis_ **()** that has pairs of parameter datatype and parameter name, all comma separated. After the closing bracket we have a colon and the datatype of the return value. Note that all datatypes must be specified. And here too opening and closing **{}** are mandatory.

#### Syntax:

```go
func <func_name>( <datatype> <parameter_name>, …) : <return datatype> {
	// lines of code
	return <value>
}
```

We devised such a syntax because the _func_ keyword would make it easier to identify a block of code to be a function definition and the necessary datatype specification would account for better documentation (like in Python) and **type safety** (like in C)

#### Example:

```go
func first( int num1, int num2) : int {
	var int num_sum = num1 + num2;
	return num_sum;
}
```

<br>

## Closure:

In this, a function is defined inside a function such that the local variables of the parent function act as global variables for the child function. <br>
We account for this '_child function_' with the keyword _cfunc_. Other than this, it follows the same rules and syntax of a function in our langauge.<br>

#### Syntax:

```go
func <func_name>( <datatype> <parameter_name>, …) : <return datatype> {
	// lines of code
	cfunc <func_name>( <datatype> <parameter_name>, …) : <return datatype> {
		// lines of code
        return <datatype>
    }
	return <datatype>
}
```

#### Example:

```go
func outer(int num, int a, int b) : int {

    cfunc inner(int x) : int{
        return num + x;
    }

    return inner(a) * inner(b);
}
```

## Operators

- _Basic arithmetic_ operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulo)
- _Basic logical_ operators:`or`, `and`, `not`
- _Bitwise_ operators: `|`(or) , `&`(and), `~`(not)
- _Bit Shift_ operators: `<<` (left shift), `>>` (right shift)
- The following table summaries the _usage of the above operators_

| `<int>`          | `<string>`            | `<bool>`            |
| ---------------- | --------------------- | ------------------- |
| `<int> + <int>`  | `<string> + <string>` | `<bool> and <bool>` |
| `<int> - <int>`  | `<string> + <char>`   | `<bool> or <bool>`  |
| `<int> * <int>`  | `<char> + <string>`   | `not <bool>`        |
| `<int> / <int>`  |                       |                     |
| `<int>`\|`<int>` |                       |                     |
| `<int> & <int>`  |                       |                     |
| `~ <int>`        |                       |                     |
| `<int> >> <int>` |                       |                     |
| `<int> << <int>` |                       |                     |

- Also, the **return type** of the operation will remain the same as the 2 operands. Hence, to add 2 chars, the user will need to initialise an empty string and the 2 add chars to them. Example: `<int> / <int>;` -> _returns int_
- Multiple operators with integers are supported, and they will be evaluated using the _BODMAS_ rule.
- _Multiple string concatenation_ using multiple **+** operators is also supported.
- Available _Shorthand notations_: `<int> += <int>;`, `<string> += <string>;`. In similar fashion, `-=, /=, *=, %=, >>=, <<=` are also supported for `int`.
  Example: `a += b;` is same as

<br>

#### Unary operators:

`<int>++;` _Increments_ the value of the integer by 1. The return type is void. <br>
`<int>--;` _Decrements_ the value of the integer by 1. The return type is void. <br>
`not bool;` _Logical negation_ operator <br>
`~ <int>;` _Bitwise negation_ operator <br>

#### Comparison operators:

**Return type** is _boolean_.

`a < b` Checks if `a` _Lesser than_ `b`. <br>
`a > b` Checks if `a` _Greater than_ `b`.<br>
`a <= b` Checks if `a` _Lesser than or equal to_ `b`.<br>
`a >= b` Checks if `a` _Greater than or equal to_ `b`.<br>
`a > b` Checks if `a` _Lesser than_ `b`.<br>
`a == b` Checks if `a` _equal to_ `b`.<br>
`a != b` Checks if `a` _not equal_ `b`.<br>

### Order of Precedence:

**Note:** Currently this is just _a proposal_ regarding resolving precedence in operators, it will be easier for us to decide once we get a hold of the implementation specifics.

The table below outlines the _precedence and associativity_ of inspired from C++ operators. The operators are arranged from top to bottom, with higher precedence listed first.

Associativity, establishes the sequence in which operators with the same level of precedence are processed within an expression.

| Precedence | Operator                | Operation Description                       | Associativity |
| ---------- | ----------------------- | ------------------------------------------- | ------------- |
| 1          | `a++` `a--`<br>`a[]`    | Postfix Increment or decrement<br>Indexing  | Left to right |
| 2          | `~ a`<br>`not b`        | Bitwise NOT<br>Logical NOT                  | Left to right |
| 3          | `a*b`   `a/b`   `a%b`   | Multiplication, division, and remainder     | Left to right |
| 4          | `a+b`   `a-b`           | Addition and subtraction                    | Left to right |
| 5          | `<<`   `>>`             | Bitwise left shift and right shift          | Left to right |
| 6          | `<`   `<=`   `>`   `>=` | For relational operators                    | Left to right |
| 7          | `==`   `!=`             | For equality operators = and ≠ respectively | Left to right |
| 8          | `a&b`                   | Bitwise AND                                 | Left to right |
| 9          | \|                      | Bitwise OR                                  | Left to right |
| 10         | and                     | Logical AND                                 | Left to right |
| 11         | or                      | Logical OR                                  | Left to right |

## Print Statements and output

- Basic syntax: `print: <expression>`
- _Python-like string formatting_ features are also present.
  Example: `print: “ The two variable are {} and {}”.format(var1, var2);`
- A newline character is not inserted at the end of any print expression by default, and the user needs mention any of these escape characters.
- _Escape characters_ supported: `\n`, `\t`, `\0`(null character), `\\` (using backslash), `\’`(single quote) , `\”` (double quote)
- Support for _direct variable printing_ is also available.
  Example : `var int a = 5; print : a`. This prints 5.
- _Multiple operands_ in the print statement are **not supported**. The flexibility to print multiple variables at once is provided to the user using formatting operations.

## Indexing and changing values

- _Arrays, strings, tuples_ follow **zero-based** indexing.
- As of now the support is _not extended multi-dimensional arrays and nested tuples_, although we plan to incorporate this feature once we have some clarity with the implementation.
- We use the _square brackets notation_ like most languages.This notation is used _access_ and _alter values_ in arrays and tuples. Changing values in _tuples_ is not permitted, since it is an **immutable object**.
- Example:

```go
arr int sample_arr = [1, 2, 3];
print: arr[0];
print: '\n';
sample_arr[0] = 5;
print: arr[0];
```

    The above code return the following ouput:
    0
    5

## Slicing of arrays and tuples

- `len(<tuple/array>)` returns the **length** of the _array or tuple_.
- Use `slice(<array/tuple>, start_index, end_index)`:  The range is _\[start, end\]_ - (**both inclusive**)
- To _slice till the end of the array/tuple_ use: `slice(<array/tuple>, start_index, tail(<array/tuple>))`
- To _slice from start of the array/tuple_ use: `slice(<array/tuple>, head(<array/tuple>), end_index)`
- To _insert an element at the start_ of an _array/tuple,_ use: `cons(<array/tuple>, <element>`. The element needs to be of the same type as the elements in the array/tuple. This is an **inplace operation.**
- This is can also be explicitly defined for arrays and tuples. To include support for both of these in a single function we plan to use function overloading, variadic functions or object oriented programming constructs like methods and attributes.
- For _strings_ use `substr(<string>, start, end)`: The range is*\[start, end\]* - (**both inclusive**)
- Also, the return types for all of these functions is the same as the first operand, except the `cons` function, which is an **inplace function**.
- The `head` and `tail` functions _just return integers_ corresponding to the start and end of their arrays/tuples respectively. We plan to add iterators once we a better idea of the implementation details.

## Exception Handling

- Use `try-catch` blocks to handle exceptions
- The `catch` block can't be used alone, the `try` block _must precede_ it.
- We can handle _specific exceptions_, using `catch(specific_exception spec_ex)`
- To handle _general exceptions_, using `catch(specific_exception spec_ex)`

```java
try {
  // block of code to try which could produce errors
}
catch(specific_exception spec_ex) {
  // Block of code to handle specific_exception error
}
catch(Exception e) {
  // Block of code to handle other types of error
  // not handled by above catch blocks.
}

```

- Additionally, `throw` keyword can to throw _custom errors_.

```java
throw Exception_type("error message");
```

**Note:** As per our current understanding, throwing errors would require us to _implement different classes of error types_, and we are still exploring different ways to provide the same functionality, as we can’t yet foresee the _implementation of classes_. Based on future developments, we might make some changes to the above functioning.

## Comments

- Structure for _single line comments_, `shrey_joshi: <- comment line -> ;` and use `;` to terminate, we also plan to support `\n` character to terminate comments, but as of now the underlying implementation is unclear for the case (say if `\n` character is part of the comments).
- Structure for _multi-line comments_, which is similar to _multi-line comments in c++_ `/*` followed by multi line comments or paragraph and end with `*/` to terminate the comment section.

```
/*
Example for multi-line comments
Hello, World!
*/

shrey_joshi: This is an example for single line comment ;
```
