###########################################
# Excptions for "Fast" Language           #
###########################################
# Coding By José Alexsandro               #
# Github: https://github.com/jsalexsandro #
###########################################

def PrintException(type,ins,value="",file="",line=1):
    if type == "ModuleNotFoundError":
        print(f'ModuleNotFoundError in {ins} - "{value}" module not found\nFile: {file}::{line}\n')
        return False

    if type == "RecursiveImportError":
        print(f'RecursiveImportError in "{ins} {value}" cannot import the same file\nFile: {file}::{line}\n\n')
        return False
    
    if type == "SemiColonError":
        print(f'Error in "{ins}" Expected ";" before "{value}" \nFile: {file}::{line}\n')
        return False

    if type == "NameError":
        print(f'NameError - "{value}" has not been defined \nFile: {file}::{line}\n')
        return False

    if type == "SyntaxError":
        print(f'SyntaxError in "{ins}" Invalid Syntax, search for language grammar\nFile: {file}::{line}\n')
        return False