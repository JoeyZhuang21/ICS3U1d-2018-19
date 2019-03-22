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