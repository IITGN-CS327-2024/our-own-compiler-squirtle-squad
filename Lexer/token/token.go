package token

const (
	Illegal = "ILLEGAL" // Error token
	EOF     = "EOF"     // End of file

	// Identifies & Literals
	Identifier  = "Identifier"
	Number      = "Number"
	Char        = "Char"
	String      = "String"
	EmptyString = "String"
	EmptyChar   = "Char"

	// Keywords
	Function            = "Function"
	ChildFunction       = "CHILDFUNCTION"
	Variable            = "Variable"
	Constant            = "Constant"
	Integer             = "Integer"
	Boolean             = "Boolean"
	Array               = "Array"
	Tuple               = "Tuple"
	Exception           = "Exception"
	True                = "True"
	False               = "False"
	If                  = "If"
	ElseIf              = "ElseIf"
	Else                = "Else"
	Return              = "Return"
	Void                = "Void"
	Try                 = "Try"
	Throw               = "Throw"
	Catch               = "Catch"
	Print               = "Print"
	For                 = "For"
	While               = "While"
	Length              = "Length"
	Slice               = "Slice"
	Break               = "Break"
	Continue            = "Continue"
	Or                  = "Or"
	And                 = "And"
	Not                 = "Not"
	String_k            = "String_k"
	Char_k              = "Char_k"
	Cons                = "Cons"
	Head                = "Head"
	Tail                = "Tail"
	Format              = "Format"
	Substr              = "Substr"
	Type                = "TYPE"
	Main                = "Main"
	Null                = "Null"
	ValueException      = "ValueException"
	TypeException       = "TypeException"
	ArithmeticException = "ArithmeticException"
	NullException       = "NullException"
	IndexException      = "IndexException"

	// Operators
	Equal           = "Equal"
	Assign          = "Assign"
	Plus            = "Plus"
	Increment       = "Increment"
	Minus           = "Minus"
	Decrement       = "Decrement"
	Star            = "Star"
	Slash           = "Slash"
	Mod             = "Mod"
	Bang            = "Bang"
	Dot             = "Dot"
	Less            = "Less"
	LessEqual       = "LessEqual"
	Greater         = "Greater"
	GreaterEqual    = "GreaterEqual"
	NotEqual        = "NotEqual"
	PlusEqual       = "PlusEqual"
	SlashEqual      = "SlashEqual"
	StarEqual       = "StarEqual"
	MinusEqual      = "MinusEqual"
	ModEqual        = "ModEqual"
	Power           = "Power"
	BitwiseNot      = "BitwiseNot"
	BitwiseAnd      = "BitwiseAnd"
	BitwiseOr       = "BitwiseOr"
	AndEqual        = "AndEqual"
	OrEqual         = "OrEqual"
	LeftShift       = "LeftShift"
	RightShift      = "RightShift"
	LeftShiftEqual  = "LeftShiftEqual"
	RightShiftEqual = "RightShiftEqual"

	// Delimiters
	Comma        = "Comma"
	Colon        = "Colon"
	Semicolon    = "Semicolon"
	LeftParen    = "LPar"
	RightParen   = "RPar"
	LeftBrace    = "LBrace"
	RightBrace   = "RBrace"
	LeftBracket  = "LSQB"
	RightBracket = "RSQB"

	// Quotations
	SingleQuote       = "'"
	DoubleQuote       = "\""
	StartMultiComment = "/*"
	EndMultiComment   = "*/"
)

// tokenType alias for a string -> just to keep things differentiated
type TokenType string

type Token struct {
	Type    TokenType
	Literal string
}

var keywords = map[string]TokenType{
	"func": Function,
	// "cfunc":               ChildFunction,
	"var":                 Variable,
	"const":               Constant,
	"int":                 Integer,
	"bool":                Boolean,
	"char":                Char_k,
	"arr":                 Array,
	"tuple":               Tuple,
	"Exception":           Exception,
	"true":                True,
	"false":               False,
	"if":                  If,
	"elseif":              ElseIf,
	"else":                Else,
	"return":              Return,
	"void":                Void,
	"try":                 Try,
	"throw":               Throw,
	"catch":               Catch,
	"print":               Print,
	"for":                 For,
	"while":               While,
	"len":                 Length,
	"slice":               Slice,
	"break":               Break,
	"continue":            Continue,
	"or":                  Or,
	"and":                 And,
	"not":                 Not,
	"string":              String_k,
	"cons":                Cons,
	"head":                Head,
	"tail":                Tail,
	"format":              Format,
	"substr":              Substr,
	"type":                Type,
	"main":                Main,
	"null":                Null,
	"ValueException":      ValueException,
	"ArithmeticException": ArithmeticException,
	"NullException":       NullException,
	"TypeException":       TypeException,
	"IndexException":      NullException,
}

// checks our keywords map for the scanned keyword.
// If its a keyword, return the TokenType else Identifier
func CheckIfKeyword(identifier string) TokenType {
	if token, ok := keywords[identifier]; ok {
		return token
	}

	return Identifier
}
