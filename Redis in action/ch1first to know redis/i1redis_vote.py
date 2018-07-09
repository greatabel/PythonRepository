import time
from termcolor import colored


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432 


def post_article(conn, user, title, link):
    print(colored('-'*30, 'red'), 'post_article:')

    article_id = str(conn.incr('article:'))
    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
        })

    conn.zadd('score', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)
    return article_id