from colorama import Fore, Back, Style

import time
import threading

class Countdown:

    def __init__(self,n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.deamon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(0.5)

    def __getstate__(self):
        return self.n

    def __setstate__(self,n):
        self.__init__(n)


def main():

    import pickle

    data = ('a1','b2')
    f = open('521.txt','wb')
    pickle.dump(data, f)

    s = pickle.dumps(data)
    print(s)

    print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    #restore from a file
    f = open('521.txt','rb')
    dataf = pickle.load(f)

    dataS = pickle.loads(s)
    print(dataf,dataS)

    print(Fore.BLUE + "demo3:" + Style.RESET_ALL)
    c = Countdown(5)
    f = open('cstate.p','wb')
    import pickle
    pickle.dump(c, f)
    f.close()

    time.sleep(3)

    print('-'*20)
    f = open('cstate.p','rb')
    pickle.load(f)

            
if __name__ == '__main__':
    main()