import time

import requests


def main():
    while True:
        time.sleep(5)
        requests.post(
            "http://127.0.0.1:8080/signal",
            data=None,
            json=None

        )


if __name__ == '__main__':
    main()
