class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)

def main():
    users = [User(1),User(20),User(300),User(2)]
    print(users)
    print(sorted(users, key= lambda u: u.user_id))
    print('alter way:')
    from operator import attrgetter
    print(sorted(users, key = attrgetter("user_id")))

if __name__ == '__main__':
    main()