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

class base_object_class:
    def __repr__(self):
        return self.__class__.__name__

class Number_literal(base_object_class):
    pass

class Bool_literal(base_object_class):
    pass

class String_literal(base_object_class):
    pass

class Char_literal(base_object_class):
    pass

class Number(base_object_class):
    def __init__(self):
        pass 

class Bool(base_object_class):
    def __init__(self):
        pass 

class Char(base_object_class):
    def __init__(self):
        pass 

class String(base_object_class):
    def __init__(self):
        pass 

Datatype = Number | Bool | Char | String

class Function_object(base_object_class):
    def __init__(self, val:str, return_type):
        self.name = val
        # self.parameters = []
        # for parameter in parameters:
        #     if(isinstance(parameter, Datatype)): self.parameters.append(parameter)
        #     else: print("Choose an appropriate datatype")

        self.return_type = return_type

class Array(base_object_class):
    def __init__(self, val:Datatype):
        self.datatype = val

class Tuple(base_object_class):
    def __init__(self, val:Datatype):
        self.datatype = val

class Exception(base_object_class):
    def __init__(self, val:str):
        self.literal = val


        
