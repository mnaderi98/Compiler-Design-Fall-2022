from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener
class DSCmetric(JavaParserLabeledListener):
    def __init__(self):
        self.nums = 0
        self.inline_statements = []

    def enterExpression20(self, ctx: JavaParserLabeled.Expression20Context):
        self.inline_statements.append((ctx.start.start, ctx.QUESTION().symbol.start, ctx.COLON().symbol.start, ctx.stop.stop, ctx.parentCtx.start.start))

