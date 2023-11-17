import re

# Define token patterns using regular expressions
TOKENS = [
    ('INT', r'int'),
    ('MAIN', r'main\(\)'),
    ('BEGIN', r'begin'),
    ('RETURN', r'return'),
    ('END', r'end'),
    ('WHILE', r'while'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifier
    ('NUM', r'\d+'),  # Integer constant
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('DIVIDE', r'/'),
    ('GT', r'>'),
    ('SEMICOLON', r';'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('BRACE_OPEN', r'{'),
    ('BRACE_CLOSE', r'}'),
    ('WHITESPACE', r'\s+'),  
]

# Lexer class
class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.text):
            for token_type, pattern in TOKENS:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.position)

                if match:
                    value = match.group(0)
                    token = (token_type, value)
                    self.tokens.append(token)
                    self.position = match.end()
                    break
            else:
                # If no match is found, raise an error
                raise Exception(f"Invalid character at position {self.position}: {self.text[self.position]}")

        return self.tokens

# Example usage
if __name__ == "__main__":
    input_text = ''
    with open('program.txt', 'r') as f:
        for line in f.readlines():
            input_text += line

    lexer = Lexer(input_text)
    tokens = lexer.tokenize()

    print("Tokens:")
    for token in tokens:
        print(token)
