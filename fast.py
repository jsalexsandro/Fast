###########################################
# The Cli for "Fast" Language !           #
###########################################
# Coding By José Alexsandro               #
# Github: https://github.com/jsalexsandro #
###########################################

import os
from plotTokens import PlotTokens
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
                print("File was exists")
            break
        elif argv in {"-t","--token"}:
            file = variables.GetFinalExtension(ag[argc+1])
            if file.endswith(".fast") and os.path.exists(ag[argc+1]):
                with open(ag[argc+1]) as v:
                    PlotTokens(v.read())
                # interpreter.Interpreter(argv).PlotTokens()
                break
            elif not file.endswith(".fast"):
                print(f"Extension '{'.'+file.split('.')[-1]}' not supported.")
                break
            elif not os.path.exists(argv):
                print(f"File '{ag[argc+1]}' not found.")
                break
            else:
                print("We had an execution problem.")
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