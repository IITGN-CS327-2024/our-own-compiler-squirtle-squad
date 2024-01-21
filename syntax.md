# Language Syntax

This document describes the syntax of our language. Some basic syntax rules are that for line termination you are supposed to put semicolon(;), and brackets : "{}" are to be used for if condtions, while loops, function definitions.

### Reserved Keywords  

The reserved keywords for our langauge are as follows:

```cpp
var char int bool string const arr tuple if elseif else void 
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

This section contains the  description as to how to define variables in our language.  
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
```cpp
arr - To declare an array arr keyword has to be used at the starting of the declaration.
There are three ways in which you can define an array:
1. arr <datatype> <name of variable> = [data1, data2, ...] ;
2. arr <datatype> <name of variable> : <size of array> ;
3. arr <datatype> <name of variable> : <size of array> : <default value of array>;
```
#### Tuple Declaration
```cpp
tuple - To declare a tuple, tuple keyword has to be used at the starting of the declaration. A tuple can be defined in the following way:

tuple <datatype> <name of tuple> = [data1, data2, ...] ;
```

The user does not need to specify the var, const keyword before array or tuple declaration because we wanted to avoid redundancy, if a user wants a const array they can use tuple, similarly if the user wants a variable array they should use arr. Also as tuples are immutable we allowed only single type of declaration.

### Mutable Variables

Do define mutable variables we defined the keyword var for basic data types, while for non mutable datatypes we defined the keyword const. Similarly mutable compound variables are arrays and non mutable data types are tuples.