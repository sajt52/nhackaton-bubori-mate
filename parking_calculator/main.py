from pathlib import Path
import datetime

INGYENES_PARKOLASPERCEK_MAX = 30
KEDVEZMENYES_ORADIJ_MAX = 3
PERCDIJ = 500//60
NAPIDIJ = 10000
ORADIJ = 500
KEDVEZMENYES = 300

def ParkoloSzamolas(lista):
    with open("output.txt","w") as f:
        f.write("RENDSZAM\tParkolasIdo(ora:perc)\tDij(HUF)\n")
        
        for parkolas in lista:
            dij = 0
            eltelt_ido = parkolas[2] - parkolas[1]
            ora = eltelt_ido.total_seconds() // 3600
            percek = (eltelt_ido.total_seconds() % 3600) //60
            
            if eltelt_ido.total_seconds() <= 0:
                dij = 0
            elif eltelt_ido.days > 0:
                dij += eltelt_ido.days * NAPIDIJ
                dij += ora * ORADIJ
                dij += percek * PERCDIJ
            else:
                if ora > 3:
                    dij += (ora-3)*ORADIJ + 3*KEDVEZMENYES
                else:
                    dij += ora*KEDVEZMENYES
                if percek > 30:
                    dij += (percek-30)*PERCDIJ

            f.write(f"{parkolas[0]} \t{int(ora):02d}:{int(percek):02d}\t \t \t \t\t{int(dij)} HUF\n")
            
    

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    #print(data, end="")
    parkolasok = []
    adatok = data.splitlines()
    for i in range(len(adatok)):
        if i < 2:
            continue
        auto = adatok[i].split("\t\t")

        rendszam = auto[0].strip()
        erkezes = datetime.datetime.strptime(auto[1].strip(),"%Y-%m-%d %H:%M:%S")
        tavozas = datetime.datetime.strptime(auto[2].strip(),"%Y-%m-%d %H:%M:%S")

        parkolas = [rendszam,erkezes,tavozas]
        parkolasok.append(parkolas)
    ParkoloSzamolas(parkolasok)



if __name__ == "__main__":
    main()
