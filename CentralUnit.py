class CentralUnit:

    def __init__(self):
        self.receiver = 1
        self.sender = 2

    def log(message, level):
        print(level + ": " + message)


def main():
    print("start")
    f = CentralUnit()
    print(f.sender)


if __name__ == '__main__':
    main()
