class DoubanBook:
    def __init__(self, name, author, publish_date, been_read_date):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.been_read_date = been_read_date
        self.readen_order = -1

    def set_readen_order(self, readen_order):
        self.readen_order = readen_order

    def displayDoubanBook(self):
          print("Name :", '#'+self.name+'#',  ", author:", '#'+self.author+'#',
            ",publish_date:",'#'+self.publish_date
            +'#', ',been_read_date=','#'+self.been_read_date
            ,'readen_order =',str(self.readen_order) )