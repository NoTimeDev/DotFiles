from enum import Enum, auto

class TokenKind(Enum):
    Add = auto()
    Add_Assingnment = auto()
    Inc = auto()

    Sub = auto()
    Sub_Assingnment = auto()
    Dec = auto()

    Mul = auto()
    Mul_Assingnment = auto()
    
    Exponent = auto()
    Exponent_Assignment = auto()

    Div = auto()
    Div_Assignment = auto()

    Mod = auto()
    Mod_Assignment = auto()

    Less_Than = auto()
    Less_Than_oeqt = auto()

    Greater_Than = auto()
    Greater_Than_oeqt = auto()
    
    Equal = auto()
    Equality = auto()
    Not_eq = auto()
    
    Bit_Not = auto()
    
    Bit_Xor = auto()
    Bit_Xor_Assignment = auto()

    LShift = auto()
    RShift = auto()
    
    LShift_Assignmet = auto()
    RShift_Assignment = auto()

    Log_Not = auto()
    
    Bit_Or = auto()
    Log_Or = auto()
    Bit_Or_Assigment = auto()

    Bit_And = auto()
    Log_And = auto()
    Bit_And_Assingment = auto()
    
    Comma = auto()
    Colon = auto()
    DColon = auto()
    Walrus = auto()
    
    DArrow = auto()

    Dot = auto()
    SArrow = auto()
    Tenary = auto()

    Open_Brack = auto()
    Close_Brack = auto()

    Curly_Open_Brack = auto()
    Curly_Close_Brack = auto()
    
    Square_Open_Brack = auto()
    Square_Close_Brack = auto()
    
    Type = auto()

    Func = auto()
    Struct = auto()
    Interface = auto() 
    Union = auto()
    Impl = auto()
    Const = auto()
    Static = auto()
    Mut = auto()
    ENUM = auto()
    Pub = auto()
    Priv = auto()


    Pre_If = auto()
    Pre_End = auto()
    Pre_Else = auto()
    Pre_Elif = auto()
    Pre_Define = auto()

    In = auto()
    Return = auto()
    New = auto()
    Del = auto()
    As = auto()
    Module = auto()
    Import = auto()
    Asm = auto()
    Extern = auto()
    From = auto()
    Def = auto()
    Defer = auto()

    If = auto()
    Elif = auto()
    Else = auto()
    For = auto()
    While = auto()
    Break = auto()
    Continue = auto()
    Match = auto()

    Int = auto()
    Float = auto()
    String = auto()
    Char = auto()
    Identifier = auto()
    EOF = auto()
  
    Semi = auto()
    Null = auto()
    Let = auto()

    Comment = auto()

class Token:
    def __init__(self, Kind: TokenKind, Value: str, Start: int, End: int, Line: int):
        self.Kind: TokenKind = Kind
        self.Value: str = Value
        self.Start: int = Start
        self.End: int = End
        self.Line: int = Line

    def __repr__(self) -> str:
        return "{" + f'"Kind" : {self.Kind}, "Value" : "{self.Value}", "Line" : {self.Line}, "Start" : {self.Start}, "End" : {self.End}' + "}"

NullToken: Token = Token(TokenKind.Null, "Null", 0, 0, 0)


