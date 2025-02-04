import re
HIVE = min(50, max(1, int(re.sub("[^0-9]", '', input("hive slot: ")))))
BOND = min(30, max(0, int(re.sub("[^0-9]", '', input("bond percentage: ")))))
print(f"{'Level':<3} {'Honey Cost':<10} {'Bond Cost':<10} {'Treat Total':<10}")
