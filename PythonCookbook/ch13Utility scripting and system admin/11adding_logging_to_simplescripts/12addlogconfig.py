import logging
import logging.config

def main():
    logging.config.fileConfig('12logconfig.ini')
    hostname = 'www.test.org'
    item = 'spam'
    filename = "data.csv"
    mode = 'r'

    logging.critical('#host %s unkonw', hostname)
    logging.error("#Couldn't find %r",item)
    logging.warning('#Feature is deprecated')
    logging.info('#Opening file %r, mode=%r', filename, mode)
    logging.debug('#Got here')


if __name__ == "__main__":
    main()