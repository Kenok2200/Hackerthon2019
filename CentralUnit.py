import logging.Logger


class CentralUnit:

    def log(message, level):
        print(level + ": " + message)
        logging(message, level)

    def main(self):
        print("start")

    if __name__ == '__main__':
        main()
