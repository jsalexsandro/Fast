########################################
# CPP Tranpiler for "Fast" Language !  #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################


def debug(a="",b=""):
    if b != "":print(a+" : "+b)

import os,sys,shutil
from re import T
import libs
from variables import GetFinalExtension, extForBuild
from langLexer import Lexer, TT_COMENT, TT_DEFINATION, TT_KEYWORD, TT_SYMBOL, TT_TYPE, types,keywords
from langParse import Parser
from msg import generated_code_for_insert


class Transpiler:
    def __init__(self,code,file_,module=False) -> None:
        self.module = module
        lexer = Lexer(code+";")
        tokens = lexer.Tokenize()
        parser = Parser(tokens,file_).Get()
        entryPointExist=parser[0]
        if entryPointExist == False:
            if module == False:
                sys.exit( print("Entry point not defined!"))
        file=file_
        self.values = parser[1]
        impors=parser[2]
        classed=parser[3]
        self.terch_code_apd = parser[4]
        self.code_imports = parser[5]
        self.imports = impors
        self.commands_add = [
            # "/* using namespace std;\n */"
            "char ** argv;\n"
        ]
        self.native_imports = set()
        # self.languagePathBuilds = os.path.join("\ "[0].join([i for i in sys.argv[0].split("\\")[0:-1]]),"run")
        self.languagePathBuilds = os.path.join(os.getcwd(),"run")
        self.languagePathNormal = os.path.join(os.getcwd(),"")
        # self.languagePathBuilds = "C:\\Users\\Alexsandro\\Desktop\\FastLanguage" + "\\run"
        self.file = file
        if not os.path.exists(self.languagePathBuilds):
            os.mkdir(self.languagePathBuilds)
        self.lang = ""
        self.setString = False
        for count,value in enumerate(self.values):
            typ = value[0]
            value = value[1]


            # debug(typ,value)
            # if typ == TT_SYMBOL and value == "\n":
            #     if self.values[count-1][1] not in {";","{","[","("}:
            #         value = ";\n"

            if typ == TT_SYMBOL and value in {'"',"'"} and self.setString == False:
                value = 'std::string("'
                self.setString = True
                    
            if typ == TT_SYMBOL and value in {'"',"'"} and self.setString == True:
                value = '")'
                self.setString = False

                # if self.setString == True:
                #     print("terminou")
                #     value += '")'
                #     self.setString = False

            if typ == TT_SYMBOL and value == "}":
                if self.values[count+1][1] != ";" and self.values[count+1][0] not in [TT_KEYWORD,TT_DEFINATION]:
                    value += ';'
            
            if typ == TT_COMENT:
                value = ""

            if value in types and typ == TT_TYPE:
                if value == "string":
                    value = "std::string"
                if value == "int":
                    value = "long"
                if value == "float":
                    value = "double"
                    
                value += " "
            
            # if value == "." and typ == TT_SYMBOL:
            #     value = "->"

           
            if value == "var" and typ == TT_KEYWORD:
                value = "auto "
                
            if value == "namespace" and typ == TT_KEYWORD:
                value = "namespace "
                
            # if value == "function" and typ == TT_KEYWORD:
            #     value = ""
                
            if value == "while" and typ == TT_KEYWORD:
                value = "while "

            if value == "for" and typ == TT_KEYWORD:
                value = "for "
                

            if value in keywords and typ == TT_KEYWORD:
                if value in {"public","private","protected","extends","static"}:
                    if value == "extends":
                        value = ":public"
                    elif value == "static":
                        value = "static"
                    else:    
                        value += ':'
                value += " " 

            if value in classed and typ == TT_DEFINATION:
                for cc,vv in enumerate(self.values[count+1:]):
                    if self.values[count+cc+1][0] == TT_DEFINATION:
                        value += " * "
                    elif self.values[count+cc+1][1] == "    ":
                        pass
                    else:break
                    # if vv[count+cc][0] == TT_DEFINATION:
                    #     print("SIM")
                value += ""

            if value == "{" and typ == TT_SYMBOL:value = " { "
            if value == "'" and typ == TT_SYMBOL:value = '"'

            self.lang += value

        if self.module == False:
            self.setMainFuncPoint()
            self.setCodeImports()
            self.setNewTrechCode()
            self.setCommands()
            self.setImports()

        if self.module == False:   
            self.lang = generated_code_for_insert.replace("[file]",file) + self.lang

        # self.Build()


    def GetValues(self):
        return [self.lang,self.imports,self.terch_code_apd]

    def setCodeImports(self):
        code = ""
        for i in self.code_imports:
            code += i+"\n"
        self.lang = code + self.lang


    def setMainFuncPoint(self):
        port_func_run = GetFinalExtension(self.file).replace(".fast","")
        if port_func_run == "main":
            port_func_run = "__main__"
        codeMain = [
            "\n\nint main(int _argc,char * _argv[]){\n",
            'setlocale(LC_ALL,"");\n',
            "argv = _argv;\n"
            f"{port_func_run}();\n",
            "return 0;\n",
            "};"
        ]

        for i in codeMain:self.lang += i


    def setCommands(self):
        code = ""
        for i in self.commands_add:
            code += i+"\n"
        self.lang = code + self.lang


    def setNewTrechCode(self):
        code = ""
        for i in self.terch_code_apd:
            code = code + i + "\n"

        self.lang = code + self.lang

    def setImports(self):
        code = ""
        for i in self.imports:
            # if i == '"libs.hpp"':
            #     self.import_('"libs.hpp"')
            #     code = code.replace("#include <iostream>\n","")
            code += "#include "+i+"\n"
        code += "\n"
        self.lang = code + self.lang

    # def import_(self,lib):
    #     global native_imports
    #     if lib == '"libs.hpp"':
    #         local = os.path.join(self.languagePathBuilds,"libs.hpp")
    #         with open(local,"wt+") as l:
    #             l.write(libs.lib.replace("[\\n]","\n"))
    #         self.native_imports.add(local)

    def Build(self):  
        f = GetFinalExtension(self.file.replace(".fast",".cpp"))
        
        self.fileBuild = os.path.join(self.languagePathBuilds,f"{f}")
        self.fileBuild_Name = self.fileBuild.replace(".cpp",extForBuild())
        # self.fileBuild_Name = self.fileBuild.replace(".cpp",".exe")
        fileBuilded = GetFinalExtension(self.fileBuild_Name)
        with open(self.fileBuild,"wt+") as file:
            file.write(self.lang)
        
        os.system("g++ "+self.fileBuild +" -w -O3 -o "+self.fileBuild_Name)
        # fileNormalBuild = os.path.join(self.languagePathNormal,fileBuilded)
        # if os.path.exists(fileNormalBuild):
        #     os.remove(fileNormalBuild)
        # shutil.move(self.fileBuild_Name,self.languagePathNormal)
        os.system(f"{self.fileBuild_Name} {' '.join(sys.argv[2:])}")
        # print(self.fileBuild,self.fileBuild_Name)
        # print(fileBuilded)
            # except:pass
        # if os.path.exists(fileBuilded):
        #     os.remove(fileBuilded)
        # shutil.move(self.fileBuild_Name,"./")
        # print(fileBuilded)
        # self.fileBuild_Name
        # os.system(self.fileBuild_Name)