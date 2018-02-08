import multiprocessing
import random
import time


class producer(multiprocessing.Process):
    def run(self):
        return ""


class consumer(multiprocessing.Process):
    def run(self):
        return ""

if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_producer = producer(queue)
        process_consumer = consumer(queue)
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        process_consumer.join()