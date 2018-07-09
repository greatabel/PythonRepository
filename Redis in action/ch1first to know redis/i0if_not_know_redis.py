from datetime import datetime, timedelta
import calendar, time
from random import randint
# https://stackoverflow.com/questions/5067218/get-utc-timestamp-in-python-with-datetime

articleid_time = {}
articleid_score = {}
articleid_users = {}

def generate_articleid_time():
    # 随机一个id
    articleid = 100635
    dnow = datetime.now()

    for i in range(0, 5):
        articleid += i
        dnow = dnow + timedelta(hours=i)
        local = calendar.timegm(dnow.utctimetuple())
        articleid_time[articleid] = local
    print(articleid_time)

def generate_articleid_score():
    for k,v in articleid_time.items():
        articleid_score[k] = v + 432 * randint(0, 100)
    print(articleid_score)

def generate_articleid_users():
    for k,v in articleid_time.items():
        users = []
        for i in range(0, randint(0,5)):
            users.append(randint(10000,11000))
        articleid_users[k] = users
    print(articleid_users)

def main():
    generate_articleid_time()
    generate_articleid_score()
    generate_articleid_users()

if __name__ == "__main__":
    main()


