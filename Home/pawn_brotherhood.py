#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns: set) -> int:
    n = 0
    for x in pawns:
        listX = list(x)
        candid1 = chr(ord(listX[0])+1) + str(int(listX[1])-1)
        candid2 = chr(ord(listX[0])-1) + str(int(listX[1])-1)
        if candid1 in pawns or candid2 in pawns:
            n += 1
    return n

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")