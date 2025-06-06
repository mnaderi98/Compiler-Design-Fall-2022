from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled

from antlr4 import *
import ast


def main(input_text):
    input_stream = InputStream(input_text)
    lexer = JavaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParserLabeled(token_stream)
    parse_tree = parser.compilationUnit()
    ast_binary = ast.parse(parse_tree.toString(lexer.ruleNames, parse_tree.stop))
    print(ast_binary)


if __name__ == '__main__':
    main("""
    class Factorial{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac(10));
    }
}

class Fac {
    public int ComputeFac(int num){
        int num_aux ;
        if (num < 1)
            num_aux = 1 ;
        else
            num_aux = num * (this.ComputeFac(num-1)) ;
        return num_aux ;
    }
}""")
