########################################
# The Parse for "Fast" Language !      #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

def resetSpaces(v:str):
    return v.replace("    ","\t")

from excp import PrintExecption
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
SCOPE = []
scope = []
typeScope = []
isScope = []
blockCommandCount = 0

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
        if not c in SCOPE:
            SCOPE.append(c)

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
        global scope,isScope,typeScope,blockCommandCount
        # lines = 0
        # countString = 0
        self.scopeName = ""
        
        for count,value in enumerate(self.tokens):
            isAppend = True
            token = value["type"]
            if token == TT_SYMBOL:
                if self.tokens[count]["name"] == "newLine":
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
                        #     EXECUTE = PrintExecption("SemiColonError","import",self.tokens[count+1]["value"],self.file)
                        code = cTranspiler.Transpiler(resetSpaces(open(fileImport,"rt").read()),fileImport,True).GetValues()
                        self.setCodeImports(code[0])
                    else:
                        EXECUTE = PrintExecption("RecursiveImportError","import",fileImport,self.file)
                else:
                    EXECUTE = PrintExecption("ModuleNotFoundError",f"import",fileImport,self.file)
                    # for i in code[1]:
                    #     if i in imports:pass
                    #     else:
                    #         print(i)
                    #         imports.add(i)
                    # Interpreter(fileImport).Build()
                # Interpreter()

            if token == TT_DEFINATION:
                if self.tokens[count-1]["type"] == TT_TYPE or self.tokens[count-1]["type"] == TT_KEYWORD and self.tokens[count-1]["value"] in {'class','import'} or self.tokens[count-1]["type"] == TT_DEFINATION and self.tokens[count-1]["value"] in class_:
                    pass
                else:
                    if value["value"] not in scope:
                        if not value["value"] in SCOPE:
                            # print(f"{value['value']} not Defined")
                            EXECUTE = PrintExecption("NameError",value["value"],value["value"],self.file)
                        # print(self.typeScope[scope.index(value["value"])])
                        # print(se)
                        # pass
                        # print(value["value"])

            if token == TT_SYMBOL:
                if (value["value"] == "{"):
                    blockCommandCount += 1
                if (value["value"] == "}"):
                    if blockCommandCount == 1:
                        scope.clear()
                        typeScope.clear()
                        isScope.clear()
                        self.scopeName = ""
                        blockCommandCount = 0
                    else:
                        blockCommandCount -= 1
                    # print(self.tokens[count+1]["value"],self.tokens[count+1]["type"],self.tokens[count+1]["name"])

            if value["value"] == "class" and token == TT_KEYWORD:
                alertExp = self.tokens[count+1]
                if (alertExp["type"] != TT_DEFINATION):
                    if self.tokens[count+2]["type"] != TT_DEFINATION:
                        EXECUTE = PrintExecption("SyntaxError","class",alertExp["value"],self.file)
                        break

                for cc,vv in enumerate(self.tokens[count+1:]):
                    if vv["type"] == TT_DEFINATION:
                        if vv["value"] == self.port_func_run:
                            ENTRY_POINT_DEFINED = True
                            
                        if vv["value"] == "main":
                            self.tokens[count+cc+1]["value"] = "__main__"

                        self.class_ =  vv["value"]
                        class_.append(vv["value"])
                        scope.append(vv["value"])
                        typeScope.append("class")
                        isScope.append("class")
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
                        EXECUTE = PrintExecption("SyntaxError",type_name_,alertExp["value"],self.file)
                        break
                    else:
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
                    if self.scopeName == "":
                        self.scopeName = name_        
                        SCOPE.append(name_)
            
                if self.scopeName != "":
                    scope.append(name_)
                    typeScope.append(type_name_)
                    isScope.append(is_variable_or_function)
                # print(is_variable_or_function+":"+name_,type_name_)
            if isAppend == True:
                self.lang.append([self.tokens[count]["type"],self.tokens[count]["value"]])


    def Get(self):
        # print(scope)
        return [EXECUTE,ENTRY_POINT_DEFINED,self.lang,imports,class_,terch_code_append,imports_code]