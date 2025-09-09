class book:
    book_store="abcd "

    def __init__(self, subject,price):
         self.subject = subject
         self.price = price

    def setsubject(self,nsub):
        self.subject=nsub

    def setprice(self,nprice):
        self.price=nprice

    def getsubject(self):
        return self.subject
    
    def getprice(self):
        return self.price

    @classmethod
    def getbook_store(cls):
        return cls.book_store
        
    
    @staticmethod
    def find_pages(pages):
        print(pages)


b1 =book("math",200)
print(b1.price)

b1.setprice(220)
print(b1.price)

print(b1.getsubject())

book.getbook_store()
b1.find_pages(300)


