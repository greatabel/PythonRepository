# import pymongo
#http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.definitions
    return db

def add_country(db):
    db.words.insert({"word" : "oarlock","definition":"A device 1234"})
    db.words.insert({"word" : "seminomadic","definition":"namadic"})
    db.words.insert({"word" : "test","definition":"test1"})
    
def get_country(db):
    return db.words.find_one({"word": 'oarlock'})

if __name__ == "__main__":

    db = get_db() 
    add_country(db)
    print('get=',get_country(db))