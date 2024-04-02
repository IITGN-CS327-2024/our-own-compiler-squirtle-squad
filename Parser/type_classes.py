'''
Number
Bool
String
Char
Function object
Array
Tuple
Exception object
'''
class Number_literal:
    pass

class Bool_literal:
    pass

class String_literal:
    pass

class Char_literal:
    pass

class Number:
    pass

class Bool:
    pass 

class Char:
    pass 

class String:
    pass

Datatype = Number | Bool | Char | String

class Function_object:
    def __init__(self, val:str, parameters:list):
        self.name = val
        self.parameters = []
        for parameter in parameters:
            if(isinstance(parameter, Datatype)): self.parameters.append(parameter)
            else: print("Choose an appropriate datatype")

class Array:
    def __init__(self, val:Datatype):
        self.datatype = val

class Tuple:
    def __init__(self, val:Datatype):
        self.datatype = val

class Exception:
    def __init__(self, val:str):
        self.literal = val


        
