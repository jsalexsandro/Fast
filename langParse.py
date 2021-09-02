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

    def AddNewScope(self,c,type):
        global SCOPE
        try:
            if not c in SCOPE["GLOBAL"][c]:
                SCOPE["GLOBAL"][c] = [type]
            # pass
        except:
            SCOPE["GLOBAL"][c] = [type]
    
    def setImport(self,c):
        global imports
        if (not c in imports):
            imports.add(c)

    def setAutomaticCodeImport(self,c,t,ii,set,type=""):
        if c == ii and t == TT_DEFINATION:
            self.setNewCode(set)
            self.AddNewScope(ii,type)

    def setCodeImports(self,v):
        global imports_code
        if (not v in imports_code):
            imports_code.add(v)


    def addCodeImports(self,value,token):
        self.setAutomaticCodeImport(value["value"],token,"print",print_fast,"string")
        self.setAutomaticCodeImport(value["value"],token,"input",input_fast,"string")
        # self.setAutomaticCodeImport(value["value"],token,"sendException",types_fast)
        self.setAutomaticCodeImport(value["value"],token,"type",types_fast,"string")
        self.setAutomaticCodeImport(value["value"],token,"stringToInt",types_fast,"string")
        self.setAutomaticCodeImport(value["value"],token,"system",system_fast,"int")
          
    def returnValues(self,vv):
        self.veriFy = True
        self.plotError = ""
        self.state = ''    
        for _cc_,_vv_ in enumerate(SCOPE["GLOBAL"]):
            if vv["value"] == _vv_:
                self.veriFy = False
                self.state = SCOPE["GLOBAL"][_vv_][0]
                # print(SCOPE["GLOBAL"][_vv_][0])
                self.plotError = "TRAVADO"
                break

        if self.veriFy == True:
            for _cc_,_vv_ in enumerate(SCOPE["NOGLOBAL"][self.nameScope[-1]]):
                if vv["value"] == _vv_[0]: 
                    self.plotError = "TRAVADO"
                    self.state = _vv_[1]
                    # print(_vv_)
                    break
        

    def Analitys(self): 
        global EXECUTE,ERROS,ENTRY_POINT_DEFINED,SCOPE,imports,class_,terch_code_append
        self.nameScope = []
        self.nameGlobalScope = ""
        self.typeGlobalScope = ""
        self.countScope = -1
        self.lines = 1
        
        for count,value in enumerate(self.tokens):
            isAppend = True
            token = value["type"]

            if self.tokens[count-1]["type"] != TT_TYPE:
                self.addCodeImports(value,token)

            if token == TT_SYMBOL:
                if self.tokens[count]["name"] == "newLine":
                    self.lines += 1
                    isAppend = False
                              
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
                    self.veriFy = False
                    # print(SCOPE["GLOBAL"])
                    if value["value"] == "":
                        self.veriFy = not self.veriFy
                        plotMsg = "TRAVADO"
                        
                    for i in SCOPE["GLOBAL"]:
                        if i == value["value"]:
                            # print(">>>",SCOPE["GLOBAL"][i])
                            self.veriFy = not self.veriFy
                            plotMsg = "TRAVADO"
                            break
                        else:
                            continue

                    if self.veriFy == False:
                        for i in SCOPE["NOGLOBAL"]:
                            for cc,vv in enumerate(SCOPE["NOGLOBAL"][i]):
                                # print(SCOPE["NOGLOBAL"][i][cc][0])
                                if value["value"] == SCOPE["NOGLOBAL"][i][cc][0]:
                                    # print(SCOPE["NOGLOBAL"][i][cc])
                                    # print("SIM")
                                    plotMsg = "TRAVADO"
                                    # break
                                #     break
                                else:
                                    if plotMsg == "":
                                        plotMsg = "DESTRAVADO"
                    if plotMsg != "TRAVADO":
                        EXECUTE = PrintException("NameError",value["value"],value["value"],self.file,self.lines)
                    # print(plotMsg)

            if token == TT_SYMBOL:
                if value["value"] == '}':
                    try:
                        del SCOPE["NOGLOBAL"][self.nameScope[-1]]
                        del self.nameScope[-1]
                        self.nameGlobalScope = ""
                        self.typeGlobalScope = ""
                    except:pass


            if value["value"] == "return" and token == TT_KEYWORD:
                for cc,vv in enumerate(self.tokens[count+1:]):
                    if vv["name"] == "newLine" and vv["type"] == TT_SYMBOL:
                        continue

                    elif vv["type"] == TT_DEFINATION:
                        self.returnValues(vv)                                
                        if self.plotError == "TRAVADO":
                            if self.state != self.typeGlobalScope:
                                print(self.state)
                                EXECUTE = PrintException("ReturnError","return",vv["value"],self.file,self.lines)
                        else:
                            self.addCodeImports(vv,vv["type"])
                            self.returnValues(vv)                                
                            if self.plotError == "TRAVADO":
                                if self.state != self.typeGlobalScope:
                                    EXECUTE = PrintException("ReturnError","return",vv["value"],self.file,self.lines)
                        break

                    elif vv["type"] in {TT_NUMBER,TT_STRING,TT_BOOL} or vv["type"] == TT_SYMBOL and vv["name"] in {'singleQuote','doubleQuote'}:
                        if self.typeGlobalScope in {"int","float"}:
                            if (vv["type"] != TT_NUMBER):
                                EXECUTE = PrintException("ReturnError","return",vv["value"],self.file,self.lines)
                                break

                        if self.typeGlobalScope == "string":
                            if (vv["type"] not in {TT_STRING,TT_SYMBOL}):
                                EXECUTE = PrintException("ReturnError","return",vv["value"],self.file,self.lines)                     
                                break

                        if self.typeGlobalScope == "bool":
                            if (vv["type"] != TT_BOOL):
                                EXECUTE = PrintException("ReturnError","return",vv["value"],self.file,self.lines)
                                break
                            
                    elif vv["value"] == "}" and vv["type"] == TT_SYMBOL:
                        break

                    else:
                        pass

            if value["value"] == "=" and token == TT_SYMBOL:
                isContinue = True
                for i in self.tokens[count+1:]:     
                    if i["type"] == TT_SYMBOL and i["name"] == "newLine":
                        continue

                    if i["value"] in {"=","<"}:
                        isContinue = False
                        break
                   
                if isContinue == False:
                    pass
                else:
                    for cc,vv in enumerate(self.tokens[count+1:]):
                        if vv["name"] == "newLine":
                            continue
                        elif vv["type"] == TT_DEFINATION:
                            variableName = ""
                            variableAttName = vv["value"]
                            self.attState = ""
                            self.state = ""
                            _count_ = 1
                            while True:
                                if self.tokens[count-_count_]["name"] != "newLine":
                                    if self.tokens[count-_count_]["type"] == TT_DEFINATION:
                                        variableName = self.tokens[count-_count_]["value"] 
                                        # print(variableName)
                                        break
                                _count_ += 1
                            plotMsg = ""
                            self.veriFy = False
                            for i in SCOPE["GLOBAL"]:
                                if variableName == i:
                                    self.state = SCOPE["GLOBAL"][i][0]
                                    plotMsg = "TRAVADO"
                                    break
                                else:
                                    self.veriFy = True
                                    continue
                            if self.veriFy == True:
                                for i in SCOPE["NOGLOBAL"]:
                                    for ii in SCOPE["NOGLOBAL"][i]:
                                        if variableName == ii[0]:
                                            plotMsg = "TRAVADO"
                                            self.state = ii[1]
                                            break  
                                        else:
                                            continue
                            twoplotMsg = ""
                            self.twoVeriFy = False
                            for i in SCOPE["GLOBAL"]:
                                if variableAttName == i:
                                    self.attState = SCOPE["GLOBAL"][i][0]
                                    twoplotMsg = "TRAVADO"
                                    break
                                else:
                                    self.twoVeriFy = True
                                    continue

                            if self.twoVeriFy == True:
                                for i in SCOPE["NOGLOBAL"]:
                                    for ii in SCOPE["NOGLOBAL"][i]:
                                        if variableAttName == ii[0]:
                                            twoplotMsg = "TRAVADO"
                                            self.attState = ii[1]
                                            break  
                                        else:
                                            continue

                            if plotMsg == twoplotMsg:
                                if (self.state != self.attState):
                                    EXECUTE = PrintException("AtributeError",'','',self.file,self.lines)

                            # print(variableName,self.state,plotMsg)
                            # print(variableAttName,self.attState,twoplotMsg)

                        elif vv["type"] in {TT_NUMBER,TT_STRING,TT_BOOL} or vv["type"] == TT_SYMBOL and vv["name"] in {'singleQuote','doubleQuote'}:
                            atualType = vv["type"]
                            variableName = ""
                            self.state = ""
                            _count_ = 1
                            while True:
                                if self.tokens[count-_count_]["name"] != "newLine":
                                    if self.tokens[count-_count_]["type"] == TT_DEFINATION:
                                        variableName = self.tokens[count-_count_]["value"] 
                                        # print(variableName)
                                        break
                                _count_ += 1
                            plotMsg = ""
                            self.veriFy = False
                            for i in SCOPE["GLOBAL"]:
                                if variableName == i:
                                    self.state = SCOPE["GLOBAL"][i][0]
                                    plotMsg = "TRAVADO"
                                    break
                                else:
                                    self.veriFy = True
                                    continue
                            if self.veriFy == True:
                                for i in SCOPE["NOGLOBAL"]:
                                    for ii in SCOPE["NOGLOBAL"][i]:
                                        if variableName == ii[0]:
                                            plotMsg = "TRAVADO"
                                            self.state = ii[1]
                                            break  
                                        else:
                                            continue 

                            if plotMsg == "TRAVADO":
                                if self.state in {"int","float"}:
                                    if (atualType != TT_NUMBER):
                                        EXECUTE = PrintException("AtributeError","","",self.file,self.lines)
                                        break

                                if self.state == "string":
                                    if (atualType not in {TT_STRING,TT_SYMBOL}):
                                        EXECUTE = PrintException("AtributeError","","",self.file,self.lines)
                                        break

                                if self.state == "bool":
                                    if (atualType != TT_BOOL):
                                        EXECUTE = PrintException("AtributeError","","",self.file,self.lines)
                                        break
                                break
        
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
                # self.nameScope.append("constructor")
                
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
                alertExp = self.tokens[count+1]
                if (alertExp["type"] != TT_DEFINATION):
                    # AQUI ENTRA UM EX
                    for cc,vv in enumerate(self.tokens[count+2:]):
                        if vv["type"] == TT_SYMBOL and vv["name"] == "newLine":
                            continue
                        else:
                            if (vv["type"] == TT_DEFINATION):
                                name_ = vv["value"]
                                break
                            else:
                                # print("ISSO É UM ERROR",vv["value"])
                                EXECUTE = PrintException("SyntaxError",type_name_,alertExp["value"],self.file,self.lines)
                                break
                else:
                    name_ = alertExp["value"]


                for cc,vv in enumerate(self.tokens[count+2:]):
                    alertExp = vv
                    # print(alertExp["value"])
                    if (alertExp["value"]) == "=":
                        is_variable_or_function = "variable"
                        break
                    
                    if (alertExp["value"]) == "(":
                        is_variable_or_function = "function"
                        break

                    if (alertExp["value"]) == ",":
                        is_variable_or_function = "variable"
                        break

                    if (alertExp["value"]) == ")":
                        is_variable_or_function = "variable"
                        break

                    is_variable_or_function = "not-detected"
                    continue    # break

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

                # print(is_variable_or_function)
                if name_ == "main":
                    name_ = "__main__"

                if is_variable_or_function == "function":
                    if len(SCOPE["NOGLOBAL"]) == 0:
                        try:
                            affterScope = SCOPE["GLOBAL"][name_][0]
                            if affterScope == type_name_:
                                SCOPE["GLOBAL"][name_] = [type_name_]
                                self.nameGlobalScope = name_
                                self.typeGlobalScope = type_name_
                            else:
                                EXECUTE = PrintException("RedefinationError",f"{type_name_}|{affterScope}",name_,self.file,self.lines)
                            # print(SCOPE["GLOBAL"][name_])

                        except:
                            SCOPE["GLOBAL"][name_] = [type_name_]
                            self.nameGlobalScope = name_
                            self.typeGlobalScope = type_name_
                        
                    SCOPE["NOGLOBAL"][name_] = []
                    self.nameScope.append(name_)

                # print(name_)
                # print(SCOPE["NOGLOBAL"][self.nameScope[-1]])
                SCOPE["NOGLOBAL"][self.nameScope[-1]].append([name_,type_name_])
                
                #############################################################
                # AGEITA O SISTEMA DE DETECÇÂO POIS NÃO ESTA 100% FUNCIONAL #
                #############################################################

            if isAppend == True:
                self.lang.append([self.tokens[count]["type"],self.tokens[count]["value"]])


    def Get(self):
        # print(scope)
        # print(SCOPE)
        return [EXECUTE,ENTRY_POINT_DEFINED,self.lang,imports,class_,terch_code_append,imports_code]