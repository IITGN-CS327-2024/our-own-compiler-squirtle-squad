%{
package parser

%}

%token Break Continue Variable Identifier Constant 
%token PlusEqual SlashEqual StarEqual MinusEqual ModEqual AndEqual OrEqual LeftShiftEqual RightShiftEqual
%token Array Tuple String Number Char Boolean String_k Char_k
%token Length Format Cons Print Slice Return Substr Tail Head Main Null True False Void Integer
%token If Else ElseIf While For Try Catch Throw
%token Exception ArithmeticException NullException IndexException ValueException TypeException
%token Function EOF
%token Or And Not Assign
%token Bang Less Greater BitwiseNot Plus Minus Star Slash Mod BitwiseAnd BitwiseOr /* Dispensible*/
%token Equal NotEqual LessEqual GreaterEqual LeftShift RightShift Power Increment Decrement
%token Colon Semicolon Comma LeftParen RightParen LeftBrace Dot RightBrace LeftBracket RightBracket

%start program

/* %left BitwiseOr BitwiseAnd
%nonassoc Equal NotEqual
%nonassoc LessEqual GreaterEqual Greater Less
%left RightShift LeftShift
%left Plus Minus
%left Star Slash Mod
%right Power */

%% 
program : statements

statements : statement
           | statement statements

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
          | EOF
          | throw_statement
          | array_declaration
          | tuple_declaration

variable_declaration_statement : variable_declaration Semicolon
variable_change_statement : variable_change Semicolon
 
loop_control : Break Semicolon | Continue Semicolon
cons_op : Cons LeftParen Identifier Comma expression RightParen Semicolon
variable_declaration : Variable datatype Identifier 
                      | Variable datatype Identifier Assign expression 
                      | Constant datatype Identifier Assign expression 

variable_change : Identifier Assign expression | Identifier opeq expression  
opeq : PlusEqual       
	|SlashEqual      
	  |StarEqual       
	  |MinusEqual      
	  |ModEqual        
      |AndEqual  
      |OrEqual   
      |LeftShiftEqual  
      |RightShiftEqual 

array_declaration: Array datatype Identifier Colon number_nt end_arr Semicolon 
                 | Array datatype Identifier Assign cont_vals Semicolon

tuple_declaration: Tuple datatype Identifier Assign cont_vals Semicolon

string_nt : String | String Dot Format LeftParen string_items | Identifier LeftBracket number_nt RightBracket | Substr LeftParen Identifier Comma number_nt Comma number_nt RightParen
string_items : Identifier Comma string_items | Identifier RightParen

number_nt : Number | Length LeftParen Identifier RightParen  | Head LeftParen Identifier RightParen | Tail LeftParen Identifier RightParen
bool_nt  : bool_literals /*| Identifier LeftBracket Number RightBracket*/ | condition
bool_literals : True | False

end_arr :  /* empty */ | Colon number_nt | Colon Char | Colon string_nt | Colon bool_nt
/* items : Number Comma items | Number RightBracket Semicolon | char_nt Comma items | char_nt RightBracket Semicolon | string_nt Comma items | string_nt RightBracket Semicolon | bool_nt Comma items | bool_nt RightBracket Semicolon */

datatype : Integer 
         | Boolean
         | Char_k
         | String_k
         | Array
         | Tuple
         | Void 
         
function_declaration : Function Identifier LeftParen parameters_def RightParen Colon datatype LeftBrace statements RightBrace | Function Main LeftParen parameters_def RightParen Colon datatype LeftBrace statements RightBrace

parameters_def : /* empty */
                | parameter_def
                | parameter_def Comma parameters_def  

parameter_def : datatype Identifier

conditional_statement : If LeftParen condition RightParen LeftBrace statements RightBrace elseif_statements else_statement

elseif_statements : /* empty */
                  | ElseIf LeftParen condition RightParen LeftBrace statements RightBrace elseif_statements

else_statement : /* empty */
               | Else LeftBrace statements RightBrace

loop_statement : While LeftParen condition RightParen LeftBrace statements RightBrace
               | For LeftParen var_init Semicolon condition Semicolon iterating RightParen LeftBrace statements RightBrace

var_init : variable_declaration | variable_change | Identifier
iterating: /* empty */ | variable_change

print_statement : Print Colon values Semicolon

exception_handling : Try LeftBrace statements RightBrace catch_blocks

catch_blocks :  Catch LeftParen exception_type Identifier RightParen LeftBrace statements RightBrace catch_blocks
              | Catch LeftParen Exception Identifier RightParen LeftBrace statements RightBrace

exception_type : ArithmeticException | NullException | IndexException | ValueException | TypeException

throw_statement : Throw exception_type LeftParen string_nt RightParen Semicolon

expression_statement : expression Semicolon

condition : expression bi_operators expression  | condition_ condition | Not condition | un_operators_pre expression | expression un_operators_post
condition_ :  condition Or | condition And 

un_operators_pre  : Bang | BitwiseNot
un_operators_post : Increment | Decrement 

bi_operators : 
                 BitwiseOr    
                |BitwiseAnd

                |Equal
                |NotEqual  

                |Less           
                |LessEqual       
                |Greater        
                |GreaterEqual    
                
                |LeftShift       
                |RightShift    
                
                |Plus            
                |Minus     

                |Star            
                |Slash  
                |Mod 

                |Power   

cont_vals : Slice LeftParen Identifier Comma number_nt Comma number_nt RightParen | LeftBracket value_conts
value_conts : values Comma value_conts | values RightBracket

parameters_call : Identifier Comma parameters_call | Identifier | 

return_statement : Return expression Semicolon

expression : bitwise_expr
bitwise_expr: bitwise_expr BitwiseOr eq_expr| bitwise_expr BitwiseAnd eq_expr| eq_expr 
eq_expr : eq_expr Equal rel_expr | eq_expr NotEqual rel_expr | rel_expr
rel_expr : rel_expr Less shift_expr | rel_expr LessEqual shift_expr | rel_expr Greater shift_expr | rel_expr GreaterEqual shift_expr | shift_expr
shift_expr : shift_expr LeftShift add_expr | shift_expr RightShift add_expr | add_expr
add_expr : add_expr Plus mult_expr | add_expr Minus mult_expr | mult_expr
mult_expr : mult_expr Star power_expr | mult_expr Slash power_expr | power_expr
power_expr : power_expr Power terminal_expr | terminal_expr
terminal_expr : values | LeftParen expression RightParen

values : number_nt | Char | string_nt | bool_literals | Identifier LeftParen parameters_call RightParen | Identifier | Null 
%%