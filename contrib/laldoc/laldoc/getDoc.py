# getDoc.py

'''
Translation and adoption of ADA function from https://github.com/AdaCore/libadalang/blob/master/extensions/src/libadalang-doc_utils.adb
'''

import libadalang as lal

def extract_Doc_From ( Node: lal.AdaNode,
                       Backwards: bool):

    Ret = []  # Return Value

    if Backwards:
        Tok = Node.token_start
    else:
        Tok = Node.token_end

    def Next_Token(Token : lal.Token):
        if Backwards:
            Token = Token.previous
        else: Token = Token.next
        return Token


    # Start of function body
    Tok = Next_Token(Tok)

    while Tok.is_trivia and not Tok.text.startswith("\n\n"):
        line = Tok.text.strip()

        if line != "" and line.startswith("---"):
            Ret.append(line[3:].strip() + "\n")

        Tok = Next_Token(Tok)

    if Backwards:
        Rev = []
        for item in reversed(Ret):
            Rev.append(item)
        return Rev

    return Ret









