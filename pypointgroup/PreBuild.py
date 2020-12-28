import datetime
import os.path as pt

def new_version():

    path = pt.join(pt.dirname(__file__), 'Version.py')
    DATE = str(datetime.date.today())
    VERSION = "1.0.0"

    with open(path, 'rt') as f:
        for line in f.readlines():
            if line.startswith("VERSION"):
                VERSION = line[10:].strip().strip('"')

    a,b,c = VERSION.split('.')

    c = str(int(c)+1)

    print(f'Old version: {VERSION}')

    VERSION = f"{a}.{b}.{c}"

    print(f'New version: {VERSION}')
    print(f'Current date: {DATE}')

    with open(path, 'wt', encoding='utf8') as f:
        f.write(f"VERSION = \"{VERSION}\"\n")
        f.write(f"DATE = \"{DATE}\"\n")

    return VERSION, DATE

def new_conda(VERSION, DATE):

    path = pt.dirname(__file__)
    path, _ = pt.split(path)
    path = pt.join(path,'conda', 'meta.yaml')

    with open(path,'rt',encoding='utf8') as f:
        meta = [line for line in f.readlines()]

    for i,line in enumerate(meta):
        if line.startswith('  version:'):
            meta[i] = f"  version: {VERSION}\n"

    with open(path, 'wt', encoding='utf8') as f:
        f.writelines(meta)

    print("Creted ", path)

def main():
    VERSION, DATE = new_version()
    new_conda(VERSION, DATE)

if __name__ == '__main__':
    main()