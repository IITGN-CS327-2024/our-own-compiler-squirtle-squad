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
            line = line.split(",", 1)
            print(line[0].upper(), line[1])
            if(line[1].isnumeric()):
                yield Token(line[0].upper(), int(line[1]))
            else:
                yield Token(line[0].upper(), line[1])

def tree_to_graphviz(tree, graph=None):

    if graph is None:
        graph = Digraph()

    if isinstance(tree, node_classes.ASTNode):
        graph.node(str(id(tree)), label=str(tree))
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

program : statements 

statements : statement+

statement : variable_declaration_statement
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
           | ";"

variable_declaration_statement : variable_declaration ";"
variable_change_statement : variable_change ";"
 
loop_control : BREAK ";" | CONTINUE ";"
cons_op : CONS "(" IDENTIFIER "Comma" expression ")" ";"
variable_declaration : VARIABLE datatype IDENTIFIER 
                      | VARIABLE datatype IDENTIFIER ASSIGN condition 
                      | CONSTANT datatype IDENTIFIER ASSIGN condition 
                      | IDENTIFIER IDENTIFIER ASSIGN condition

variable_change : IDENTIFIER ASSIGN condition | IDENTIFIER opeq condition
                 | IDENTIFIER "[" expression "]" ASSIGN condition
                 | IDENTIFIER "[" expression "]" opeq condition

opeq : PLUSEQUAL       
	  | SLASHEQUAL      
	  | STAREQUAL       
	  | MINUSEQUAL      
	  | MODEQUAL        
      | ANDEQUAL  
      | OREQUAL   
      | LEFTSHIFTEQUAL  
      | RIGHTSHIFTEQUAL 

array_declaration: arr_datatype IDENTIFIER ":" NUMBER end_arr ";" 
                  | arr_datatype IDENTIFIER ":" IDENTIFIER end_arr ";" 
                  | arr_datatype IDENTIFIER ASSIGN cont_vals ";"

tuple_declaration: tup_datatype IDENTIFIER ASSIGN cont_vals ";"

end_arr :  | "[" NUMBER "]" | "[" CHAR "]" | "[" string_nt "]" | "[" bool_literals "]"

string_nt :STRING | STRING "Dot" FORMAT "(" string_items | IDENTIFIER "[" expression "]" | "Substr" "(" IDENTIFIER "Comma" expression "Comma" expression ")"
string_items : IDENTIFIER "Comma" string_items | IDENTIFIER ")"

number_nt : NUMBER | LENGTH "(" IDENTIFIER ")" | HEAD "(" IDENTIFIER ")" | TAIL "(" IDENTIFIER ")"

bool_literals: TRUE | FALSE

datatype : INTEGER 
          | BOOLEAN
          | CHAR_K
          | STRING_K
          | VOID
          | ARRAY INTEGER | ARRAY BOOLEAN | ARRAY CHAR_K | ARRAY STRING_K 
          | TUPLE INTEGER | TUPLE BOOLEAN | TUPLE CHAR_K | TUPLE STRING_K

arr_datatype : ARRAY INTEGER | ARRAY BOOLEAN | ARRAY CHAR_K | ARRAY STRING_K 
tup_datatype : TUPLE INTEGER | TUPLE BOOLEAN | TUPLE CHAR_K | TUPLE STRING_K

datatype_f : datatype | FUNCTION "(" final_call ")" ":" datatype
final_call: | datatype_call
datatype_call : datatype | datatype "Comma" datatype_call
         
function_declaration : FUNCTION IDENTIFIER "(" parameters_def ")" ":" datatype_f "{" statements "}" | FUNCTION MAIN "(" parameters_def ")" ":" datatype "{" statements "}"

parameters_def : | params_def
params_def : parameter_def | parameter_def "Comma" params_def  
parameter_def : datatype IDENTIFIER

type_declaration : TYPE IDENTIFIER ASSIGN FUNCTION "(" final_call ")" ":" datatype ";" 

conditional_statement : if_statement elseif_statements else_statement

if_statement : IF "(" condition ")" "{" statements "}"

