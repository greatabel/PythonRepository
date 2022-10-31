import pickle
import time
from datetime import datetime


def hello():


    # --------- share data -------
    fp = open("shared.pkl", "rb")
    shared = pickle.load(fp)
    r = shared["area_rate"]
    current_date_and_time = datetime.now()
    print('Cmd thread ['+ str(current_date_and_time)+ '] is receving green-rate:', str(round(r, 2)) )
    # --------- share data end -------




if __name__ == "__main__":
    while True:
        # every 0.1 seconds
        time.sleep(0.1)
        hello()

