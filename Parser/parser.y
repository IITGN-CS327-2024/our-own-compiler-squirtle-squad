%{
package parser

%}

%token Break Continue Variable Identifier Constant 
%token PlusEqual SlashEqual StarEqual MinusEqual ModEqual AndEqual OrEqual LeftShiftEqual RightShiftEqual
%token Array Tuple String Number Char Boolean String_k Char_k
%token Length Format Cons Print Slice Return Substr Tail Head
%token If Else ElseIf While For Try Catch Throw
%token Exception ArithmeticException NullException IndexException ValueException TypeException
%token Function
%token Or And Not Assign
%token Bang Less Greater BitwiseNot Plus Minus Star Slash Mod BitwiseAnd BitwiseOr /* Dispensible*/
%token Equal NotEqual LessEqual GreaterEqual LeftShift RightShift Power Increment Decrement

%start program

%left BitwiseOr BitwiseAnd
%nonassoc Equal NotEqual
%nonassoc LessEqual GreaterEqual Greater Less
%left RightShift LeftShift
%left Plus Minus
%left Star Slash Mod
%right Power

%% 
program : statements

statements : statement
           | statement statements
           | /*empty*/

/* statement : variable_declaration ';'
          | function_declaration
          | conditional_statement
          | loop_statement
          | print_statement
          | exception_handling
          | expression_statement
          | return_statement
          | loop_control
          | variable_change ';'
          | cons_op 
          | throw_statement
          | array_declaration
          | tuple_declaration */

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

array_declaration: Array datatype Identifier ':' Number end_arr ';' 
                 | Array datatype Identifier Assign cont_vals

tuple_declaration: Tuple datatype Identifier Assign cont_vals 

string_nt : String | String '.' Format '(' string_items | Identifier '[' Number ']' | Substr '(' Identifier Number ',' Number ')'
string_items : Identifier ',' string_items | Identifier ')' ';'

/* number_nt : Number | Length '[' Identifier ']' | Identifier '[' Number ']' | Head '(' Identifier ')' | Tail '(' Identifier ')' */
char_nt : Char | Identifier '[' Number ']'
bool_nt  : Boolean | Identifier '[' Number ']' | condition

end_arr :  /* empty */ | ':' Number | ':' char_nt | ':' string_nt | ':' bool_nt
/* items : Number ',' items | Number ']' ';' | char_nt ',' items | char_nt ']' ';' | string_nt ',' items | string_nt ']' ';' | bool_nt ',' items | bool_nt ']' ';' */

datatype : Number 
         | Boolean
         | Char_k
         | String_k
         | Array
         | Tuple
         
function_declaration : Function Identifier '(' parameters_def ')' ':' datatype '{' statements '}'

parameters_def : /* empty */
                | parameter_def
                | parameter_def ',' parameters_def  

parameter_def : datatype Identifier

conditional_statement : If '(' condition ')' '{' statements '}' elseif_statements else_statement

elseif_statements : /* empty */
                  | ElseIf '(' condition ')' '{' statements '}' elseif_statements

else_statement : /* empty */
               | Else '{' statements '}'

loop_statement : While '(' condition ')' '{' statements '}'
               | For '(' var_init ';' condition ';' iterating ')' '{' statements '}'

var_init : variable_declaration | variable_change | Identifier
iterating: /* empty */ | variable_change

print_statement : Print ':' expression ';'

exception_handling : Try '{' statements '}' catch_blocks

catch_blocks :  Catch '(' exception_type Identifier ')' '{' statements '}' catch_blocks
              | Catch '(' Exception Identifier ')' '{' statements '}'

exception_type : ArithmeticException | NullException | IndexException | ValueException | TypeException

throw_statement : Throw exception_type '(' string_nt ')' ';'

expression_statement : expression ';'

condition : expression bi_operators expression | un_operators_pre expression | expression un_operators_post | condition_ condition | Not condition
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


/* vals : Number | char_nt | string_nt | bool_nt | expression | Identifier '(' parameters_call ')' | Identifier */
cont_vals : Slice '(' Identifier ',' Number ',' Number ')' | '[' number_conts | '[' string_conts | '[' char_conts | '[' bool_conts 
number_conts : Number ',' number_conts | Number ']'
string_conts : string_nt ',' string_conts | string_nt ']'
char_conts: char_nt ',' char_conts | char_nt ']'
bool_conts: bool_nt ',' bool_conts | bool_nt ']'

parameters_call : Identifier ',' parameters_call | Identifier

return_statement : Return expression ';'

/* expression: values | expression bi_operators expression | expression un_operators_post | un_operators_pre expression | '(' expression ')' */
expression: values | expression_ expression | expression__ | un_operators_pre expression | '(' expression ')'
expression_ : expression bi_operators
expression__ : expression un_operators_post
values : Number | Char | string_nt | Boolean | Identifier '(' parameters_call ')' | Identifier | Identifier '[' Number ']'

%%