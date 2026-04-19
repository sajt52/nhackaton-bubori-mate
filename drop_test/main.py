from pathlib import Path


def min_number_of_drops(n, h):
    
    dp = [0] * (n+1)
    dobasok = 0

    while dp[n] < h:
        dobasok += 1
        elozo = dp.copy()
        for i in range(1, n+1):
            dp[i] = dp[i] + elozo[i-1] + 1

    print(dobasok)



def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    #print(data, end="")
    for line in data.splitlines():
        prots = line.split(",")[0].strip()
        height = line.split(",")[1].strip()
        min_number_of_drops(int(prots),int(height))

if __name__ == "__main__":
    main()
