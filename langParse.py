########################################
# The Parse for "Fast" Language !      #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

from variables import GetFinalExtension
from langLexer import (
    TT_KEYWORD,
    symbols,
    TT_DEFINATION,
    TT_SYMBOL,
    TT_TYPE
)

from libs import (
print_fast,
types_fast
)

SCOPE_APPEND = []
ENTRY_POINT_DEFINED = False
EXECUTE = True
ERROS = ""

imports = {
    "<iostream>",
    "<locale.h>"
}
terch_code_append =set()
class_ = []

import sys
class Parser:
    def __init__(self,tokens = [],file="") -> None:
        self.tokens = tokens
        self.lang = []
        self.class_ = ""
        self.file = file
        self.port_func_run = GetFinalExtension(self.file).replace(".fast","")
        self.Analitys()
        # print(class_)
        # print(SCOPE_APPEND)
        if EXECUTE == False:
            print(ERROS)
            sys.exit()

    def setNewCode(self,v):
        global terch_code_append
        for i in v[0]:
            self.setImport(i)
        if not v[1] in terch_code_append:
            terch_code_append.add(v[1])

    def setImport(self,c):
        global imports
        if (not c in imports):
            imports.add(c)

    def setAutomaticCodeImport(self,c,t,ii,set):
        if c == ii and t == TT_DEFINATION:
            self.setNewCode(set)

    def Analitys(self): 
        global EXECUTE,ERROS,ENTRY_POINT_DEFINED,SCOPE_APPEND,imports,class_,terch_code_append
        lines = 1
        for count,value in enumerate(self.tokens):
            token = value["type"]
            # if token == TT_SYMBOL:
            #     print()
            #     if value["name"] == symbols["\n"]:
            #         if (
            #             self.tokens[count-1]["value"] not in {";","{","[","("}
            #             # and self.tokens[count+1]["name"] != "newLine"
            #         ):
            #             self.tokens[count]["value"] = ";\n"
            #         lines += 1
            #     # elif self.tokens[count-1]["value"] == ")":
            #     #         self.tokens[count]["value"] = ");"
            #     elif value["name"] == symbols["\t"]:
            #         self.tokens[count]["value"] = "    "
            self.setAutomaticCodeImport(value["value"],token,"print",print_fast)
            self.setAutomaticCodeImport(value["value"],token,"type",types_fast)
            # if value["value"] in {"print"} and token == TT_DEFINATION:
            #     self.setNewCode(print_fast)
            #     # print("code_nw")
            #     # pass

            if value["value"] == "class" and token == TT_KEYWORD:
                for cc,vv in enumerate(self.tokens[count+1:]):
                    if vv["type"] == TT_DEFINATION:
                        if vv["value"] == self.port_func_run:
                            ENTRY_POINT_DEFINED = True
                            
                        if vv["value"] == "main":
                            self.tokens[count+cc+1]["value"] = "__main__"

                        self.class_ =  vv["value"]
                        class_.append(vv["value"])
                        break

            # if value["value"] == "function" and token == TT_KEYWORD:
            #     for cc,vv in enumerate(self.tokens[count+1:]):
            #         if vv["type"] == TT_DEFINATION:
            #             if vv["value"] == "main":
            #                 self.tokens[count+cc+1]["value"] = "__main__"
                        
                
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

                if value["value"] == "string":pass
                    # self.tokens[count]["value"] = "char * "
                        # imports.add("<string.h>")
                
                if value["value"] == "int":pass
                    # self.tokens[count]["value"] = "long "
                        # imports.add("<string.h>")

                if value["value"] == "bool":
                    self.setImport("<stdbool.h>")

                if value["value"] == "float":pass
                    # self.tokens[count]["value"] = "double "


                defined = ""
                its = ""
                for cc,vv in enumerate(self.tokens[count+1:]):
                    if self.tokens[count+cc+1]["type"] == TT_DEFINATION:
                        if self.tokens[count+cc+1]["value"] == self.port_func_run:
                            ENTRY_POINT_DEFINED = True

                        if self.tokens[count+cc+1]["value"] == "main":
                            self.tokens[count+cc+1]["value"] = "__main__"
                        
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
        return [ENTRY_POINT_DEFINED,self.lang,imports,class_,terch_code_append]