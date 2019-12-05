def log(message, level):
    print(level + ": " + message)
    log(message, level)


def main():
    print("start")


if __name__ == '__main__':
    main()
