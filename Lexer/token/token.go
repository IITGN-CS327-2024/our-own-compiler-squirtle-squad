package token

const (
	Illegal = "ILLEGAL" // Error token
	EOF     = "EOF"     // End of file

	// Identifies & Literals
	Identifier  = "IDENTIFIER"
	Number      = "NUMBER"
	Char        = "CHARACTER"
	String      = "STRING"
	EmptyString = ""

	// Keywords
	Function      = "FUNCTION"
	ChildFunction = "CHILDFUNCTION"
	Variable      = "VARIABLE"
	Constant      = "CONSTANT"
	Integer       = "INTEGER"
	Boolean       = "BOOLEAN"
	Array         = "ARRAY"
	Tuple         = "TUPLE"
	Exception     = "EXCEPTION"
	True          = "TRUE"
	False         = "FALSE"
	If            = "IF"
	ElseIf        = "ELSEIF"
	Else          = "ELSE"
	Return        = "RETURN"
	Void          = "VOID"
	Try           = "TRY"
	Throw         = "THROW"
	Catch         = "CATCH"
	Print         = "PRINT"
	For           = "FOR"
	While         = "WHILE"
	Length        = "LENGTH"
	Slice         = "SLICE"
	Break         = "BREAK"
	Continue      = "CONTINUE"
	Or            = "OR"
	And           = "AND"
	Not           = "NOT"
	String_k      = "STRING_K"
	Cons          = "CONS"
	Head          = "HEAD"
	Tail          = "TAIL"
	Format        = "FORMAT"
	Substr        = "SUBSTR"
	Type          = "TYPE"
	Main          = "MAIN"

	// Operators
	Equal           = "=="
	Assign          = "="
	Plus            = "+"
	Increment       = "++"
	Minus           = "-"
	Decrement       = "--"
	Star            = "*"
	Slash           = "/"
	Mod             = "%"
	Bang            = "!"
	Dot             = "."
	Less            = "<"
	LessEqual       = "<="
	Greater         = ">"
	GreaterEqual    = ">="
	NotEqual        = "!="
	PlusEqual       = "+="
	SlashEqual      = "/="
	StarEqual       = "*="
	MinusEqual      = "-="
	ModEqual        = "%="
	Power           = "**"
	BitwiseNot      = "~"
	BitwiseAnd      = "&"
	BitwiseOr       = "|"
	AndEqual        = "&="
	OrEqual         = "|="
	LeftShift       = "<<"
	RightShift      = ">>"
	LeftShiftEqual  = "<<="
	RightShiftEqual = ">>="

	// Delimiters
	Comma        = ","
	Colon        = ":"
	Semicolon    = ";"
	LeftParen    = "("
	RightParen   = ")"
	LeftBrace    = "{"
	RightBrace   = "}"
	LeftBracket  = "["
	RightBracket = "]"
	Paranthesis  = "PARANTHESIS"
)

// tokenType alias for a string -> just to keep things differentiated
type TokenType string

type Token struct {
	Type    TokenType
	Literal string
}

var keywords = map[string]TokenType{
	"func":      Function,
	"cfunc":     ChildFunction,
	"var":       Variable,
	"const":     Constant,
	"int":       Integer,
	"bool":      Boolean,
	"arr":       Array,
	"tuple":     Tuple,
	"Exception": Exception,
	"true":      True,
	"false":     False,
	"if":        If,
	"elseif":    ElseIf,
	"else":      Else,
	"return":    Return,
	"void":      Void,
	"try":       Try,
	"throw":     Throw,
	"catch":     Catch,
	"print":     Print,
	"for":       For,
	"while":     While,
	"len":       Length,
	"slice":     Slice,
	"break":     Break,
	"continue":  Continue,
	"or":        Or,
	"and":       And,
	"not":       Not,
	"string":    String_k,
	"cons":      Cons,
	"head":      Head,
	"tail":      Tail,
	"format":    Format,
	"substr":    Substr,
	"type":      Type,
	"main":      Main,
}

// checks our keywords map for the scanned keyword.
// If its a keyword, return the TokenType else Identifier
func CheckIfKeyword(identifier string) TokenType {
	if token, ok := keywords[identifier]; ok {
		return token
	}

	return Identifier
}
