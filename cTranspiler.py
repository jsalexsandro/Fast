import os
import shutil
import sys
import libs
from variables import GetFinalExtension
from langLexer import TT_DEFINATION, TT_KEYWORD, TT_SYMBOL, TT_TYPE, types,keywords

imports = [
    "<stdio.h>",
    "<locale.h>"
]
native_imports = set()

class Transpiler:
    def __init__(self,mainExist=False,file="",values = "",impors=[],classed=[]) -> None:
        self.languagePathBuilds = os.getcwd() + "\\run"
        # self.languagePathBuilds = "C:\\Users\\Alexsandro\\Desktop\\FastLanguage" + "\\run"
        self.file = file
        if not os.path.exists(self.languagePathBuilds):
            os.mkdir(self.languagePathBuilds)
        for i in impors:
            imports.append(i)
        self.lang = ""
        for count,value in enumerate(values):
            typ = value[0]
            value = value[1]
            if value in types and typ == TT_TYPE:
                value += " "
            
            if value in keywords and typ == TT_KEYWORD:
                if value in {"public","private","protected"}:
                    value += ':'
                value += " " 

            if value in classed and typ == TT_DEFINATION:
                for cc,vv in enumerate(values[count+1:]):
                    if values[count+cc+1][0] == TT_DEFINATION:
                        value += "*"
                    elif values[count+cc+1][1] == "    ":
                        pass
                    else:break
                    # if vv[count+cc][0] == TT_DEFINATION:
                    #     print("SIM")
                value += " "

            if value == "{" and typ == TT_SYMBOL:value = " { "
            if value == "'" and typ == TT_SYMBOL:value = '"'

            self.lang += value
        
        self.setMainFuncPoint()
        self.setImports()

        self.__Build()
      
    def setMainFuncPoint(self):
        codeMain = [
            "\n\nint main(){\n",
            '    setlocale(LC_ALL,"");\n',
            "    __main__();\n",
            "    return 0;\n",
            "};"
        ]

        for i in codeMain:self.lang += i


    def setImports(self):
        code = ""
        for i in imports:
            if i == '"libs.h"':
                self.import_('"libs.h"')
                code = code.replace("#include <stdio.h>\n","")
            code += "#include "+i+"\n"
        code += "\n"
        self.lang = code + self.lang

    def import_(self,lib):
        global native_imports
        if lib == '"libs.h"':
            local = self.languagePathBuilds+"\\libs.h"
            with open(local,"wt+") as l:
                l.write(libs.lib.replace("[\\n]","\n"))
            native_imports.add(local)

    def __Build(self):  
        f = GetFinalExtension(self.file.replace(".fast",".cpp"))
        self.fileBuild = self.languagePathBuilds + f"\\{f}"
        self.fileBuild_Name = self.fileBuild.replace(".cpp","")
        # self.fileBuild_Name = self.fileBuild.replace(".cpp",".exe")
        fileBuilded = GetFinalExtension(self.fileBuild_Name)
        fileBuilded = GetFinalExtension(self.fileBuild_Name)
        with open(self.fileBuild,"wt+") as file:
            file.write(self.lang)
        
        os.system("g++ "+self.fileBuild +" -w -O3 -o "+self.fileBuild_Name)
            # except:pass
        # if os.path.exists(fileBuilded):
        #     os.remove(fileBuilded)
        # shutil.move(self.fileBuild_Name,"./")
        # os.system(fileBuilded)
        os.system("cd run && "+fileBuilded)