# Generated from E:/01021/Compiler/Midterm/grammar\email.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,1,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,11,8,0,10,
        0,12,0,14,9,0,1,0,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,4,1,25,
        8,1,11,1,12,1,26,1,2,4,2,30,8,2,11,2,12,2,31,0,0,3,1,1,3,0,5,0,1,
        0,2,10,0,33,33,36,36,38,38,40,45,48,59,61,61,65,90,95,95,97,122,
        126,126,4,0,45,45,48,57,65,90,97,122,34,0,1,1,0,0,0,1,7,1,0,0,0,
        3,24,1,0,0,0,5,29,1,0,0,0,7,12,3,3,1,0,8,9,5,46,0,0,9,11,3,3,1,0,
        10,8,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,15,1,0,
        0,0,14,12,1,0,0,0,15,16,5,64,0,0,16,19,3,5,2,0,17,18,5,46,0,0,18,
        20,3,5,2,0,19,17,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,
        0,22,2,1,0,0,0,23,25,7,0,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,
        0,0,0,26,27,1,0,0,0,27,4,1,0,0,0,28,30,7,1,0,0,29,28,1,0,0,0,30,
        31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,6,1,0,0,0,5,0,12,21,26,
        31,0
    ]

class emailLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMAIL = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "EMAIL" ]

    ruleNames = [ "EMAIL", "LOCAL_SUBPART", "DOMAIN_SUBPART" ]

    grammarFileName = "email.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


