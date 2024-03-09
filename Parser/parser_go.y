%{
package parser

%}

%token Break Continue Variable Identifier Constant 
%token PlusEqual SlashEqual StarEqual MinusEqual ModEqual AndEqual OrEqual LeftShiftEqual RightShiftEqual
%token Array Tuple String Number Char Boolean String_k Char_k
%token Length Format Cons Print Slice Return Substr Tail Head
%token If Else ElseIf While For Try Catch Throw
%token Exception ArithmeticException NullException IndexException ValueException TypeException
%token Function EOF
%token True False Null
%token Or And Not Assign Void
%token Bang Less Greater BitwiseNot Plus Minus Star Slash Mod BitwiseAnd BitwiseOr /* Dispensible*/
%token Equal NotEqual LessEqual GreaterEqual LeftShift RightShift Power Increment Decrement

%start program

%% 
program : statements EOF

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
          | throw_statement
          | array_declaration
          | tuple_declaration

variable_declaration_statement : variable_declaration ';'
variable_change_statement : variable_change ';'
 
loop_control : Break ';' | Continue ';'
cons_op : Cons '(' Identifier ',' expression ')' ';'
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

array_declaration: Array datatype Identifier ':' Number ';' 
                 | Array datatype Identifier Assign cont_vals ';'

tuple_declaration: Tuple datatype Identifier Assign cont_vals ';'

string_nt : String | String '.' Format '(' string_items | Identifier '[' Number ']' | Substr '(' Identifier Number ',' Number ')'
string_items : Identifier ',' string_items | Identifier ')'

number_nt : Number | Length '[' Identifier ']' | Head '(' Identifier ')' | Tail '(' Identifier ')'
/* char_nt : Char | Identifier '[' Number ']' */

/* bool_nt  : bool_literals | condition */

bool_literals: True | False

/* end_arr :   | '(' number_nt ')' | '(' Char ')' | '(' string_nt ')' | '(' bool_nt ')' */

datatype : Number 
         | Boolean
         | Char_k
         | String_k
         | Array
         | Tuple
         | Void
         
function_declaration : Function Identifier '(' parameters_def ')' ':' datatype '{' statements '}'

parameters_def : 
                | parameter_def
                | parameter_def ',' parameters_def  

parameter_def : datatype Identifier

conditional_statement : If '(' condition ')' '{' statements '}' elseif_statements else_statement

elseif_statements : 
                  | ElseIf '(' condition ')' '{' statements '}' elseif_statements

else_statement : 
               | Else '{' statements '}'

loop_statement : While '(' condition ')' '{' statements '}'
               | For '(' var_init ';' condition ';' iterating ')' '{' statements '}'

var_init : variable_declaration | variable_change | Identifier
iterating:  | variable_change

print_statement : Print ':' expression ';'

exception_handling : Try '{' statements '}' catch_blocks

catch_blocks :  Catch '(' exception_type Identifier ')' '{' statements '}' catch_blocks
              | Catch '(' Exception Identifier ')' '{' statements '}'

exception_type : ArithmeticException | NullException | IndexException | ValueException | TypeException

throw_statement : Throw exception_type '(' string_nt ')' ';'

expression_statement : values ';'

condition:  condition_ 
condition_:  condition_ Or condition__ | condition__ 
condition__: condition__ And condition___ | condition___
condition___: Not cond_terminal | cond_terminal
cond_terminal: expression | un_operators_pre expression | expression un_operators_post | expression comp_operators expression

un_operators_pre  : Bang | BitwiseNot
un_operators_post : Increment | Decrement

comp_operators:  Less           
                |LessEqual       
                |Greater        
                |GreaterEqual    

cont_vals : Slice '(' Identifier ',' number_nt ',' number_nt ')' | '[' value_conts

value_conts : values ',' value_conts | values ']'

parameters_call : Identifier ',' parameters_call | Identifier

return_statement : Return expression ';'

expression : bitwise_expr
bitwise_expr: bitwise_expr BitwiseOr eq_expr| bitwise_expr BitwiseAnd eq_expr| eq_expr 
eq_expr : eq_expr Equal shift_expr | eq_expr NotEqual shift_expr | shift_expr
shift_expr : shift_expr LeftShift add_expr | shift_expr RightShift add_expr | add_expr
add_expr : add_expr Plus mult_expr | add_expr Minus mult_expr | mult_expr
mult_expr : mult_expr Star power_expr | mult_expr Slash power_expr | mult_expr Mod power_expr | power_expr
power_expr : power_expr Power terminal_expr | terminal_expr
terminal_expr : values | '(' expression ')'

values: number_nt | Char | string_nt | bool_literals | Identifier '{' parameters_call '}' | Identifier | Null 

%%