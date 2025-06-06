# import xml.etree.ElementTree as ET
# tree = ET.parse('Myxml.xml')
# root = tree.getroot()
#
# FontComboBoxTrees = []
#
# for FontComboBox in root.iter('FontComboBox'):
#     FontComboBoxTrees.append(FontComboBox)
#
# print(FontComboBoxTrees)
from antlr4 import *
from gram.gen.XMLLexer import XMLLexer
from gram.gen.XMLParser import XMLParser
from AST import *
import argparse

def getQFontComboBoxList(input_address):
    stream = FileStream(input_address)
    lexer = XMLLexer(stream)
    tokens = lexer.getAllTokens()
    QFONTBOXLIST = []
    i = 0
    while i < len(tokens):
        currentToken = tokens[i]
        # print(currentToken.text)
        if currentToken.text == "QFontComboBox":
            s = "<QFontComboBox "
            i += 1
            currentToken = tokens[i]
            while currentToken.text != "QFontComboBox":
                s += f" {currentToken.text}"
                i += 1
                currentToken = tokens[i]
            s += f" {currentToken.text}>"
            QFONTBOXLIST.append(s)
        i += 1
    return QFONTBOXLIST

def getAstList(QFONTBOXLIST):
    ASTLIST = []
    for QFONTBOX in QFONTBOXLIST:
        istream = InputStream(QFONTBOX)
        lexer = XMLLexer(istream)
        stream = CommonTokenStream(lexer)
        parser = XMLParser(stream)
        parse_tree = parser.document()
        listener = ast_creator()
        walker = ParseTreeWalker()
        walker.walk(listener, parse_tree)
        ASTLIST.append(listener)
        listener.show_tree()
        print(f"root: {listener.root}, attrs: {listener.attrs}")
    return(ASTLIST)

def codeGenerator(ASTLIST):
    imports = "from PyQt5.QtWidgets import *\nfrom PyQt5 import Qttore, OtGui\nfrom PyOt5.OtGui import *\nfrom Pyot5.OtCore import *\nimport sys\n"
    base = "app = QApplication([])\nwindow = QWidget()\nwindow.setWindowTitle(QFONTCOMBOBOX)\n"
    final_out = imports+base
    final_out = get_ast_str(ASTLIST, start_str=final_out, num_of_space=8)
    final_out += "window.setLayout(QFCB)\nwindow.show()\nsys.exit(app.exec())"

    print(final_out)

    with open("final_out.py", "w") as f:
        f.write(final_out)

if __name__ == "__main__":
    QFONTBOXLIST=getQFontComboBoxList("Myxml.xml")
    ASTLIST = getAstList(QFONTBOXLIST)
    final = codeGenerator(ASTLIST)
