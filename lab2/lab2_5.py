from pathlib import Path
counter = 0
s = input()
top_lvl = Path.cwd().rglob(f'*{s}')
for _ in top_lvl:
    counter +=1
print(counter)