import sys


def write(file_path: str, text: str):
    with open(file_path, 'w') as file:
        file.write(text+'\n')
    return


def read(file_path: str) -> str:
    with open(file_path, 'r') as file:
        print(file.read())


if __name__ == "__main__":
    write(sys.argv[1], sys.argv[2])
    read(sys.argv[1])

#  python3 task1.py file.txt 'Hello world!'

