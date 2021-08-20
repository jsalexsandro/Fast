###########################################
# Tokens user View  for Fast Language     #
###########################################
# Coding By José Alexsandro               #
# Github: https://github.com/jsalexsandro #
###########################################


import langLexer

def PlotTokens(code):
    lexer = langLexer.Lexer(code+";").Tokenize()
    for i in lexer:
        if i["value"] not in {""," "}:
            if i["name"] == i["value"]:
                i["name"] = "NAME_UNDEFINED"
            print(f"""TYPE: {i["type"]} | NAME: {i["name"]} | VALUE: {i["value"]}""")
