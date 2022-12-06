
operators = {
    "+": "ADD",
    "-": "SUB",
    "*": "MUL",
    "/": "DIV",
    "(": "LPAREN",
    ")": "RPAREN"

}

dataTypes = {
    "int": "INT",
    "String": "STRING",
    "real": "REAL",
    "boolean": "BOOLEAN"
}

comparisons = {
    "<": "LESS",
    ">": "GREATER",
    "<=": "LESSEQ",
    ">=": "GREATEREQ",
    "!=": "NOTEQ"
    "==" "ISEQ"
}


SYMBOLS = '+-*/()<>=!;'
DIGITS = '0123456789.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


class Token:
    def __init__(self, _type, value=None) -> None:
        self.type = _type
        self.value = value

    # representation method to return a string with the token's value and type
    def __repr__(self) -> str:
        return f"{self.type}:{self.value}"



def lex(line):
    tok = []
    lineSplit = line.split(" ")
    print(lineSplit)
    for i in lineSplit:
        if(i in operators):
            tok.append(Token("OPERATOR",operators[i]))
        elif(i in dataTypes):
            tok.append(Token("DATATYPE",dataTypes[i]))
        elif(i in comparisons):
            tok.append(Token("COMPARISON",comparisons[i]))
        elif(i == ";"):
            tok.append(Token("SEMICOLON",i))
        elif(i == "="):
            tok.append(Token("ASSIGN",i))
        elif(i.isdigit()):
            tok.append(Token("INTEGER", i))
        elif(i[0].isdigit()):
            dot = i.count(".")
            num = True
            for j in i:
                if(j in DIGITS):
                    continue
                elif(j in LETTERS or j in SYMBOLS):
                    num = False
                else:
                    print(j + " is an invalid token")
                    exit(1)

            if(dot > 0 and num == True):
                tok.append(Token("REAL", i))
            else:
                tok.append(Token("IDENTIFIER",i))
        else:
            for j in i:
                if j not in DIGITS and j not in LETTERS and j not in SYMBOLS:
                    print(j + " is an invalid token")
                    exit(1)

            tok.append(Token("IDENTIFIER",i))


    return tok




print('5'.isdigit())
line = 'int x = 10.5'
tokenList = lex(line)
print(tokenList)