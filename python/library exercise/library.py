class library():
    def __init__(self):
        self.nobooks = 0
        self.books = []
        
    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)
        
    def showinfo(self):
        print(f"The Library has {self.nobooks}.\nThe Books are as follows :")
        for i in self.books:
            print(i)
           
b1=library() 
b1.addbook("THE BOYS")

b1.addbook("BREAKING BAD")

b1.addbook("THE PUNISHER")
        
b1.showinfo()