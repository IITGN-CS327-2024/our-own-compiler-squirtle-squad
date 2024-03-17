from lark import Lark, Transformer, v_args, Tree
from lark.lexer import Lexer, Token
from graphviz import Digraph
import ast_transform
import sys
import rich 
import node_classes

class CustomLexer(Lexer):
    def __init__(self,lexer_conf):
        pass
    def lex(self,data):
        #read the file data and store in string split the string according to new line
        try:
            with open(data,'r',encoding="utf8") as file:
                file_contents=file.read()
        except FileNotFoundError:
            print(f"File Not present")
        code_lines=file_contents.splitlines()
        #split each lines via comma and store in array
        for line in code_lines:
            line = line.split(",")
            print(line[0].upper(), line[1])
            if(line[1].isnumeric()):
                yield Token(line[0].upper(), int(line[1]))
            else:
                yield Token(line[0].upper(), line[1])

def tree_to_graphviz(tree, graph=None):

    if graph is None:
        graph = Digraph()

    if isinstance(tree, node_classes.ASTNode):
        children = vars(tree).items()
        for _,child in children:
            if isinstance(child, node_classes.ASTNode):
                graph.node(str(id(child)), label = str(child))
                graph.edge(str(id(tree)), str(id(child)))
                tree_to_graphviz(child, graph)

            else:
                graph.node(str(id(child)), label=str(child))
                graph.edge(str(id(tree)), str(id(child)))
    return graph

def tree_to_graphviz_lark(tree, graph=None):
    if graph is None:
        graph = Digraph()

    if isinstance(tree, Tree):
        for child in tree.children:
            if isinstance(child, Tree):
                graph.node(str(id(child)), label=child.data)
                graph.edge(str(id(tree)), str(id(child)))
                tree_to_graphviz(child, graph)
            else:
                graph.node(str(id(child)), label=str(child))
                graph.edge(str(id(tree)), str(id(child)))
    return graph

