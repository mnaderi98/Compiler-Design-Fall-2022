import argparse
import os
from antlr4 import *
from gen.JavaLexer import JavaLexer
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from metric import DSCmetric
import argparse

import os
def main(args):
    stream = FileStream(r""+args.file, encoding="utf8")

    if os.path.exists(args.out):
        os.remove(args.out)
    output = open(r"" + args.out, "a")
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParserLabeled(token_stream)
    parser_tree = parser.compilationUnit()

    my_listener = DSCmetric()

    walker = ParseTreeWalker()
    walker.walk(t=parser_tree, listener=my_listener)

    statements = my_listener.inline_statements

    text = stream.strdata
    out = text
    index = 0
    for statement in statements:
        s, q, c, e, pre = statement
        if_else_statement = f"""if ({text[s:q]})
            {{
                {text[pre:s]}{text[q + 1:c]};
            }}
            else 
            {{
                {text[pre:s]}{text[c + 1:e + 1]};
            }}"""
        out = out[:pre + index] + if_else_statement + out[e + 2 + index:]
        index += len(if_else_statement) - e + pre - 2

    output.write(out)
    output.close()
if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-n', '--file',type=str,help='name of Java file',default=r'A.java')
    args = argparser.parse_args()

    argparser.add_argument( '-out', '--out', help='output java file path', default=r"B.java")
    args = argparser.parse_args()
    if args.file.split('.')[-1] == 'java':
        main(args)