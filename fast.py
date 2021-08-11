########################################
# The Cli for "Fast" Language !        #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

import os
import sys
import langhelp
import variables
import interpreter

def Main():
    if len(sys.argv) == 1:
        print(f'For information on using the cli "{variables.langName} --help" or "{variables.langName} -h"')
        sys.exit()    

    ag = sys.argv[1:]
    for argc,argv in enumerate(ag):
        if argv in {"--help","-h"}:
            print(langhelp.RayLangHelp)
            break
        elif argv in {"--version","-v"}:
            print(f"{variables.langName} - version: {variables.langVersion}")
            break
        elif argv in {"-nf","--new-file"}:
            if not os.path.exists(ag[argc+1]):
                with open(ag[argc+1],"wt+"):pass
            else:
                print("Ja existe o arquivo")
            break
        else:   
            file = variables.GetFinalExtension(argv)
            if file.endswith(".fast") and os.path.exists(argv):
                interpreter.Interpreter(argv).Build()
                break
            elif not file.endswith(".fast"):
                print(f"Extension '{'.'+file.split('.')[-1]}' not supported.")
                break
            elif not os.path.exists(argv):
                print(f"File '{argv}' not found.")
                break
            else:
                print("We had an execution problem.")
                break
if __name__ == "__main__":
    Main()