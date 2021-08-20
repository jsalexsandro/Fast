###########################################
# The Parse for "Fast" Language !         #
###########################################
# Coding By José Alexsandro               #
# Github: https://github.com/jsalexsandro #
###########################################

def resetSpaces(v:str):
    return v.replace("    ","\t")

from excp import PrintException
import os
import cTranspiler
from variables import GetFinalExtension
from langLexer import (
    TT_BOOL,
    TT_COMENT,
    TT_KEYWORD,
    TT_NUMBER,
    TT_OPERATOR,
    TT_STRING,
    symbols,
    TT_DEFINATION,
    TT_SYMBOL,
    TT_TYPE,
    keyFors
)

from libs import (
print_fast,
input_fast,
types_fast,
system_fast
)

import sys

SCOPE_APPEND = []
ENTRY_POINT_DEFINED = False
EXECUTE = True
fileMain = ""

imports = {
    "<iostream>",
    "<locale.h>"
}
terch_code_append =set()
imports_code = set()
class_ = []
SCOPE = {
    "GLOBAL":{},
    "NOGLOBAL":{

    }
}
SCOPE_NAMES = [
    
]

class Parser:
    def __init__(self,tokens = [],file="") -> None:
        self.tokens = tokens
        self.lang = []
        self.class_ = ""
        self.file = file
        self.normalFile = GetFinalExtension(file).replace(".fast","")
        self.port_func_run = GetFinalExtension(self.file).replace(".fast","")
        self.Analitys()
        # print(class_)
        # print(SCOPE_APPEND)
        # if EXECUTE == False:
        #     print(ERROS)
        #     sys.exit()

    def setNewCode(self,v):
        global terch_code_append
        for i in v[0]:
            self.setImport(i)
        if not v[1] in terch_code_append:
            terch_code_append.add(v[1])

    def AddNewScope(self,c):
        global SCOPE
        try:
            if not c in SCOPE["GLOBAL"][c]:
                SCOPE["GLOBAL"][c] = []
            # pass
        except:
            SCOPE["GLOBAL"][c] = []
    
    def setImport(self,c):
        global imports
        if (not c in imports):
            imports.add(c)

    def setAutomaticCodeImport(self,c,t,ii,set):
        if c == ii and t == TT_DEFINATION:
            self.setNewCode(set)
            self.AddNewScope(ii)

    def setCodeImports(self,v):
        global imports_code
        if (not v in imports_code):
            imports_code.add(v)


    def Analitys(self): 
        global EXECUTE,ERROS,ENTRY_POINT_DEFINED,SCOPE,imports,class_,terch_code_append
        self.nameScope = []
        self.countScope = -1
        self.lines = 1
        
        for count,value in enumerate(self.tokens):
            isAppend = True
            token = value["type"]
            if token == TT_SYMBOL:
                if self.tokens[count]["name"] == "newLine":
                    self.lines += 1
                    isAppend = False

            self.setAutomaticCodeImport(value["value"],token,"print",print_fast)
            self.setAutomaticCodeImport(value["value"],token,"input",input_fast)
            # self.setAutomaticCodeImport(value["value"],token,"sendException",types_fast)
            self.setAutomaticCodeImport(value["value"],token,"type",types_fast)
            self.setAutomaticCodeImport(value["value"],token,"stringToInt",types_fast)
            self.setAutomaticCodeImport(value["value"],token,"system",system_fast)
          
            if (value["value"] == "import" and token == TT_KEYWORD):
                fileImport = ""
                if (self.tokens[count+1]["type"] == TT_DEFINATION):
                    fileImport = self.tokens[count+1]["value"] + ".fast"
                else:
                    if (self.tokens[count+2]["type"] == TT_DEFINATION):
                        fileImport = self.tokens[count+2]["value"] + ".fast"

                if(os.path.exists(fileImport)):
                    if self.normalFile != str(fileImport).replace(".fast",""):
                        # if self.tokens[count+2]["type"] == TT_SYMBOL and self.tokens[count+2]["value"] == ";":
                        #     pass
                        # else:
                        #     EXECUTE = PrintException("SemiColonError","import",self.tokens[count+1]["value"],self.file)
                        code = cTranspiler.Transpiler(resetSpaces(open(fileImport,"rt").read()),fileImport,True).GetValues()
                        self.setCodeImports(code[0])
                    else:
                        EXECUTE = PrintException("RecursiveImportError",f"import",fileImport,self.file,self.lines)
                else:
                    EXECUTE = PrintException("ModuleNotFoundError",f"import",fileImport,self.file,self.lines)

            if token == TT_DEFINATION:
                if self.tokens[count-1]["type"] == TT_TYPE or self.tokens[count-1]["type"] == TT_KEYWORD and self.tokens[count-1]["value"] in {'class','import'} or self.tokens[count-1]["type"] == TT_DEFINATION and self.tokens[count-1]["value"] in class_:
                    pass
                else:
                    plotMsg = ""
                    if value["value"] not in SCOPE["GLOBAL"]:
                        for i in SCOPE["NOGLOBAL"]:
                            if value["value"] in SCOPE["NOGLOBAL"][i]:
                                plotMsg = "TRAVADO"
                                break
                            else:
                                if plotMsg != "TRAVADO":
                                    EXECUTE = PrintException("NameError",value["value"],value["value"],self.file,self.lines)

            if token == TT_SYMBOL:
                if value["value"] == '}':
                    try:
                        del SCOPE["NOGLOBAL"][self.nameScope[-1]]
                        del self.nameScope[-1]
                    except:pass

            if value["value"] == "class" and token == TT_KEYWORD:
                alertExp = self.tokens[count+1]
                if (alertExp["type"] != TT_DEFINATION):
                    if self.tokens[count+2]["type"] != TT_DEFINATION:
                        EXECUTE = PrintException("SyntaxError","class",alertExp["value"],self.file,self.lines)
                        break

                for cc,vv in enumerate(self.tokens[count+1:]):
                    if vv["type"] == TT_DEFINATION:
                        if vv["value"] == self.port_func_run:
                            ENTRY_POINT_DEFINED = True
                            
                        if vv["value"] == "main":
                            self.tokens[count+cc+1]["value"] = "__main__"

                        self.class_ =  vv["value"]
                        class_.append(vv["value"])
                        break        
                
            if value["value"] == "constructor" and token == TT_KEYWORD:
                self.tokens[count]["value"] = self.class_
                # self.class_ = ""

            if token == TT_TYPE:

                if value["value"] == "string":pass
                    # self.setImport("<string.h>")
                        # imports.add("<string.h>")
                
                if value["value"] == "int":pass

                if value["value"] == "bool":
                    self.setImport("<stdbool.h>")

                if value["value"] == "float":pass
                    # self.tokens[count]["value"] = "double "


                defined = ""
                is_variable_or_function = ""
                name_ = ""
                type_name_ = self.tokens[count]["value"]
                # for cc,vv in enumerate(self.tokens[count+1:]):
                alertExp = self.tokens[count+1]
                if (alertExp["type"] != TT_DEFINATION):
                    # AQUI ENTRA UM EX
                    if self.tokens[count+2]["type"] != TT_DEFINATION:
                        EXECUTE = PrintException("SyntaxError",type_name_,alertExp["value"],self.file,self.lines)
                        break
                    else:
                        # print(self.tokens[count+2]["value"])
                        name_ = self.tokens[count+2]["value"]

                else:
                    name_ = alertExp["value"]

                for cc,vv in enumerate(self.tokens[count+2:]):
                    alertExp = self.tokens[count+2]
                    if (alertExp["value"]) == "(":
                        if is_variable_or_function == "":
                            is_variable_or_function = "function"
                            break

                    elif (alertExp["value"]) == "=":
                        if is_variable_or_function == "":
                            is_variable_or_function = "variable"
                            break

                    elif (alertExp["value"]) == ",":
                            is_variable_or_function = "variable"
                            break
                    else:
                        is_variable_or_function = "not-detected"
                        break

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

                if is_variable_or_function == "function":
                    print(name_)
                    if len(SCOPE["NOGLOBAL"]) == 0:
                        SCOPE["GLOBAL"][name_] = []

                    SCOPE["NOGLOBAL"][name_] = []
                    self.nameScope.append(name_)

                # print(name_)
                SCOPE["NOGLOBAL"][self.nameScope[-1]].append(name_)
                
                #############################################################
                # AGEITA O SISTEMA DE DETECÇÂO POIS NÃO ESTA 100% FUNCIONAL #
                #############################################################


                # except:
                #     print(self.nameScope)
                # print(SCOPE["NOGLOBAL"][self.nameScope[-1]])



            if isAppend == True:
                self.lang.append([self.tokens[count]["type"],self.tokens[count]["value"]])


    def Get(self):
        # print(scope)
        # print(SCOPE)
        return [EXECUTE,ENTRY_POINT_DEFINED,self.lang,imports,class_,terch_code_append,imports_code]