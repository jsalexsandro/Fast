########################################
# Lexer and Parser connector.          #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

from cTranspiler import Transpiler

class Interpreter:
    def __init__(self,file:str) -> None:
        self.fastCode = ""
        self.file = file
        with open(file,"rt",encoding="utf-8") as f:
            self.fastCode = f.read()
            self.fastCode = self.fastCode.replace("    ","\t")
            Transpiler(self.fastCode+"",self.file)
        # lexer = Lexer(self.fastCode+";")
        # tokens = lexer.Tokenize()
        # parser = Parser(tokens).Get()
        # Transpiler(parser[0],self.file,parser[1],parser[2],parser[3])