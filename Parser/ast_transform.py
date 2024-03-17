import node_classes
import lark  

def flatten(lst):
    flat_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flat_list.extend(flatten(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

class OurTransformer(lark.Transformer):

    """We write a transformer for each node in the parse tree
    (concrete syntax) by writing a method with the same name.
    Non-terminal symbols are passed a list of their children
    after transformation, which proceeds from leaves to root
    recursively. Terminal symbols (like NUMBER) are instead
    passed a lark.Token structure.
    """

    def Integer(self, n):
        return int(n)
    
    def Boolean(self, b):
        if(b): return 1 
        else: return 0
       
    def start(self, children):
        children = flatten(children)
        return node_classes.Start(children)
    
    def program(self, children):
        children = flatten(children)
        return node_classes.Program(children) 
    
    def statement(self, children):
        children = flatten(children)
        return node_classes.Statement(children)
    
    def statements(self, children):
        children = flatten(children)
        return node_classes.Statements(children)
    
    def variable_declaration_statement(self, children):
        children = flatten(children)
        return node_classes.VariableDeclarationStatement(children)
    
    def variable_declaration(self, children):
        children = flatten(children)
        return children
    
    def datatype(self, children):
        children = flatten(children)
        return children
    
    def condition(self, children):
        children = flatten(children)
        return children
    
    def condition1(self, children):

        children = flatten(children)
        if(len(children) == 1):
            return flatten(children)
        
        return node_classes.Condition1(children)
    
    def condition2(self, children):

        children = flatten(children)
        if(len(children) == 1):
            return flatten(children)
        
        return node_classes.Condition2(children)
    
    def condition3(self, children):

        children = flatten(children)
        if(len(children) == 1):
            return children
        
        return node_classes.Condition3(children)
    
    def un_operators_pre(self, children):
        children = flatten(children)
        return children 
    
    def un_operators_post(self, children):
        children = flatten(children)
        return children 
    
    def comp_operators(self , children):
        children = flatten(children)
        return children 
    
    def cond_terminal(self, children):
        children = flatten(children)
        return children
    
    def expression(self, children):
        children = flatten(children)
        if(len(children) == 1): return children 
        return node_classes.Expression(children)
    
    def bitwise_expr(self, children):

        children = flatten(children)
        if(len(children) == 1): return children
        return node_classes.BitwiseExpr(children)

    def eq_expr(self, children):

        children = flatten(children)
        if(len(children) == 1): return children
        return node_classes.EqExpr(children)

    def shift_expr(self, children):

        children = flatten(children)
        if(len(children) == 1): return children
        return node_classes.ShiftExpr(children)

    def add_expr(self, children):

        children = flatten(children)
        if(len(children) == 1): return children
        return node_classes.AddExpr(children)

    def mult_expr(self, children):

        children = flatten(children)
        if(len(children) == 1): return children
        return node_classes.MultExpr(children)

    def power_expr(self, children):

        children = flatten(children)
        if(len(children) == 1): return children
        return node_classes.PowerExpr(children)
    
    def terminal_expr(self, children):
        children = flatten(children)
        return children
    
    def function_call(self, children):
        children = flatten(children)
        return node_classes.FunctionCall(children)
    
    def parameters_call(self, children):
        children = flatten(children)
        if(len(children) == 0): return None
        return node_classes.ParametersCall(children)
    
    def params_call(self, children):
        children = flatten(children)
        return children

    def values(self, children):
        children = flatten(children)
        return children

    def number_nt(self, children):
        children = flatten(children)
        return children 
    
    def variable_change_statement(self, children):
        children = flatten(children)
        return node_classes.VariableChangeStatement(children)

    def variable_change(self, children):
        children = flatten(children)
        return children

    def opeq(self, children):
        children = flatten(children)
        return children
    
    def loop_control(self, children):
        children = flatten(children)
        return children
    
    def cons_op(self, children):
        children = flatten(children)
        return node_classes.ConsOp(children)
    
    def array_declaration(self, children):
        children = flatten(children)
        return node_classes.ArrayDeclaration(children)
    
    def end_arr(self, children):
        children = flatten(children)
        return children
    
    def tuple_declaration(self, children):
        children = flatten(children)
        return node_classes.TupleDeclaration(children)
    
    def string_nt(self, children):
        children = flatten(children)
        return children
    
    def string_items(self, children):
        children = flatten(children)
        return children
    
    def bool_literals(self, children):
        children = flatten(children)
        return children
    
    def arr_datatype(self, children):
        children = flatten(children)
        return children

    def tup_datatype(self, children):
        children = flatten(children)
        return children
    
    def expression_statment(self, children):
        children = flatten(children)
        return node_classes.ExpressionStatement(children)
    
    def exception_type(self, children):
        children = flatten(children)
        return children
    
    def throw_statement(self, children):
        children = flatten(children)
        return node_classes.ThrowStatement(children)
    
    def print_statement(self, children):
        children = flatten(children)
        return node_classes.PrintStatement(children)
    
    def function_declaration(self, children):
        children = flatten(children)
        return node_classes.FunctionDeclaration(children)
    
    def parameter_def(self, children):
        children = flatten(children)
        return children
    
    def conditional_statement(self, children):
        children = flatten(children)
        return node_classes.ConditionalStatement(children)
    
    def elseif_statements(self, children):
        children = flatten(children)
        return node_classes.ElseIfStatements(children)
    
    def else_statement(self, children):
        children = flatten(children)
        return node_classes.ElseStatement(children)
    
    def loop_statement(self, children):
        children = flatten(children)
        return node_classes.LoopStatement(children)
    
    def var_init(self, children):
        children = flatten(children)
        return children
    
    def iterating(self, children):
        children = flatten(children)
        if(len(children) == 0): return None 
        else: return children






















    

    


        


    

 
 