grammar = '''
start: program "EOF"

!program : statements 

!statements : statement+

!statement : variable_declaration_statement
           | function_declaration
           | conditional_statement
           | loop_statement
           | print_statement
           | exception_handling
           | expression_statement
           | return_statement
           | loop_control
           | variable_change_statement
           | cons_op 
           | throw_statement
           | array_declaration
           | tuple_declaration
           | type_declaration
           | "Semicolon"

!variable_declaration_statement : variable_declaration "Semicolon"
!variable_change_statement : variable_change "Semicolon"
 
!loop_control : "Break" "Semicolon" | "Continue" "Semicolon"
!cons_op : "Cons" "LeftParen" "Identifier" "Comma" expression "RightParen" "Semicolon"
!variable_declaration : "Variable" datatype "Identifier" 
                      | "Variable" datatype "Identifier" "Assign" condition 
                      | "Constant" datatype "Identifier" "Assign" condition 
                      | "Identifier" "Identifier" "Assign" condition

!variable_change : "Identifier" "Assign" condition | "Identifier" opeq condition
                 | "Identifier" "LeftBracket" expression "RightBracket" "Assign" condition
                 | "Identifier" "LeftBracket" expression "RightBracket" opeq condition

!opeq : "PlusEqual"       
	  | "SlashEqual"      
	  | "StarEqual"       
	  | "MinusEqual"      
	  | "ModEqual"        
      | "AndEqual"  
      | "OrEqual"   
      | "LeftShiftEqual"  
      | "RightShiftEqual" 

!array_declaration: arr_datatype "Identifier" "Colon" "Number" end_arr "Semicolon" 
                  | arr_datatype "Identifier" "Colon" "Identifier" end_arr "Semicolon" 
                  | arr_datatype "Identifier" "Assign" cont_vals "Semicolon"

!tuple_declaration: tup_datatype "Identifier" "Assign" cont_vals "Semicolon"

!end_arr :  | "LeftBracket" "Number" "RightBracket" | "LeftBracket" "Char" "RightBracket" | "LeftBracket" string_nt "RightBracket" | "LeftBracket" bool_literals "RightBracket"

!string_nt : "String" | "String" "Dot" "Format" "LeftParen" string_items | "Identifier" "LeftBracket" expression "RightBracket" | "Substr" "LeftParen" "Identifier" "Comma" expression "Comma" expression "RightParen"
!string_items : "Identifier" "Comma" string_items | "Identifier" "RightParen"

!number_nt : "Number" | "Length" "LeftParen" "Identifier" "RightParen" | "Head" "LeftParen" "Identifier" "RightParen" | "Tail" "LeftParen" "Identifier" "RightParen"

!bool_literals: "True" | "False"

!datatype : "Integer" 
          | "Boolean"
          | "Char_k"
          | "String_k"
          | "Void"
          | "Array" "Integer" | "Array" "Boolean" | "Array" "Char_k" | "Array" "String_k" 
          | "Tuple" "Integer" | "Tuple" "Boolean" | "Tuple" "Char_k" | "Tuple" "String_k"

!arr_datatype : "Array" "Integer" | "Array" "Boolean" | "Array" "Char_k" | "Array" "String_k" 
!tup_datatype : "Tuple" "Integer" | "Tuple" "Boolean" | "Tuple" "Char_k" | "Tuple" "String_k"

!datatype_f : datatype | "Function" "LeftParen" final_call "RightParen" "Colon" datatype
!final_call: | datatype_call
!datatype_call : datatype | datatype "Comma" datatype_call
         
!function_declaration : "Function" "Identifier" "LeftParen" parameters_def "RightParen" "Colon" datatype_f "LeftBrace" statements "RightBrace" | "Function" "Main" "LeftParen" parameters_def "RightParen" "Colon" datatype "LeftBrace" statements "RightBrace"

!parameters_def : | params_def
!params_def : parameter_def | parameter_def "Comma" params_def  
!parameter_def : datatype "Identifier"

!type_declaration : "TYPE" "Identifier" "Assign" "Function" "LeftParen" final_call "RightParen" "Colon" datatype "Semicolon" 

!conditional_statement : "If" "LeftParen" condition "RightParen" "LeftBrace" statements "RightBrace" elseif_statements else_statement

!elseif_statements : 
                   | "ElseIf" "LeftParen" condition "RightParen" "LeftBrace" statements "RightBrace" elseif_statements

!else_statement : 
                | "Else" "LeftBrace" statements "RightBrace"

!loop_statement : "While" "LeftParen" condition "RightParen" "LeftBrace" statements "RightBrace"
                | "For" "LeftParen" var_init "Semicolon" condition "Semicolon" iterating "RightParen" "LeftBrace" statements "RightBrace"

!var_init : variable_declaration | variable_change | "Identifier"
!iterating:  | variable_change

!print_statement : "Print" "Colon" expression "Semicolon"

!exception_handling : "Try" "LeftBrace" statements "RightBrace" catch_blocks

!catch_blocks : "Catch" "LeftParen" exception_type "Identifier" "RightParen" "LeftBrace" statements "RightBrace" catch_blocks
              | "Catch" "LeftParen" "Exception" "Identifier" "RightParen" "LeftBrace" statements "RightBrace"

!exception_type : "ArithmeticException" | "NullException" | "IndexException" | "ValueException" | "TypeException"

!throw_statement : "Throw" exception_type "LeftParen" string_nt "RightParen" "Semicolon"

!expression_statement : condition "Semicolon"

!condition:  condition1
!condition1:  condition1 "Or" condition2 | condition2 
!condition2: condition2 "And" condition3 | condition3
!condition3: "Not" cond_terminal | cond_terminal
!cond_terminal: expression | un_operators_pre expression | expression un_operators_post | expression comp_operators expression

!un_operators_pre  : "Bang" | "BitwiseNot"
!un_operators_post : "Increment" | "Decrement"

!comp_operators : "Less"           
                | "LessEqual"       
                | "Greater"        
                | "GreaterEqual"    
 
!cont_vals : "Slice" "LeftParen" "Identifier" "Comma" expression "Comma" expression "RightParen" | "LeftBracket" value_conts 

!value_conts : values "Comma" value_conts | values "RightBracket"

!function_call : "Identifier" "LeftParen" parameters_call "RightParen"

!parameters_call : | params_call

!params_call : "Identifier" "Comma" params_call | "Identifier" 
               | string_nt "Comma" params_call | string_nt
               | number_nt "Comma" params_call | number_nt 
               | bool_literals "Comma" params_call | bool_literals
               | "Char" "Comma" params_call | "Char"

!return_statement : "Return" expression "Semicolon" | "Return" function_declaration 

!expression : bitwise_expr
!bitwise_expr: bitwise_expr "BitwiseOr" eq_expr| bitwise_expr "BitwiseAnd" eq_expr| eq_expr 
!eq_expr : eq_expr "Equal" shift_expr | eq_expr "NotEqual" shift_expr | shift_expr
!shift_expr : shift_expr "LeftShift" add_expr | shift_expr "RightShift" add_expr | add_expr
!add_expr : add_expr "Plus" mult_expr | add_expr "Minus" mult_expr | mult_expr
!mult_expr : mult_expr "Star" power_expr | mult_expr "Slash" power_expr | mult_expr "Mod" power_expr | power_expr
!power_expr : power_expr "Power" terminal_expr | terminal_expr
!terminal_expr : values | "LeftParen" condition "RightParen"

!values: number_nt | "Char" | string_nt | bool_literals | cont_vals | function_call | "Identifier" | "Null" 
'''

def visualize(obj):

    try:
        children = vars(obj).items()
        for _, value in children:
            print(value)
            visualize(value)

    except:
        pass

if __name__ == "__main__": 
    file_path = sys.argv[1]

    parser = Lark(grammar, parser='lalr', lexer=CustomLexer, strict=True)
    transformer = ast_transform.OurTransformer()
    concrete_tree = parser.parse(file_path)
    ast = transformer.transform(concrete_tree)
    rich.print(concrete_tree)
    graph = tree_to_graphviz(ast)
    graph.render('tree',format='png', view=True)
    