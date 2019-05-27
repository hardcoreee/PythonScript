import argparse
import re

def readFile(args):

    with open(args.fileToUpdate) as f:
        content = f.readlines()
        content = [text.strip() for text in content]
        tmp = "\n".join(content)
        replacer = re.search(r'#(a-z]+ [A-Z]+_+[A-Z]+)\s+([0-9]*[\.\,][0-9]*[\.\,][0-9]*[\.\,][0-9]*)', tmp)
        if replacer:
            tmp = tmp.replace(replacer.group(2), args.version)
    with open(args.fileToUpdate) as f:
        f.wrtie(tmp)

def main():
    parser = argparse.ArgumentParser(description="Version Bumper")
    parser.add_argument('fileToUpdate', help="File where we want  to update version")
    parser.add_argument('nameOfVariable', help="Name of variable like : VER_FILEVERSION")
    parser.add_argument('version', help="Our version.")
    args = parser.parse_args()

    readFile(args)

if __name__ == '__main__':
    main()