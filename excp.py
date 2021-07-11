def PrintExecption(type,ins,line,value=""):
    if type == 'DefineError':
        return [False,f"DefineError line {line} in '{ins}' - '{value}' value not implicit\n"]
    if type == "ScopeError":
         return [False,f"ScopeError in '{ins}' line {line}\n"]
    if type == "ScopeWasDefinedError":
         return [False,f"ScopeWasDefinedError in '{ins}' line {line}\n"]
   
    return False,""
