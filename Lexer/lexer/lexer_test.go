package lexer

import (
	"testing"
	"Lexer/token"
)

func TestNextToken(t *testing.T) {
	input := `var int x1 = 69"
`

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
