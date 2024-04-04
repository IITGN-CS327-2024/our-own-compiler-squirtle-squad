import node_classes
import lark  

def check_existence(small_list, large_list):
    return any(element in large_list for element in small_list)

def flatten(lst):
    flat_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flat_list.extend(flatten(sublist))

        elif(sublist is not None):
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

    # count = 0

    def NUMBER(self, n):
        return node_classes.NumberNode(n)
    
    def BOOLEAN(self, b):
        if(b): return node_classes.BoolNode(True) 
        else: return node_classes.BoolNode(False)

    def CHAR(self, c):
        return node_classes.CharNode(c)
    
    def STRING(self, s):
        return node_classes.StringNode(s)
    
    def IDENTIFIER(self, i):
        return node_classes.VarNode(i)
    
    def TRUE(self, t):
        return node_classes.BoolNode(True)
    
    def FALSE(self, t):
        return node_classes.BoolNode(False)
    
    def CHAR_K(self, c):
        return node_classes.CharNode(c)
    
    def STRING_K(self, c):
        return node_classes.StringNode(c)
    
    def INTEGER(self, i):
        return node_classes.NumberNode(i)
    
    def MAIN(self, m):
        return node_classes.Main(m)
       
    def start(self, children):
        children = flatten(children)
        return node_classes.Start(children)
    
    def program(self, children):
        children = flatten(children)
        return node_classes.Program(children) 
    
    def statement(self, children):
        children = flatten(children)
        return children
    
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
        
        return node_classes.OrCondition(children)
    
    def condition2(self, children):

        children = flatten(children)
        if(len(children) == 1):
            return flatten(children)
        
        return node_classes.AndCondition(children)
    
    def condition3(self, children):

        children = flatten(children)
        if(len(children) == 1):
            return children
        
        # self.count+=1
        # print(self.count)
        # for i in children:
        #     print(i, type(i))

        if children[0] == "not":
            return node_classes.NotCondition(children)
        
        comparators = [">", "<", ">=", "<="]
        if check_existence(comparators, children):
            return node_classes.CompCondition(children)
        
        if children[-1]=="++" or children[-1]=="--" or children[0]=="~" or children[0]=="!":
            return node_classes.UnaryOperation(children)
        
        print("Error in condition3")
    
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

        # for i in children: print(i, type(i))

        if(len(children) == 1): return children
        return node_classes.PowerExpr(children)

        # if (len(children)>2):
        #     if children[1] == '**':
        #         return node_classes.PowerExpr(children)
        # return children
    
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
        if len(children) > 1:
            return node_classes.ComplexVal(children)
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
    
    def expression_statement(self, children):
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
    
    def parameters_def(self, children):
        children = flatten(children)
        if(len(children) == 0): return None
        return children

    def params_def(self, children):
        children = flatten(children)
        return children

    def parameter_def(self, children):
        children = flatten(children)
        return children
    
    def datatype_f(self, children):
        children = flatten(children)
        return children
    
    def final_call(self, children):
        children = flatten(children)
        if(len(children) == 0): return None
        return children

    def datatype_call(self, children):
        children = flatten(children)
        return children
    
    def conditional_statement(self, children):
        children = flatten(children)
        return node_classes.ConditionalStatement(children)
    
    def if_statement(self, children):
        children = flatten(children)
        return node_classes.IfStatement(children)
    
    def else_statement(self, children):
        children = flatten(children)
        if(len(children) == 0): return None
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

    def type_declaration(self, children):
        children = flatten(children)
        return node_classes.TypeDeclaration(children)
    
    def return_statement(self, children):
        children = flatten(children)
        return node_classes.ReturnStatement(children)

    def exception_handling(self, children):
        children = flatten(children)
        return node_classes.ExceptionHandling(children)
    
    def catch_blocks(self, children):
        children = flatten(children)
        return children
    
    def cont_vals(self, children):
        children = flatten(children)
        return children
    
    def value_conts(self, children):
        children = flatten(children)
        return children