"""Abstract syntax representation of a sequence of sums."""

# import logging
# logging.basicConfig()
# log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)
class ASTNodeMeta(type):
    def __new__(cls, name, bases, dct):
        if name != 'ASTNode':
            def repr_func(self):
                return name
            dct['__repr__'] = repr_func
        return super().__new__(cls, name, bases, dct)

class ASTNode(metaclass=ASTNodeMeta):
    """Abstract b"""
    pass

# Example of using the metaclass for defining classes
# class Start(ASTNode):
#     def __init__(self, values):
#         for i, value in enumerate(values):
#             setattr(self, f'values{i}', value)

# Add more classes following the same pattern

# class ASTNode:
#     """Abstract base class for abstract sequence of sequence of sums"""
#     def __init__(self):
#         """This is an abstract class and should not be instantiated"""
#         this_class = self.__class__.__name__
#         if this_class == "ASTNode":
#             raise NotImplementedError("ASTNode is an abstract class and should not be instantiated")
#         else:
#             raise NotImplementedError(f"{this_class} is missing a constructor method")

class sabka_baap(ASTNode):
   
   def __init__(self, values):

    self.children = []
    for i, value in enumerate(values):
        self.children.append(value)
      
class Start(sabka_baap):
   
   def __init__(self, values):
      super().__init__(values)
  
class Program(sabka_baap):
   
   def __init__(self,values):
      super().__init__(values)

class Statement(sabka_baap):
   
   def __init__(self,values):
      super().__init__(values)

class Statements(sabka_baap):
   
   def __init__(self,values):
      super().__init__(values)
   
class VariableDeclarationStatement(sabka_baap):

   def __init__(self,values):
      super().__init__(values)
    

class Values(sabka_baap):
  
   def __init__(self,values):
      super().__init__(values)
  
class FunctionCall(sabka_baap):

   def __init__(self,values):
      super().__init__(values)
 
class Condition(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

  
class OrCondition(sabka_baap):

   def __init__(self,values):
      super().__init__(values)
  
    
class AndCondition(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

  
class NotCondition(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

  
class Expression(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

    
class BitwiseExpr(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

class EqExpr(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

    
class ShiftExpr(sabka_baap):

   def __init__(self,values):
      super().__init__(values) 

     
class AddExpr(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

    
class MultExpr(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

     
class PowerExpr(sabka_baap):

   def __init__(self,values):
      super().__init__(values)

  
class ParametersCall(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)
   

class VariableChangeStatement(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

   
class FunctionDeclaration(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class ConditionalStatement(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class LoopControl(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class PrintStatement(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class ExceptionHandling(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class ExpressionStatement(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)


class ReturnStatement(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class ConsOp(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class ThrowStatement(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class ArrayDeclaration(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class TupleDeclaration(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class TypeDeclaration(sabka_baap):
   
    def __init__(self,values):
      super().__init__(values)

class IfStatement(sabka_baap):
    
    def __init__(self,values):
      super().__init__(values)

class ElseStatement(sabka_baap):
    
    def __init__(self,values):
      super().__init__(values)

class LoopStatement(sabka_baap):
    def __init__(self,values):
      super().__init__(values)

class TypeDeclaration(sabka_baap):
    def __init__(self,values):
      super().__init__(values)

class ReturnStatement(sabka_baap):
    def __init__(self,values):
      super().__init__(values)

class ExceptionHandling(sabka_baap):
    def __init__(self,values):
      super().__init__(values)

class ComplexVal(sabka_baap):
    def __init__(self,values):
      super().__init__(values)

class CompCondition(sabka_baap):
    def __init__(self,values):
      super().__init__(values)

class UnaryOperation(sabka_baap):
    def __init__(self,values):
      super().__init__(values)