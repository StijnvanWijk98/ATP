from collections import namedtuple
from enum import Enum

class TokenTypes (Enum):
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    EOF = "EOF"


class Token:
    def __init__(self, type : TokenTypes, value):
        # Type is a of class TokenTypes
        self.type = type
        self.value = value
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return "Token({}, {})".format(self.type.name, str(self.value))

if __name__ == "__main__":
    a = Token(TokenTypes.INTEGER, 4)
    print(a)