elseif_statements : 
                   | ELSEIF "(" condition ")" "{" statements "}" elseif_statements

else_statement : 
                | ELSE "{" statements "}"

loop_statement : WHILE "(" condition ")" "{" statements "}"
                | FOR "(" var_init ";" condition ";" iterating ")" "{" statements "}"

var_init : variable_declaration | variable_change | IDENTIFIER
iterating:  | variable_change

print_statement : PRINT ":" condition ";"

exception_handling : TRY "{" statements "}" catch_blocks

catch_blocks : CATCH "(" exception_type IDENTIFIER ")" "{" statements "}" catch_blocks
              | CATCH "(" EXCEPTION IDENTIFIER ")" "{" statements "}"

exception_type : ARITHMETICEXCEPTION | NULLEXCEPTION | INDEXEXCEPTION | VALUEEXCEPTION | TYPEEXCEPTION

throw_statement : THROW exception_type "(" string_nt ")" ";"

expression_statement : condition ";"

condition:  condition1
condition1:  condition1 OR condition2 | condition2 
condition2: condition2 AND condition3 | condition3
condition3: NOT cond_terminal | cond_terminal
cond_terminal: expression | un_operators_pre expression | expression un_operators_post | expression comp_operators expression

un_operators_pre  : BANG | BITWISENOT
un_operators_post : INCREMENT | DECREMENT

comp_operators : LESS           
                | LESSEQUAL       
                | GREATER        
                | GREATEREQUAL    
 
cont_vals : SLICE "(" IDENTIFIER "Comma" expression "Comma" expression ")" | "[" value_conts 

value_conts : values "Comma" value_conts | values "]"

function_call : IDENTIFIER "(" parameters_call ")"

parameters_call : | params_call

params_call : IDENTIFIER "Comma" params_call | IDENTIFIER 
               | string_nt "Comma" params_call | string_nt
               | number_nt "Comma" params_call | number_nt 
               | bool_literals "Comma" params_call | bool_literals
               | CHAR "Comma" params_call | CHAR

return_statement : RETURN expression ";" | RETURN function_declaration 

expression : bitwise_expr
bitwise_expr: bitwise_expr BITWISEOR eq_expr| bitwise_expr BITWISEAND eq_expr| eq_expr 
eq_expr : eq_expr EQUAL shift_expr | eq_expr NOTEQUAL shift_expr | shift_expr
shift_expr : shift_expr LEFTSHIFT add_expr | shift_expr RIGHTSHIFT add_expr | add_expr
add_expr : add_expr PLUS mult_expr | add_expr MINUS mult_expr | mult_expr
mult_expr : mult_expr STAR power_expr | mult_expr SLASH power_expr | mult_expr MOD power_expr | power_expr
power_expr : power_expr POWER terminal_expr | terminal_expr
terminal_expr : values | "(" condition ")"

values: number_nt | CHAR | string_nt | bool_literals | cont_vals | function_call | IDENTIFIER | NULL 

%declare INTEGER BOOLEAN CHAR_K STRING VOID ARRAY TUPLE NUMBER CHAR NULL STRING_K
%declare ASSIGN PLUSEQUAL MINUSEQUAL STAREQUAL SLASHEQUAL MODEQUAL ANDEQUAL OREQUAL LEFTSHIFTEQUAL RIGHTSHIFTEQUAL
%declare BREAK CONTINUE CONS IDENTIFIER CONSTANT VARIABLE FUNCTION PRINT RETURN
%declare TRUE FALSE LENGTH HEAD TAIL FORMAT MAIN TYPE SLICE
%declare IF ELSEIF ELSE WHILE FOR TRY CATCH THROW 
%declare EXCEPTION ARITHMETICEXCEPTION NULLEXCEPTION INDEXEXCEPTION VALUEEXCEPTION TYPEEXCEPTION
%declare OR AND NOT BANG BITWISENOT INCREMENT DECREMENT LESS LESSEQUAL GREATER GREATEREQUAL
%declare BITWISEOR BITWISEAND EQUAL NOTEQUAL LEFTSHIFT RIGHTSHIFT PLUS MINUS STAR SLASH MOD POWER
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
    