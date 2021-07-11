########################################
# The Lexer for "Fast" Language !      #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

import re

TT_NUMBER = "NUMBER"
TT_STRING = "STRING"
TT_BOOL = "BOOL"
TT_KEYWORD = "KEYWORD"
TT_TYPE = "TYPE"
TT_SYMBOL = "SYMBOL"
TT_DEFINATION = "DEFINATION"

stringInit = 0
stringInitedQuote = ""

keywords = [
    "const","return","if","else","namespace","switch",
    "case","new","class","constructor","public","private","protected",
    "extern"
]

bolleans = ["true","false"]

operators = ['+','-','%','/','*','**','<','>']

types = [
    "int",
    "string",
    "float",
    "bool",
    "null",
    "undefined",
]

symbols = {
    '.':'dot',
    '=':'equal',
    ':':'beginBlock',
    '(':'lparen',
    ')':'rparen',
    ',':'comma',
    '[':'lbracket',
    ']':'rbracket',
    "'":'singleQuote',
    '"':'doubleQuote',
    '#':'hashtag',
    ' ':'space',
    '\n':'newLine',
    '\t':'tab',
    '!':'exclamation',
    '{':'lbrace',
    '}':'rbrace',
    '>':'greaterThan',
    '<':'lessThan',
    '_':'underline'
}


def AppendToken(type,key,value):
    return {"type":type,"name":key,"value":value}

class Lexer:
    def __init__(self,code:str) -> None:
        self.codeSplitedKeys = [i for i in re.split("(\W)",code) if not i == ""]
        self.tokens = []


    def Tokenize(self):
        global stringInit,stringInitedQuote
        for count,value in enumerate(self.codeSplitedKeys):
            if re.match("[0-9]",value):
                # Set String
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_NUMBER,""+value,""+value))
            
            elif value in keywords:
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_KEYWORD,value,value))
            elif value in types:
                # Set String
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_TYPE,value,value))
            elif value in symbols:
                if symbols[value] in {'singleQuote','doubleQuote'}:
                    if stringInit % 2 == 0:
                        stringInitedQuote = symbols[value]
                        stringInit += 1
                    else:
                        if stringInitedQuote == symbols[value]:
                            stringInit += 1
                            stringInitedQuote = ""
                # Set String
                if stringInit % 2 != 0:
                    if stringInitedQuote != symbols[value]:
                        v = value
                        if value == "\t":value = "    "
                        self.tokens.append(AppendToken(TT_STRING,symbols[v],value))
                    else:
                        self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],value))
                else:
                    if symbols[value] != "space":
                        self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],value))
            
            elif value in bolleans:
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_BOOL,value,value))
            else:

                # Set String
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_DEFINATION,value,value))
        return self.tokens
########################################