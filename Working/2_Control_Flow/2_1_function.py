'''
-------------------------------------------------------------------------------
Name:		cigar_party.py
Purpose:	to determine if the squirrel party is a cigar party

Author:	Zhuang.J

Created:	date in 22/03/2019
------------------------------------------------------------------------------
'''


def cigar_party(cigars, is_weekend):
    if (40 <= cigars and cigars >= 60) and not (is_weekend):
        print("True")
    elif 40 <= cigars and is_weekend:
        print("True")
    else:
        print("False")

def main():
    cigar_party(30, False)

main()