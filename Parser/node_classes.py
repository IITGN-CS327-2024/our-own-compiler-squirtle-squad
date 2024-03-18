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
        
class Start(ASTNode):
  
  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

   
class Program(ASTNode):
   
  def __init__(self, values):
    # print(values)
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

    
class Statement(ASTNode):
   
  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class Statements(ASTNode):
   
  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)
   
class VariableDeclarationStatement(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)
    

class Values(ASTNode):
  
  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

  
class FunctionCall(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

 
class Condition(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

  
class OrCondition(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)
  
    
class AndCondition(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

  
class NotCondition(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

  
class Expression(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

    
class BitwiseExpr(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

    
class EqExpr(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

    
class ShiftExpr(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

     
class AddExpr(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

    
class MultExpr(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

     
class PowerExpr(ASTNode):

  def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

  
class ParametersCall(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)
   

class VariableChangeStatement(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

   
class FunctionDeclaration(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class ConditionalStatement(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class LoopControl(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class PrintStatement(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class ExceptionHandling(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class ExpressionStatement(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)


class ReturnStatement(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class ConsOp(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class ThrowStatement(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class ArrayDeclaration(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class TupleDeclaration(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class TypeDeclaration(ASTNode):
   
   def __init__(self, values):
    for i, value in enumerate(values):
        setattr(self, f'values{i}', value)

class IfStatement(ASTNode):
    
    def __init__(self, values):
      for i, value in enumerate(values):
          setattr(self, f'values{i}', value)

class ElseIfStatements(ASTNode):
   
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class ElseStatement(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class LoopStatement(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class TypeDeclaration(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class ReturnStatement(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class ExceptionHandling(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class ComplexVal(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class CompCondition(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class UnaryOperation(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)