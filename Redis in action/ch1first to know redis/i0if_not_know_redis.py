from datetime import datetime, timedelta
import calendar, time

# https://stackoverflow.com/questions/5067218/get-utc-timestamp-in-python-with-datetime

articleid_time = {}

def main():
    # 随机一个id
    articleid = 100635
    dnow = datetime.now()
    
    # print('local=', local)
    # print('@', time.gmtime(local))
    for i in range(0, 5):
        articleid += i
        dnow = dnow + timedelta(hours=i)
        local = calendar.timegm(dnow.utctimetuple())
        articleid_time[articleid] = local

        # d0 = dnow + timedelta(hours=-1)
        # d1 = dnow + timedelta(hours=1)
        # print(dnow, '#', d0, d1)
    print(articleid_time)

if __name__ == "__main__":
    main()


