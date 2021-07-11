########################################
# The Parse for "Fast" Language !      #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

from os import pipe
from typing import no_type_check
from excp import PrintExecption
from langLexer import (
    TT_KEYWORD,
    symbols,
    TT_DEFINATION,
    TT_SYMBOL,
    TT_TYPE
)

SCOPE_APPEND = []

MAIN_FUNCTION_DEFINED = False
EXECUTE = True
ERROS = ""

imports = set()
class_ = []

import sys
class Parser:
    def __init__(self,tokens = []) -> None:
        self.tokens = tokens
        self.lang = []
        self.class_ = ""
        self.Analitys()
        # print(class_)
        # print(SCOPE_APPEND)
        if EXECUTE == False:
            print(ERROS)
            sys.exit()

    def Analitys(self): 
        global EXECUTE,ERROS,MAIN_FUNCTION_DEFINED,SCOPE_APPEND,imports,class_
        lines = 1
        for count,value in enumerate(self.tokens):
            token = value["type"]
            if token == TT_SYMBOL:
                if value["name"] == symbols["\n"]:
                    if self.tokens[count-1]["value"] not in {"{","[","("}:
                        self.tokens[count]["value"] = ";\n"
                    lines += 1
                # elif self.tokens[count-1]["value"] == ")":
                #         self.tokens[count]["value"] = ");"
                elif value["name"] == symbols["\t"]:
                    self.tokens[count]["value"] = "    "
                
            if value["value"] == "print" and token == TT_DEFINATION:
                if not '"libs.h"' in imports:
                    imports.add('"libs.h"')

            if value["value"] == "class" and token == TT_KEYWORD:
                for cc,vv in enumerate(self.tokens[count+1:]):
                    if vv["type"] == TT_DEFINATION:
                        self.class_ =  vv["value"]
                        class_.append(vv["value"])
                        break
                
            if value["value"] == "constructor" and token == TT_KEYWORD:
                self.tokens[count]["value"] = self.class_
                # self.class_ = ""

            if token == TT_TYPE:
                # extern = False
                # # cExtern = 0
                # for cc,vv in enumerate(self.tokens[count+1:]):
                #     c = 1
                #     if self.tokens[cc+count-c]["type"] == TT_KEYWORD:
                #         if (self.tokens[cc+count-c]["value"] == "extern"):
                #             extern = True
                #             # cExtern = cc+count-c
                #             break

                if value["value"] == "string":
                    self.tokens[count]["value"] = "char * "

                if value["value"] == "bool":
                    if not "<stdbool.h>" in imports:
                        imports.add("<stdbool.h>")

                if value["value"] == "float":
                    self.tokens[count]["value"] = "double "


                defined = ""
                its = ""
                for cc,vv in enumerate(self.tokens[count+1:]):
                    if self.tokens[count+cc+1]["type"] == TT_DEFINATION:
                        if self.tokens[count+cc+1]["value"] == "main":
                            self.tokens[count+cc+1]["value"] = "__main__"
                            MAIN_FUNCTION_DEFINED = True
                        for ccc,vvv in enumerate(self.tokens[count+cc+1:]):
                            if vvv["type"] == TT_DEFINATION:
                                if defined == "" :
                                    defined = [vvv["value"]][0]
                                    break


                    for ccc,vvv in enumerate(self.tokens[count+cc+1:]):
                        if self.tokens[count+cc+1]["value"] == "=":
                            if its == "":
                                its = "variable"
                                break
                        
                        elif self.tokens[count+cc+1]["value"] == "(":
                            if its == "":
                                its = "function"
                                break

                        else:
                            pass

                #testa esse novo sistema de detecção de variaveis e funções
                if its == "variable":
                    pass

                if its == "function":
                    SCOPE_APPEND.append(defined)


            # Fazer o sistema para ssbae se é um função ou variavel
            self.lang.append([self.tokens[count]["type"],self.tokens[count]["value"]])


    def Get(self):
        return [MAIN_FUNCTION_DEFINED,self.lang,imports,class_]