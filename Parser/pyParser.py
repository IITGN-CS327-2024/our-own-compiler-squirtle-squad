from lark import Lark, Transformer, v_args, Tree
from lark.lexer import Lexer, Token
from graphviz import Digraph
import sys

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
            if(line[1].isnumeric()):
                yield Token(line[0].upper(), int(line[1]))
            else:
                yield Token(line[0].upper(), line[1])

def tree_to_graphviz(tree, graph=None):
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
!start: program "EOF"

!program : statements 

!statements : statement
           | statement statements

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

!variable_declaration_statement : variable_declaration "Semicolon"
!variable_change_statement : variable_change "Semicolon"
 
!loop_control : "Break" "Semicolon" | "Continue" "Semicolon"
!cons_op : "Cons" "LeftParen" "Identifier" "Comma" expression "RightParen" "Semicolon"
!variable_declaration : "Variable" datatype "Identifier" 
                      | "Variable" datatype "Identifier" "Assign" condition 
                      | "Constant" datatype "Identifier" "Assign" condition 

!variable_change : "Identifier" "Assign" condition | "Identifier" opeq condition  
!opeq : "PlusEqual"       
	  | "SlashEqual"      
	  | "StarEqual"       
	  | "MinusEqual"      
	  | "ModEqual"        
      | "AndEqual"  
      | "OrEqual"   
      | "LeftShiftEqual"  
      | "RightShiftEqual" 

!array_declaration: "Array" datatype "Identifier" "Colon" "Number" end_arr "Semicolon" 
                 | "Array" datatype "Identifier" "Assign" cont_vals "Semicolon"

!tuple_declaration: "Tuple" datatype "Identifier" "Assign" cont_vals "Semicolon"

!end_arr :  | "LeftBracket" "Number" "RightBracket" | "LeftBracket" "Char" "RightBracket" | "LeftBracket" string_nt "RightBracket" | "LeftBracket" bool_literals "RightBracket"

!string_nt : "String" | "String" "Dot" "Format" "LeftParen" string_items | "Identifier" "LeftBracket" "Number" "RightBracket" | "Substr" "LeftParen" "Identifier" "Number" "Comma" "Number" "RightParen"
!string_items : "Identifier" "Comma" string_items | "Identifier" "RightParen"

!number_nt : "Number" | "Length" "LeftBracket" "Identifier" "RightBracket" | "Head" "LeftParen" "Identifier" "RightParen" | "Tail" "LeftParen" "Identifier" "RightParen"

!bool_literals: "True" | "False"

!datatype : "Integer" 
         | "Boolean"
         | "Char_k"
         | "String_k"
         | "Array"
         | "Tuple"
         | "Void"
         
!function_declaration : "Function" "Identifier" "LeftParen" parameters_def "RightParen" "Colon" datatype "LeftBrace" statements "RightBrace" | "Function" "Main" "LeftParen" parameters_def "RightParen" "Colon" datatype "LeftBrace" statements "RightBrace"

!parameters_def : 
                | parameter_def
                | parameter_def "Comma" parameters_def  

!parameter_def : datatype "Identifier"

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

!catch_blocks :  "Catch" "LeftParen" exception_type "Identifier" "RightParen" "LeftBrace" statements "RightBrace" catch_blocks
              | "Catch" "LeftParen" "Exception" "Identifier" "RightParen" "LeftBrace" statements "RightBrace"

!exception_type : "ArithmeticException" | "NullException" | "IndexException" | "ValueException" | "TypeException"

!throw_statement : "Throw" exception_type "LeftParen" string_nt "RightParen" "Semicolon"

!expression_statement : condition "Semicolon"

!condition:  condition_ 
!condition_:  condition_ "Or" condition__ | condition__ 
!condition__: condition__ "And" condition___ | condition___
!condition___: "Not" cond_terminal | cond_terminal
!cond_terminal: expression | un_operators_pre expression | expression un_operators_post | expression comp_operators expression

!un_operators_pre  : "Bang" | "BitwiseNot"
!un_operators_post : "Increment" | "Decrement"

!comp_operators:  "Less"           
                |"LessEqual"       
                |"Greater"        
                |"GreaterEqual"    

!cont_vals : "Slice" "LeftParen" "Identifier" "Comma" number_nt "Comma" number_nt "RightParen" | "LeftBracket" value_conts

!value_conts : values "Comma" value_conts | values "RightBracket"

!parameters_call : "Identifier" "Comma" parameters_call | "Identifier"

!return_statement : "Return" expression "Semicolon"

!expression : bitwise_expr
!bitwise_expr: bitwise_expr "BitwiseOr" eq_expr| bitwise_expr "BitwiseAnd" eq_expr| eq_expr 
!eq_expr : eq_expr "Equal" shift_expr | eq_expr "NotEqual" shift_expr | shift_expr
!shift_expr : shift_expr "LeftShift" add_expr | shift_expr "RightShift" add_expr | add_expr
!add_expr : add_expr "Plus" mult_expr | add_expr "Minus" mult_expr | mult_expr
!mult_expr : mult_expr "Star" power_expr | mult_expr "Slash" power_expr | mult_expr "Mod" power_expr | power_expr
!power_expr : power_expr "Power" terminal_expr | terminal_expr
!terminal_expr : values | "LeftParen" expression "RightParen"

!values: number_nt | "Char" | string_nt | bool_literals | "Identifier" "LeftBrace" parameters_call "RightBrace" | "Identifier" | "Null" 
'''

if __name__ == "__main__":
    file_path = sys.argv[1]

    parser = Lark(grammar, parser='lalr', lexer=CustomLexer, strict=True)
    tree = parser.parse(file_path)
    graph = tree_to_graphviz(tree)
    graph.render('tree', format='png', view=True)