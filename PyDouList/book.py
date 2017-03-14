class DoubanBook:
    def __init__(self, name, author, publish_date, been_read_date):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.been_read_date = been_read_date
        self.readen_order = -1
        # to indicate whether match file at local
        self.matched_file = False
        self.category = ''

    def set_readen_order(self, readen_order):
        self.readen_order = readen_order
        
    def set_category(self, category):
        self.category = category

    def set_matched_file(self):
        self.matched_file = True

    def displayDoubanBook(self):
        print(  '\nreaden_order:',str(self.readen_order),
                '\nname:', self.name,
                '\nauthor:', self.author,
                '\npublish_date:',self.publish_date,    
                '\nbeen_read_date:',self.been_read_date,          
                '\ncategory:', self.category,
                '\nmatched_file:',self.matched_file 
               )