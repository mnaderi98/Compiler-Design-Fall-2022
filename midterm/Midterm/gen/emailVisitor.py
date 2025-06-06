# Generated from E:/01021/Compiler/Midterm/grammar\email.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .emailParser import emailParser
else:
    from emailParser import emailParser

# This class defines a complete generic visitor for a parse tree produced by emailParser.

class emailVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by emailParser#start.
    def visitStart(self, ctx:emailParser.StartContext):
        return self.visitChildren(ctx)



del emailParser