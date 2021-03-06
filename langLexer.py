###########################################
# The Lexer for "Fast" Language !         #
###########################################
# Coding By José Alexsandro               #
# Github: https://github.com/jsalexsandro #
###########################################

import re

TT_NUMBER = "NUMBER"
TT_STRING = "STRING"
TT_COMENT = "COMENT"
TT_BOOL = "BOOL"
TT_KEYWORD = "KEYWORD"
TT_TYPE = "TYPE"
TT_SYMBOL = "SYMBOL"
TT_DEFINATION = "DEFINATION"
TT_OPERATOR = "OPERATOR"
TT_CPP = "CPP_CODE"

stringInit = 0
stringInitedQuote = ""
coment_init = 0
float_init = 0
cpp_count = 0

keyFors = [
    "else",
    "catch"
]

keywords = [
    "const","return","if","else","namespace","switch",
    "case","new","class","extends","constructor","static","public","private","protected",
    "namespace","var","while","for","break","continue","import",
    "try","catch"
]

bolleans = ["true","false"]

operators = ['+','-','%','/','*','**','<','>']

types = [
    "int",
    "string",
    "float",
    "bool",
    "void"
    # "null",
    # "undefined",
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
    '_':'underline',
    ";":"outherPoint"
}


def AppendToken(type,key,value):
    return {"type":type,"name":key,"value":value}

class Lexer:
    def __init__(self,code:str) -> None:
        self.codeSplitedKeys = [i for i in re.split("(\W)",code) if not i == ""]
        self.tokens = []


    def Tokenize(self):
        global stringInit,stringInitedQuote,coment_init,float_init,cpp_count
        for count,value in enumerate(self.codeSplitedKeys):
            if value == "`" and coment_init == 0 and float_init == 0 and cpp_count == 0:
                self.tokens.append(AppendToken(TT_CPP,"","`"))
                cpp_count += 1
            
            elif value == "`" and coment_init == 0 and float_init == 0 and cpp_count == 1:
                self.tokens.append(AppendToken(TT_CPP,"","`"))
                cpp_count = 0

            elif value == "/" and self.codeSplitedKeys[count+1] == "*" and coment_init == 0 and cpp_count == 0:
                self.codeSplitedKeys[count] = ""
                self.codeSplitedKeys[count+1] = ""
                float_init = 1

            elif value == "*" and self.codeSplitedKeys[count+1] == "/" and float_init == 1 and cpp_count == 0:
                self.codeSplitedKeys[count] = ""
                self.codeSplitedKeys[count+1] = ""
                # self.tokens.append(AppendToken(TT_SYMBOL,symbols[" "],""))
                float_init = 0

            elif value == "/" and self.codeSplitedKeys[count+1] == "/" and float_init == 0 and cpp_count == 0:
                self.codeSplitedKeys[count] = ""
                self.codeSplitedKeys[count+1] = ""
                coment_init = 1
        
            elif value == "\n" and coment_init == 1 and float_init == 0 and cpp_count == 0:
                self.tokens.append(AppendToken(TT_SYMBOL,symbols["\n"],""))
                # self.codeSplitedKeys[count] = ""
                coment_init = 0

            elif re.match("[0-9]",value) and coment_init == 0 and float_init == 0 and cpp_count == 0:
                # Set String
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_NUMBER,""+value,""+value))
            
            elif value in keywords and coment_init == 0 and float_init == 0 and cpp_count == 0:
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_KEYWORD,value,value))
            
            elif value in types and coment_init == 0 and float_init == 0 and cpp_count == 0:
                # Set String
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_TYPE,value,value))

            elif value in symbols and coment_init == 0 and float_init == 0 and cpp_count == 0:
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
                        if symbols[value] != "space" and symbols[value] != symbols["\n"]:
                            if value == "\n":
                                self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],""))
                            else:
                                self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],value))

                else:
                    if symbols[value] != "space" and symbols[value] != symbols["\t"]:
                        if value == "\n":
                            self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],""))
                        else:
                            self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],value))

            elif value in bolleans and coment_init == 0 and float_init == 0 and cpp_count == 0:
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_BOOL,value,value))
            
            elif value in operators and coment_init == 0 and float_init == 0 and cpp_count == 0:
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                else:
                    self.tokens.append(AppendToken(TT_OPERATOR,value,value))
            else:

                # Set String
                if stringInit % 2 != 0:
                    self.tokens.append(AppendToken(TT_STRING,value,value))
                elif coment_init == 1:
                    self.tokens.append(AppendToken(TT_COMENT,value,value))
                elif float_init == 1:
                    if value == "\n":
                        # print("IMS")
                        self.tokens.append(AppendToken(TT_SYMBOL,symbols[value],""))
                    else:
                        self.tokens.append(AppendToken(TT_COMENT,value,value))
                elif cpp_count == 1:
                        self.tokens.append(AppendToken(TT_CPP,"",value))
                else:
                    self.tokens.append(AppendToken(TT_DEFINATION,value,value))
        return self.tokens
########################################