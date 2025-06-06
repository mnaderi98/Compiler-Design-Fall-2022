from typing import List

from antlr4 import *
import queue
import argparse
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener
class TreeNode:
    def __init__(self, value, child, brother):
        self.Value = value
        self.Child = child
        self.Brother = brother

class ast_creator():
    def __init__(self):
        self.Current = None
        self.Root = None

    def MakeNode(self, Value, Child, Brother):
        Node = TreeNode(Value, Child, Brother)
        if self.Root is None:
            self.Root = Node
            self.Current = Node
        return Node

    def AddBrother(self, Node, Bro):
        if Node.Brother is None:
            Node.Brother = Bro
        else:
            self.Current = Node.Brother
            while self.Current.Brother is not None:
                self.Current = self.Current.Brother
            self.Current.Brother = Bro
        self.Current = Bro

    def AddChild(self, Node, Child):
        if Node.Child is None:
            Node.Child = Child
        else:
            self.Current = Node.Child
        while self.Current.Brother is not None:
            self.Current = self.Current.Brother
        self.Current.Brother = Child
        self.Current = Child

class ConstructAbstractSyntaxTreeListener(JavaParserLabeledListener):
    def __init__(self):
        self.AST = ast_creator()
        self.Q = queue.Queue()

    def exitOperations_expression(self, ctx:MiniJavaParser.Operations_expressionContext):
        Child1 = self.AST.MakeNode(ctx.expression(0).value_attr, None, None)
        Child2 = self.AST.MakeNode(ctx.expression(1).value_attr, None, None)
        self.AST.AddBrother(Child1, Child2)
        Parent = self.AST.MakeNode(ctx.operations().getText(), Child1, None)
        ctx.value_attr = Parent

    def exitEqual_statement(self, ctx: MiniJavaParser.Equal_statementContext):
        Child1 = self.AST.MakeNode(ctx.identifier().value_attr, None, None)
        Child2 = self.AST.MakeNode(ctx.expression().value_attr, None, None)
        self.AST.AddBrother(Child1, Child2)
        Parent = self.AST.MakeNode('=', Child1, None)
        ctx.value_attr = Parent
        self.AST.Root = Parent

    def exitIf_statement(self, ctx:MiniJavaParser.If_statementContext):
        Child0 = self.AST.MakeNode(ctx.expression().value_attr, None, None)
        Child1 = self.AST.MakeNode(ctx.statement(0).value_attr, None, None)
        Child2 = self.AST.MakeNode(ctx.statement(1).value_attr, None, None)
        self.AST.AddBrother(Child0, Child1)
        self.AST.AddBrother(Child1, Child2)
        Parent = self.AST.MakeNode('if', Child0, None)
        ctx.value_attr = Parent

    def enterWhile_statement(self, ctx:MiniJavaParser.While_statementContext):
        Child0 = self.AST.MakeNode(ctx.expression().value_attr, None, None)
        Child1 = self.AST.MakeNode(ctx.statement(0).value_attr, None, None)
        self.AST.AddBrother(Child0, Child1)
        Parent = self.AST.MakeNode('while', Child0, None)
        ctx.value_attr = Parent

    def exitKeywords(self, ctx:MiniJavaParser.KeywordsContext):
        Child = self.AST.MakeNode(ctx.getText(), None, None)
        ctx.value_attr = Child

    def exitWord(self, ctx:MiniJavaParser.WordContext):
        Child = self.AST.MakeNode(ctx.getText(), None, None)
        ctx.value_attr = Child

    def PrintTree(self, node=None, level=1):
        if node is None:
            print("--------     ----------")
            return
        if not self.Q.empty():
            print('Parent:', str(self.Q.get().Value))
            print('\t' * level, end='')
        while node is not None:
            print(node.Value, '\t───\t', end='')
            if node.Child is not None:
                self.Q.put(node.Child)
                self.Q.put(node)
            node = node.Brother
            if node is None:
                print(' ', end='\n')
        if not self.Q.empty():
            self.PrintTree(node=self.Q.get(), level=level + 1)



def get_ast_str(ast_list: List[ast_creator], obj_name='DSB', start_str="", num_of_space=0):
    indent = " " * num_of_space
    for ast in ast_list:
        output_code = f"{indent}{obj_name} = QDoubleSpinBox()\n"
        for at in ast.attrs:
            tag = at.tag
            val = at.value
            at_str = indent+_attributes_factory[tag].format(obj_name=obj_name, value=f"{val[1:-1]}")
            output_code += at_str
        start_str += output_code
    return start_str
