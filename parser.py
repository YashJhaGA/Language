class Token:
    def __init__(self, _type, value=None) -> None:
        self.type = _type
        self.value = value

    # representation method to return a string with the token's value and type
    def __repr__(self) -> str:
        return f"{self.type}:{self.value}"



class parser:

    def __init__(self, listOfTokens):
        self.listOfTokens = listOfTokens
        self.index = 0


    def printTokens(self):
        print(self.listOfTokens)


    def isThereANextToken(self):
        try:
            self.listOfTokens[self.index+1]
            return True
        except:
            return False

    def getNextToken(self):
        if(self.isThereANextToken()):
            self.index += 1
            return self.listOfTokens[self.index]
        else:
            return "NONE"

    def startParse(self):
        while(self.index < len(self.listOfTokens)):
            currentToken = self.listOfTokens[self.index]
            if(currentToken.type == 'DATATYPE'):
                self.declaration(currentToken)



    def validateIdentifier(self,currentToken):
        for i in currentToken.value:
            if(i.isalpha()):
                pass
            else:
                return False
        return True


    def declaration(self,currentToken):

        declareType = currentToken.value

        currentToken = self.getNextToken()
        if (currentToken == 'NONE'):
            print("Missing tokens necessary for declaration")
            exit(1)
        elif (currentToken.type != 'IDENTIFIER'):
            print("Expected Token Type of IDENTIFIER and instead received " + currentToken.type)
            exit(1)
        else:
            if(self.validateIdentifier(currentToken)):
                pass
            else:
                print("Variable Identifier has wrong naming convention")
                exit(1)

        currentToken = self.getNextToken()

        if(currentToken == 'NONE'):
            exit(1)
        elif(currentToken.type == 'SEMICOLON'):
            return
        elif(currentToken.type == 'ASSIGN'):
            self.initializePicker(declareType)
        else:
            print("Expected Token of Semicolon or Assign. Instead received "+currentToken.type)


    def initializePicker(self,declareType):
        if(declareType == 'INT'):
            self.makeInt()
        elif(declareType == 'STRING'):
            self.makeString()
        elif(declareType == 'REAL'):
            self.makeReal()
        else:
            self.makeBoolean()


    def makeInt(self):
        currentToken = self.getNextToken()

        # If Token is a 'INTEGER', increment.
        # If Token is a 'OPERATOR', decrement.
        # If this value is something other than 0 or 1, throw error.
        expresionBalance = 0

        if(currentToken == 'NONE'):
            print("Missing necessary tokens")
        elif(currentToken.type == 'INTEGER'):
            expresionBalance += 1
            pass
        else:
            print("Expected token of INTEGER. Instead received "+currentToken.type)
            exit(1)


        currentToken = self.getNextToken()

        if(currentToken == 'NONE'):
            print("Missing Semicolon")
            exit(1)
        elif(currentToken.type == 'SEMICOLON'):
            pass
        elif(currentToken.type != 'OPERATOR'):
            print("Expected Operator. Instead received "+currentToken.type)
            exit(1)
        else:
            while(currentToken.type != 'SEMICOLON'):

                if(currentToken.type == 'INTEGER'):
                    expresionBalance += 1
                elif(currentToken.type == 'OPERATOR'):
                    expresionBalance -= 1
                else:
                    print(currentToken.type)
                    print('Invalid Token for initializing Integer')
                    exit(1)

                if(expresionBalance < 0 or expresionBalance > 1):
                    print("Expression is unbalanced. You can't have 2 consecutive numbers or operators")
                    exit(1)

                currentToken = self.getNextToken()
                if (currentToken == 'NONE'):
                    print('Missing tokens to initialize')
                    exit(1)


        if(expresionBalance != 1):
            print("Invalid Syntax for Integer Initialization.")