class Lexer:
    def __init__(self, SourceCode: str):
        self.FileName: str = ""
        self.SourceCode: str = SourceCode
        self.SourceLines: list[str] = SourceCode.split('\n')
        
        self.Alphas: dict[str, TokenKind] = {
            "func":TokenKind.Func,
            "struct": TokenKind.Struct,
            "union" : TokenKind.Union,
            "impl" : TokenKind.Impl,
            "interface" : TokenKind.Interface,

            "for" : TokenKind.For,
            "while" : TokenKind.While,

            "const" : TokenKind.Const,
            "mut" : TokenKind.Mut,
            "static" : TokenKind.Static,
            "let" : TokenKind.Let,

            "if" : TokenKind.If,
            "elif" : TokenKind.Elif,
            "else" : TokenKind.Else,

            "match" : TokenKind.Match,
            "break" : TokenKind.Break,
            "continue" : TokenKind.Continue,

            "char" : TokenKind.Type,
            "i28" : TokenKind.Type,
            "i64" : TokenKind.Type,
            "i32" : TokenKind.Type,
            "i16" : TokenKind.Type,
            "i8" : TokenKind.Type,

            "ui28" : TokenKind.Type,
            "u64" : TokenKind.Type,
            "u32" : TokenKind.Type,
            "u16" : TokenKind.Type,
            "u8" : TokenKind.Type,

            "Self" : TokenKind.Type,
            "String" : TokenKind.Type,

            "enum" : TokenKind.ENUM,
            "pub" : TokenKind.Pub,
            "priv" : TokenKind.Priv,
            "new" : TokenKind.New,
            "del" : TokenKind.Del,
            "as" : TokenKind.As,
            "mod" : TokenKind.Module,
            "import" : TokenKind.Import,
            "asm" : TokenKind.Asm,
            "return" : TokenKind.Return,
            "in" : TokenKind.In,
            "extern" : TokenKind.Extern,
            "from" : TokenKind.From,
            "defer" : TokenKind.Defer,
            "def" : TokenKind.Def
        }

    def Lex(self) -> list[Token]:
        Tokens: list[Token] = []

        def Add(Token):
            Tokens.append(Token)
            
        Pos: int = 0
        Coloum: int = 0 
        Line: int = 0 
        
        def Peek(num: int=1):
            return self.SourceCode[Pos + 1 + num - 1: Pos + 1 + num]
        
        while Pos < len(self.SourceCode):
            match self.SourceCode[Pos]:
                case ' ' | '\t':
                    Pos+=1; Coloum+=1
                case '\n':
                    Line+=1
                    Coloum = 0 
                    Pos+=1

                case '+':
                    if Peek() == "+":
                        Add(Token(TokenKind.Inc, "++", Coloum, Coloum + 2, Line)) 
                        Coloum+=2; Pos+=2
                    elif Peek() == "=":
                        Add(Token(TokenKind.Add_Assingnment, '+=', Coloum, Coloum + 2, Line))
                        Coloum+=2; Pos+=2
                    else:
                        Add(Token(TokenKind.Add, "+", Coloum, Coloum + 1, Line))
                        Coloum+=1; Pos+=1
                case '-':
                    if Peek() == '-':
                        Add(Token(TokenKind.Dec, '--', Coloum, Coloum + 2, Line))
                        Coloum+=2; Pos+=2;
                    elif Peek() == '=':
                        Add(Token(TokenKind.Sub_Assingnment, '-=', Coloum, Coloum + 2, Line))
                        Coloum+=2; Pos+=2
                    elif Peek() == ">":
                        Add(Token(TokenKind.SArrow, "->", Coloum, Coloum + 2, Line))
                        Coloum+=2; Pos+=2
                    else:
                        Add(Token(TokenKind.Sub, "-", Coloum, Coloum + 1, Line))
                        Coloum+=1; Pos+=1
                case "*":
                    if Peek() == '*':
                        if Peek(2) == '=':
                            Add(Token(TokenKind.Exponent_Assignment, "**=", Coloum, Coloum + 3, Line))
                            Coloum+=3; Pos+=3
                        else:
                            (Peek(2))
                            Add(Token(TokenKind.Exponent, "**", Coloum, Coloum + 2, Line))
                            Coloum+=2; Pos+=2
                    elif Peek() == '=':
                        Add(Token(TokenKind.Mul_Assingnment, "*=", Coloum, Coloum + 2, Line))
                        Coloum+=2; Pos+=2
                    else:
                        Add(Token(TokenKind.Mul, "*", Coloum, Coloum + 1, Line))
                        Coloum+=1; Pos+=1 
                case '/':
                    if Peek() == '/':
                        Start = Coloum
                        Pos+=2
                        Coloum+=2

                        while self.SourceCode[Pos] != '\n':
                            Pos+=1
                            Coloum+=1
                        
                        (self.SourceCode[Pos])
                        Pos-=1
                        Coloum-=1
                        (self.SourceCode[Pos])
                        Add(Token(TokenKind.Comment, "", Start, Coloum + 1, Line))
                    elif Peek() == "*":
                        Start = Coloum
                        Pos+=2
                        Coloum+=2
                        
                        while self.SourceCode[Pos] != '*' and Peek(2) != '/':
                            if self.SourceCode[Pos] == '\n':
                                Add(Token(TokenKind.Comment, "", Start, Coloum, Line))
                                Line+=1 
                                Start = 0 
                                Coloum = 0 
                            Pos+=1 
                            Coloum+=1

                        if self.SourceCode[Pos] == '\n':
                            Line+=1
                            Coloum = 1
                        Pos+=3
                        Coloum+=2 
                        (self.SourceCode[Pos])
                        Add(Token(TokenKind.Comment, "", Start, Coloum, Line))
                    elif Peek() == "=":
                        Add(Token(TokenKind.Div_Assignment, "/=", Coloum, Coloum + 2, Line))
                        Pos+=2 
                        Coloum+=2
                    else:
                        Add(Token(TokenKind.Div, '/', Coloum, Coloum + 1, Line))
                        Pos+=1
                        Coloum+=1
                case '%':
                    if Peek() == "=":
                        Add(Token(TokenKind.Mod_Assignment, '%=', Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Mod, '%', Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '=':
                    if Peek() == "=":
                        Add(Token(TokenKind.Equality, "==", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    elif Peek() == ">":
                        Add(Token(TokenKind.DArrow, "=>", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Equal, "=", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '!':
                    if Peek() == '=':
                        Add(Token(TokenKind.Not_eq, "!=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Log_Not, '!', Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '<':
                    if Peek() == "<":
                        if Peek(2) == "=":
                            Add(Token(TokenKind.LShift_Assignmet, "<<=", Coloum, Coloum + 3, Line))
                            Pos+=3; Coloum+=3
                        
                        else:
                            Add(Token(TokenKind.LShift, "<<", Coloum, Coloum + 2, Line))
                            Pos+=2; Coloum+=2
                    elif Peek() == "=":
                        Add(Token(TokenKind.Less_Than_oeqt, "<=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else: 
                        Add(Token(TokenKind.Less_Than, "<", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '>':
                    if Peek() == ">":
                        if Peek(2) == "=":
                            Add(Token(TokenKind.RShift_Assignment   , ">>=", Coloum, Coloum + 3, Line))
                            Pos+=3; Coloum+=3
                        
                        else:
                            Add(Token(TokenKind.RShift, ">>", Coloum, Coloum + 2, Line))
                            Pos+=2; Coloum+=2
                    elif Peek() == "=":
                        Add(Token(TokenKind.Greater_Than_oeqt, ">=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else: 
                        Add(Token(TokenKind.Greater_Than, ">", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '&':
                    if Peek() == "=":
                        Add(Token(TokenKind.Bit_And_Assingment, "&=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    elif Peek() == "&":
                        Add(Token(TokenKind.Log_And, "&&", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Bit_And, "&", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '|':
                    if Peek() == "|":
                        Add(Token(TokenKind.Log_Or, "||", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    elif Peek() == "=":
                        Add(Token(TokenKind.Bit_Or_Assigment, "|=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Bit_Or, "|", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '^':
                    if Peek() == "=":
                        Add(Token(TokenKind.Bit_Xor_Assignment, "^=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Bit_Xor, "^", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case '~':
                    Add(Token(TokenKind.Bit_Not, "~", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1
                case ".":
                    Add(Token(TokenKind.Dot, ".", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1
                case ":":
                    if Peek() == ":":
                        Add(Token(TokenKind.DColon, "::", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    elif Peek() == "=":
                        Add(Token(TokenKind.Walrus, ":=", Coloum, Coloum + 2, Line))
                        Pos+=2; Coloum+=2
                    else:
                        Add(Token(TokenKind.Colon, ":", Coloum, Coloum + 1, Line))
                        Pos+=1; Coloum+=1
                case ",":
                    Add(Token(TokenKind.Comma, ",", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1
                case "(":
                    Add(Token(TokenKind.Open_Brack, "(", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1 
                case ")":
                    Add(Token(TokenKind.Close_Brack, ")", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1 
                case "{":
                    Add(Token(TokenKind.Curly_Open_Brack, "{", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1
                case "}":
                    Add(Token(TokenKind.Curly_Close_Brack, "}", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1  
                case "[":
                    Add(Token(TokenKind.Square_Open_Brack, "[", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1
                case "]":
                    Add(Token(TokenKind.Square_Close_Brack, "]", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1
                case ";":
                    Add(Token(TokenKind.Semi, ";", Coloum, Coloum + 1, Line))
                    Pos+=1; Coloum+=1 
                case "#":
                    Predefines: dict[str, TokenKind] = {
                        "#define" : TokenKind.Pre_Define,
                        "#if" : TokenKind.Pre_If,
                        "#elif" : TokenKind.Pre_Elif,
                        "#else" : TokenKind.Pre_Else,
                        "#end" : TokenKind.Pre_End
                    }

                    PreDef: str = "#" 
                    Start: int = Coloum
                    Pos+=1; Coloum+=1
                    while self.SourceCode[Pos].isalpha():
                            PreDef+=self.SourceCode[Pos]

                            Pos+=1; Coloum+=1
                    
                    
                    if Predefines.get(PreDef) != None:
                        Add(Token(Predefines[PreDef], PreDef, Start, Coloum, Line))
                    else:
                        pass 
                case _:
                    if self.SourceCode[Pos].isdigit():
                        NUMBERLIST = '0123456789abcdefABCDEF_.Xx'
                        NUMBERHEXLIST = "abcdefxABCDEFX"
                        Number: str = ""
                        DotCount: int = 0
                        Start: int = Coloum
                        Dots = []

                        while self.SourceCode[Pos] in NUMBERLIST:
                            if self.SourceCode[Pos] != '_':
                                if self.SourceCode[Pos] == '.':
                                    DotCount+=1
                                    Dots.append(Coloum)

                                Number+=self.SourceCode[Pos]
                            Pos+=1; Coloum+=1

                        if DotCount >= 1:
                            if DotCount > 1:
                                pass
                            else:
                                try:
                                    float(Number)
                                except ValueError:
                                    pass
                            Add(Token(TokenKind.Float, Number, Start, Coloum, Line))
                        else: 
                            if Number.lower().startswith('0x'):
                                Number = str(int(Number, 16))

                            ishex = False
                            for i in Number:
                                if i in NUMBERHEXLIST:
                                    ishex = True

                            if ishex == True:
                                pass 
                            Add(Token(TokenKind.Int, Number, Start, Coloum, Line))
                    elif self.SourceCode[Pos].isalpha() or self.SourceCode[Pos] == '_':
                        Start: int = Coloum
                        Alpha: str = ""
                        while self.SourceCode[Pos].isalnum() or self.SourceCode[Pos] == '_':
                            Alpha+=self.SourceCode[Pos]

                            Pos+=1; Coloum+=1
                        
                        if self.Alphas.get(Alpha) != None:
                            Add(Token(self.Alphas[Alpha], Alpha, Start, Coloum, Line))            
                        else:
                            Add(Token(TokenKind.Identifier, Alpha, Start, Coloum, Line))
                    elif self.SourceCode[Pos] == '"':
                        Start: int = Coloum
                        String: str = "\""
                        Got_Unterminated: bool = False
                        Pos+=1; Coloum+=1
                        while True:
                            if String[-1] != '\\' and self.SourceCode[Pos] == '"':
                                break
                            if self.SourceCode[Pos] == '\n':
                                Got_Unterminated = True
                                break
                                 
                            String+=self.SourceCode[Pos]
                            Pos+=1; Coloum+=1
                        
                        if Got_Unterminated == False:
                            Pos+=1; Coloum+=1
                        
                        Add(Token(TokenKind.String, String + '"', Start, Coloum, Line))
                    elif self.SourceCode[Pos] == "'":
                        Start: int = Coloum
                        Character: str = "'"
                        Got_Unterminated: bool = False
                        Pos+=1; Coloum+=1
                        while True:
                            if Character[-1] != '\\' and self.SourceCode[Pos] == "'":
                                break
                            elif self.SourceCode[Pos] == '\n':

                                Got_Unterminated = True
                                break

                            Character+=self.SourceCode[Pos]
                            Pos+=1; Coloum+=1
                        
                        if Got_Unterminated == False:
                            Pos+=1; Coloum+=1

                        if Got_Unterminated == False:
                            if len(Character) > 2:
                                if len(Character) != 1 and Character[1] != "\\":
                                    pass 
                        Add(Token(TokenKind.Char, Character + "'", Start, Coloum, Line))
                    else:
                        Pos+=1; Coloum+=1                                    
            
        

        
        return Tokens 

if __name__ == "__main__":
    import sys
    print("Applying Hightlight") 
    with open(sys.argv[1]) as File:
        Code = File.read()
        
    with open("/home/devvy/.config/nvim/lua/Zed/ZedLight.txt", 'w') as File:
        File.write("")     
    Code+='\n'        
    LexerClass: Lexer = Lexer(Code)
    LexedTokens = LexerClass.Lex()
    
    NextBracket = "YellowBrack"
    NextBracketList = []

    Pos = 0
    def Add(Line: int, Start: int, End: int, HighLight: str):
        with open("/home/devvy/.config/nvim/lua/Zed/ZedLight.txt", 'a') as File:
            File.write(str(Line) + '\n')
            File.write(str(Start) + '\n')
            File.write(str(End) + '\n')
            File.write(HighLight + '\n')
                 
    VarNameList = []

    def Peek(num):
        try:
            LexedTokens[Pos + num]
        except IndexError:
            return NullToken
        else:
            return LexedTokens[Pos + num]

    while Pos < len(LexedTokens):
        CToken = LexedTokens[Pos]
        
        print(CToken)

        if CToken.Kind in [TokenKind.Int, TokenKind.Float]:
            Add(CToken.Line, CToken.Start, CToken.End, "ZedNumber") # type: ignore
        elif CToken.Kind in [TokenKind.Comment]:
            Add(CToken.Line, CToken.Start, CToken.End, "ZedComment")
        elif CToken.Kind == TokenKind.Import:
            Add(CToken.Line, CToken.Start, CToken.End, "ZedKeyword")

            if Peek(1).Kind == TokenKind.Less_Than:
                Add(Peek(1).Line, Peek(1).Start, Peek(1).End, "ZedString")
                Add(Peek(2).Line, Peek(2).Start, Peek(2).End, "ZedString")
                Add(Peek(3).Line, Peek(3).Start, Peek(3).End, "ZedString")

                Pos+=3 
        
        elif CToken.Kind in [TokenKind.String, TokenKind.Char]:
            String = CToken.Value
            StrStart = CToken.Start

            mPos = 1
            Start = 0 
            while mPos  < len(String) - 1:
                if String[mPos] == "\\":
                    print("Fuck")
                    Add(CToken.Line, Start + StrStart, mPos + StrStart, "ZedString")
                    Add(CToken.Line, mPos + StrStart, mPos + 2 + StrStart, "SlashCode")
                    mPos+=1
                    Start = mPos + 1 
                mPos+=1 
            Add(CToken.Line, StrStart + Start, CToken.End, "ZedString")
        elif CToken.Kind in [TokenKind.Let, TokenKind.Mut]:
            Add(CToken.Line, CToken.Start, CToken.End, "ZedLet")
            
            Pos+=1 

            while LexedTokens[Pos].Kind == TokenKind.Identifier: 
                VarNameList.append(LexedTokens[Pos].Value)
                CToken = LexedTokens[Pos]
                Add(CToken.Line, CToken.Start, CToken.End, "ZedVar")
                Pos+=1 
                if LexedTokens[Pos].Kind == TokenKind.Comma:
                    Pos+=1 
               
        elif CToken.Kind  == TokenKind.Identifier:
            if CToken.Value in VarNameList:
                Add(CToken.Line, CToken.Start, CToken.End, "ZedVar")
        elif CToken.Kind == TokenKind.Type:
            Add(CToken.Line, CToken.Start, CToken.End, "ZedType")
        elif CToken.Kind in [TokenKind.Open_Brack, TokenKind.Curly_Open_Brack, TokenKind.Square_Open_Brack]:
            if len(NextBracketList) == 0:
                NextBracket = "YellowBrack"
            NextBracketList.append(NextBracket)

            Add(CToken.Line, CToken.Start, CToken.End, NextBracket)
            
            if len(NextBracketList) != 0:
                if NextBracket == "YellowBrack":
                    NextBracket = "PurpleBrack"
                else:
                    NextBracket = "YellowBrack" 
            
                
        elif CToken.Kind in [TokenKind.Close_Brack, TokenKind.Square_Close_Brack, TokenKind.Curly_Close_Brack]:
            Add(CToken.Line, CToken.Start, CToken.End, NextBracketList.pop())
        Pos+=1
