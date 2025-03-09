import re, os
if os.name == 'nt':
    os.system('cls')
else:
    os.system("clear")
BONDCOST = [0, 10, 40, 200, 750, 4000, 15000, 60000, 270000, 450000, 1200000, 2000000, 4000000, 7000000, 15000000, 120000000, 450000000, 1900000000, 7500000000, 15000000000, 475000000000, 4500000000000, 95000000000000, 5000000000000000, 95000000000000000]
SLOT = min(50, max(1, int(re.sub("[^0-9]", '', input("hive slot: ")))))
BONDPERC = min(130, max(100, int(re.sub("[^0-9]", '', input("bond percentage: ")))))
def numbFormat(x):
    if x<1000:
        return str(x)
    a, i = ["", "k", "m", "b", "t", "qd", "qn", "sx"], 0
    while x >= 1000 and i < len(a)-1:
        x /= 1000; i+=1
    return f"{x:.2f}{a[i]}"
print(f"{'Level':<5} - {'Honey Per Bee':<15} - {f'Honey Total (x{SLOT})':<15} - {f'Bond ({BONDPERC})':<5}")
print("-"*45)
for lvl in range(1, 26):
    costBee = ((10*BONDCOST[lvl-1])/BONDPERC)*10000
    print(f"{lvl:<5} - {numbFormat(costBee):<15} - {numbFormat(costBee*SLOT):<15}")
