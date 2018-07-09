from termcolor import colored


def post_article(conn, user, title, link):
    print(colored('-'*30, 'red'))
    print('in post_article')