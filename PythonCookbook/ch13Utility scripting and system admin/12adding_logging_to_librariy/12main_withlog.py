import i12somelib
import logging

def main():
    print('in 12main')
    logging.basicConfig(filename='app.log')
    i12somelib.func()


if __name__ == "__main__":
    main()