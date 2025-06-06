from antlr4 import *
from gen.JavaLexer import JavaLexer
import os

def main(input_file, output_file):
    file_stream = FileStream(r""+input_file)
    if os.path.exists(output_file):
        os.remove(output_file)
    output_stream = open(r""+output_file, "a")
    lexer = JavaLexer(file_stream)
    token = lexer.nextToken()

    while token.type != Token.EOF:
        text = token.text
        prev = 0
        if token.type == lexer.COMMENT:
            text = "//" + text[2:-2]
            text = text.replace("\n    ", "\n")
            text = text.replace("\n", "\n//")
            text += "\n"
            prev = 0
            token = lexer.nextToken()
            t = token.text
            while token.type == lexer.LINE_COMMENT or token.type == lexer.COMMENT or token.text == "\n" or token.text == "\n    " or token.text == "\n        ":
                prev = 1
                token = lexer.nextToken()
        if token.type == lexer.LINE_COMMENT:
            text = text + "\n"
            text = text.replace("\n    ", "\n")
            prev = 0
            token = lexer.nextToken()
            t = token.text
            while token.type == lexer.LINE_COMMENT or token.type == lexer.COMMENT or token.text == "\n" or token.text == "\n    " or token.text == "\n        ":
                prev = 1
                token = lexer.nextToken()

        output_stream.write(text)
        if prev == 0:
            token = lexer.nextToken()
        prev = 0

    output_stream.close()

if __name__ == '__main__':
    input_file = "A.java";
    output_file = "B.java";

    main(input_file, output_file)
