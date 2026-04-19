from pathlib import Path

def magic_number(n):
    
    
    if "^" in n:
        szamok = n.split("^")
        szam = str(int(szamok[0])**int(szamok[1]))
        lentgh = len(szam)
    else:
        szam = n
        lentgh = len(szam)

    kozep = (lentgh + 1) // 2 
    
    nagyobb = 0
    szamreferenc = int(szam)

    while nagyobb != 1:
        
        baloldalszam = int(szam[:kozep])+1
        baloldal = str(baloldalszam)
        
        palindromaszam = int(palindrom(baloldal,lentgh))
        palindroma = str(palindromaszam)

        nagyobb = nagyobbE(palindromaszam,szamreferenc)
        if len(palindroma) > lentgh:
            print("1" + ("0" * (lentgh-1)) + "1")
            return
    
    print(palindromaszam)
    return

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    # print(data, end="")
    for sor in data.strip().splitlines():
        magic_number(sor)


def palindrom(szamstr, n):
    if n % 2 == 0:
        return szamstr + szamstr[::-1]
    else:
        return szamstr + szamstr[:-1][::-1]

def nagyobbE(keresett, referencia):
    if keresett > referencia:
        return 1
    if keresett < referencia:
        return -1
    if keresett == referencia:
        return 0

if __name__ == "__main__":
    main()
