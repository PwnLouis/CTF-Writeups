from pathlib import Path
from pprint import pprint

here: Path = Path('chall/Security')

flag: str = ''

p = Path(here).glob('**/readme_*.txt')
files = [x for x in p if x.is_file()]

for txt_file in files:
    with txt_file.open('r') as f:
        flag += f.read().rstrip()

print(flag)