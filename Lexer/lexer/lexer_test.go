package lexer

import (
	"myproject/Lexer/token"
	"testing"
)
// var x = 10;
func TestNextToken(t *testing.T) {
	input := `var int x1 = 69`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "x1"},
		{token.Assign, "="},
		{token.Number, "69"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestKeywords(t *testing.T) {
	input := `func cfunc var const int bool arr tuple Exception true false if elseif else return void try throw catch print for while len slice break continue or and not string`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.Function, "func"},
		{token.ChildFunction, "cfunc"},
		{token.Variable, "var"},
		{token.Constant, "const"},
		{token.Integer, "int"},
		{token.Boolean, "bool"},
		{token.Array, "arr"},
		{token.Tuple, "tuple"},
		{token.Exception, "Exception"},
		{token.True, "true"},
		{token.False, "false"},
		{token.If, "if"},
		{token.ElseIf, "elseif"},
		{token.Else, "else"},
		{token.Return, "return"},
		{token.Void, "void"},
		{token.Try, "try"},
		{token.Throw, "throw"},
		{token.Catch, "catch"},
		{token.Print, "print"},
		{token.For, "for"},
		{token.While, "while"},
		{token.Length, "len"},
		{token.Slice, "slice"},
		{token.Break, "break"},
		{token.Continue, "continue"},
		{token.Or, "or"},
		{token.And, "and"},
		{token.Not, "not"},
		{token.String_k, "string"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestOperators(t *testing.T) {
	input := `== = + ++ - -- * / % ! < <= > >= != += /= *= -= %= ** ~ & | &= |= << >> <<= >>=`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.Equal, "=="},
		{token.Assign, "="},
		{token.Plus, "+"},
		{token.Increment, "++"},
		{token.Minus, "-"},
		{token.Decrement, "--"},
		{token.Star, "*"},
		{token.Slash, "/"},
		{token.Mod, "%"},
		{token.Bang, "!"},
		{token.Less, "<"},
		{token.LessEqual, "<="},
		{token.Greater, ">"},
		{token.GreaterEqual, ">="},
		{token.NotEqual, "!="},
		{token.PlusEqual, "+="},
		{token.SlashEqual, "/="},
		{token.StarEqual, "*="},
		{token.MinusEqual, "-="},
		{token.ModEqual, "%="},
		{token.Power, "**"},
		{token.BitwiseNot, "~"},
		{token.BitwiseAnd, "&"},
		{token.BitwiseOr, "|"},
		{token.AndEqual, "&="},
		{token.OrEqual, "|="},
		{token.LeftShift, "<<"},
		{token.RightShift, ">>"},
		{token.LeftShiftEqual, "<<="},
		{token.RightShiftEqual, ">>="},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestDelimiters(t *testing.T) {
	input := `(){}[],:;`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.LeftParen, "("},
		{token.RightParen, ")"},
		{token.LeftBrace, "{"},
		{token.RightBrace, "}"},
		{token.LeftBracket, "["},
		{token.RightBracket, "]"},
		{token.Comma, ","},
		{token.Colon, ":"},
		{token.Semicolon, ";"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestSmallProgram1(t *testing.T) {
	input := `var int x1 = 30
	var int x2 = 420
	var int x3 = 1337
	var int x4 = 9001
	var int x5 = 80085
	`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "x1"},
		{token.Assign, "="},
		{token.Number, "30"},
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "x2"},
		{token.Assign, "="},
		{token.Number, "420"},
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "x3"},
		{token.Assign, "="},
		{token.Number, "1337"},
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "x4"},
		{token.Assign, "="},
		{token.Number, "9001"},
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "x5"},
		{token.Assign, "="},
		{token.Number, "80085"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestForLoop(t *testing.T) {
	input := `for ( var int i = 0; i < 10; i++ ) {
		print :i ; 
	}`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.For, "for"},
		{token.LeftParen, "("},
		{token.Variable, "var"},
		{token.Integer, "int"},
		{token.Identifier, "i"},
		{token.Assign, "="},
		{token.Number, "0"},
		{token.Semicolon, ";"},
		{token.Identifier, "i"},
		{token.Less, "<"},
		{token.Number, "10"},
		{token.Semicolon, ";"},
		{token.Identifier, "i"},
		{token.Increment, "++"},
		{token.RightParen, ")"},
		{token.LeftBrace, "{"},
		{token.Print, "print"},
		// {token.LeftParen, "("},
		{token.Colon, ":"},
		{token.Identifier, "i"},
		// {token.RightParen, ")"},
		{token.Semicolon, ";"},
		{token.RightBrace, "}"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestWhileLoop(t *testing.T) {
	input := `while ( i < 10 ) {
		print : i ;
	}`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.While, "while"},
		{token.LeftParen, "("},
		{token.Identifier, "i"},
		{token.Less, "<"},
		{token.Number, "10"},
		{token.RightParen, ")"},
		{token.LeftBrace, "{"},
		{token.Print, "print"},
		{token.Colon, ":"},
		// {token.LeftParen, "("},
		{token.Identifier, "i"},
		// {token.RightParen, ")"},
		{token.Semicolon, ";"},
		{token.RightBrace, "}"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestIfElse(t *testing.T) {
	// add elseif also
	input := `if ( i < 10 ) {
		print : i ;
	} 
	elseif ( i == 10 ) {
		break;
	}
		else {
		print : "i is greater than 10" ;
	}`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.If, "if"},
		{token.LeftParen, "("},
		{token.Identifier, "i"},
		{token.Less, "<"},
		{token.Number, "10"},
		{token.RightParen, ")"},
		{token.LeftBrace, "{"},
		{token.Print, "print"},
		{token.Colon, ":"},
		// {token.LeftParen, "("},
		{token.Identifier, "i"},
		// {token.RightParen, ")"},
		{token.Semicolon, ";"},
		{token.RightBrace, "}"},
		{token.ElseIf, "elseif"},
		{token.LeftParen, "("},
		{token.Identifier, "i"},
		{token.Equal, "=="},
		{token.Number, "10"},
		{token.RightParen, ")"},
		{token.LeftBrace, "{"},
		{token.Break, "break"},
		{token.Semicolon, ";"},
		{token.RightBrace, "}"},
		{token.Else, "else"},
		{token.LeftBrace, "{"},
		{token.Print, "print"},
		{token.Colon, ":"},
		// {token.LeftParen, "("},
		{token.String, "i is greater than 10"},
		// {token.RightParen, ")"},
		{token.Semicolon, ";"},
		{token.RightBrace, "}"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}

func TestFuncDefin(t *testing.T) {
	input := `func shrey ( string spoiler , string name) : string {
		print : "Hello, World!" ;
		var string s = "gpl" ;
		return s ;
	}`

	tests := []struct {
		expectedType    token.TokenType
		expectedLiteral string
	}{
		{token.Function, "func"},
		{token.Identifier, "shrey"},
		{token.LeftParen, "("},
		{token.String_k, "string"},
		{token.Identifier, "spoiler"},
		{token.Comma, ","},
		{token.String_k, "string"},
		{token.Identifier, "name"},
		{token.RightParen, ")"},
		{token.Colon, ":"},
		{token.String_k, "string"},
		{token.LeftBrace, "{"},
		{token.Print, "print"},
		{token.Colon, ":"},
		// {token.LeftParen, "("},
		{token.String, "Hello, World!"},
		// {token.RightParen, ")"},
		{token.Semicolon, ";"},
		{token.Variable, "var"},
		{token.String_k, "string"},
		{token.Identifier, "s"},
		{token.Assign, "="},
		{token.String, "gpl"},
		{token.Semicolon, ";"},
		{token.Return, "return"},
		// {token.LeftParen, "("},
		{token.Identifier, "s"},
		// {token.RightParen, ")"},
		{token.Semicolon, ";"},
		{token.RightBrace, "}"},
	}

	l := New(input)

	for i, tt := range tests {
		tok := l.NextToken()

		if tok.Type != tt.expectedType {
			t.Fatalf("tests[%d] - tokentype wrong. expected=%q, got=%q",
				i, tt.expectedType, tok.Type)
		}

		if tok.Literal != tt.expectedLiteral {
			t.Fatalf("tests[%d] - literal wrong. expected=%q, got=%q",
				i, tt.expectedLiteral, tok.Literal)
		}
	}
}
