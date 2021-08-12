########################################
# Excptions for "Fast" Language !      #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

1
def PrintExecption(type,ins,value="",file=""):
    if type == "ModuleNotFoundError":
         print(f'ModuleNotFoundError in {ins} - "{value}" module not found\nFile: {file} \n')
         return False

    if type == "RecursiveImportError":
         print(f'RecursiveImportError in "{ins} {value}" cannot import the same file\nFile: {file} \n')
         return False
    
    if type == "SemiColonError":
         print(f'Error in "{ins}" Expected ";" before "{value}" \nFile: {file} \n')
         return False
