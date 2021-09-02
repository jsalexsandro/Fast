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
    
    if type == "ReturnError":
        print(f'ReturnError in "{ins}" - A function must return a value that matches its type in "return {value}" \nFile: {file}::{line}\n')
        return False

    if type == "AtributeError":
        print(f'AtributeError - You can only assign the variable a value that matches its type. \nFile: {file}::{line}\n')
        return False

    if type == "NameError":
        print(f'NameError - "{value}" has not been defined \nFile: {file}::{line}\n')
        return False

    if type == "RedefinationError":
        print(f'RedefinationError - "{str(ins).split("|")[0]} {value}" to redefine a function or variable, it must have the same type as the first definition ({str(ins).split("|")[1]}). \nFile: {file}::{line}\n')
        return False

    if type == "SyntaxError":
        print(f'SyntaxError in "{ins}" Invalid Syntax, search for language grammar\nFile: {file}::{line}\n')
        return False