package lexer 

import (
	"myproject/Lexer/token"
)

type Lexer struct {
	input        string
	position     int
	nextPosition int
	ch           byte
}

func New(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar()
	return l
}

func (l *Lexer) NextToken() token.Token {

	var tok token.Token
	l.skipWhitespace()

	switch l.ch {
	case '=':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.Equal, Literal: literal}
		} else {
			tok = newToken(token.Assign, l.ch)
		}
	case '+':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.PlusEqual, Literal: literal}
		} else if(l.peekChar() == '+') {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.Increment, Literal: literal}
		}else {
			tok = newToken(token.Plus, l.ch)
		}
	case '.':
		tok = newToken(token.Dot, l.ch)

	case '-':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.MinusEqual, Literal: literal}
		} else if(l.peekChar() == '-') {
				ch := l.ch
				l.readChar()
				literal := string(ch) + string(l.ch)
				tok = token.Token{Type: token.Decrement, Literal: literal}	
		} else {
			tok = newToken(token.Minus, l.ch)
		}

	case '!':

		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.NotEqual, Literal: literal}
		} else {
			tok = newToken(token.Bang, l.ch)
		}

	case '*':

		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.StarEqual, Literal: literal}
		} else if l.peekChar() == '*' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.Power, Literal: literal}
		} else {
			tok = newToken(token.Star, l.ch)
		}

	case '/':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.SlashEqual, Literal: literal}
			
		} else if l.peekChar() == '*' {
			l.skipMultiLineComment()
			return l.NextToken()

		} else {
			tok = newToken(token.Slash, l.ch)
		}
	case '<':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.LessEqual, Literal: literal}
			
		} else if l.peekChar() == '<' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			if(l.peekChar() != '=') {
				tok = token.Token{Type: token.LeftShift, Literal: literal}
			} else {
				l.readChar()
				literal += string(l.ch)
				tok = token.Token{Type: token.LeftShiftEqual, Literal: literal}
			}	
		} else {
			tok = newToken(token.Less, l.ch)
		}

	case '>':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.GreaterEqual, Literal: literal}
			
		} else if l.peekChar() == '>' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			if(l.peekChar() != '=') {
				tok = token.Token{Type: token.RightShift, Literal: literal}
			} else {
				l.readChar()
				literal += string(l.ch)
				tok = token.Token{Type: token.RightShiftEqual, Literal: literal}
			}
		} else {
			tok = newToken(token.Greater, l.ch)
		}
	case ',':
		tok = newToken(token.Comma, l.ch)
	case ';':
		tok = newToken(token.Semicolon, l.ch)
	case ':':
		tok = newToken(token.Colon, l.ch)
	case '(':
		tok = newToken(token.LeftParen, l.ch)
	case ')':
		tok = newToken(token.RightParen, l.ch)
	case '{':
		tok = newToken(token.LeftBrace, l.ch)
	case '}':
		tok = newToken(token.RightBrace, l.ch)
	case '[':
		tok = newToken(token.LeftBracket, l.ch)
	case ']':
		tok = newToken(token.RightBracket, l.ch)
	case '"':
		tok.Type = token.String
		tok.Literal = l.readString()
		if tok.Literal == "" {
			tok.Type = token.EmptyString
		}
	case '~':
		tok.Type = token.BitwiseNot 
		tok.Literal = string(l.ch )

	case '%':
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.ModEqual, Literal: literal}
		} else {
			tok = newToken(token.Mod, l.ch)
		}

	case '|':

		if(l.peekChar() == '=') {
			ch := l.ch 
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.OrEqual, Literal: literal}
		} else {tok.Type = token.BitwiseOr 
		tok.Literal = string(l.ch)} 

	case '&':

		if(l.peekChar() == '=') {
			ch := l.ch 
			l.readChar()
			literal := string(ch) + string(l.ch)
			tok = token.Token{Type: token.AndEqual, Literal: literal}
		} else {tok.Type = token.BitwiseAnd
		tok.Literal = string(l.ch)}
	
	case 0:
		tok.Literal = ""
		tok.Type = token.EOF

	default:
		if isLetter(l.ch) {
			tok.Literal = l.readIdentifier()
			if(tok.Literal == "shrey_joshi") {
				l.skipSingleLineComment()
				return l.NextToken()
			}
			tok.Type = token.CheckIfKeyword(tok.Literal)
			return tok
		} else if isDigit(l.ch) {
			tok.Literal = l.readNumber()
			tok.Type = token.Number 
			return tok
		} else {
			tok = newToken(token.Illegal, l.ch)
		}
	}

	l.readChar()
	return tok
}

func newToken(tokenType token.TokenType, ch byte) token.Token {
	return token.Token{Type: tokenType, Literal: string(ch)}
}

func (l *Lexer) readChar() {
	l.ch = l.peekChar()
	l.position = l.nextPosition
	l.nextPosition += 1
}


func (l *Lexer) readString() string {
	pos := l.position + 1
	for {
		l.readChar()
		if l.ch == '"' || l.ch == 0 {
			break
		}
	}

	if pos == l.position { 
		return ""}

	return l.input[pos:l.position]
}

func (l *Lexer) readNumber() string {
	pos := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[pos:l.position]
}

func (l *Lexer) readIdentifier() string {

	pos := l.position
	l.readChar()
	for isLetter(l.ch) || isDigit(l.ch) {
		l.readChar()
	}

	return l.input[pos:l.position]
}

func isLetter(ch byte) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_'
}

func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

func (l *Lexer) skipWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\n' || l.ch == '\r' {
		l.readChar()
	}
}

func (l *Lexer) skipSingleLineComment() {
	for l.ch != '\n' && l.ch != 0 {
		l.readChar()
	}
	l.skipWhitespace()
}

func (l *Lexer) peekChar() byte {
	if l.nextPosition >= len(l.input) {
		return 0
	} else {
		return l.input[l.nextPosition]
	}
}

func (l *Lexer) skipMultiLineComment() {
	endFound := false

	for !endFound {
		if l.ch == 0 {
			endFound = true
		}

		if l.ch == '*' && l.peekChar() == '/' {
			endFound = true
			l.readChar()
		}

		l.readChar()
	}

	l.skipWhitespace()
}
