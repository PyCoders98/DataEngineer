
##/////////////////////.......  LIBRARY MANAGEMENT SYSYTEM  ........////////////////////


##/////////////////////.......  LIBRARY MANAGEMENT SYSYTEM  ........////////////////////

def add_data(title,author,book_id):
   # file = open("myfile.txt","a")
   # file.write(f"{title},{author},{book_id},{availability}\n")
   # file.close()
   with open('myfile.txt','a')as file:
     file.write(f'{title},{author},{book_id}\n')
   

def load_file():
   with open('myfile.txt','r')as f1:
      content = f1.read()


class Book:
   def __init__(self, title, author, id):
      self.title = title
      self.author = author
      self.id = id

class Library:
    def __init__(self):
       self.books = []


    def add_books(self, title, author, id):
       bk = Book(title, author, id)
       self.books.append(bk.title)
       print(self.books)


    def available_books(self):
       for book in self.books:
          print(book)


    def borrow_book(self,title):
       if title in self.books:
          print(f'the book {title} is available , you can borrow')
          self.books.remove(title) 
          print(self.books)
       else:
          print('this book is not available')

    def return_books(self, book_retn):
        if book_retn not in self.books:
           print(f'{book_retn} is a borrowed book ')
           print(f'{book_retn} is available now')
        self.books.append(book_retn)
        print(self.books)


obj = Library()

message = '''  1. add book
  2. Available books
  3. Borrow books
  4. Return books
            '''

while True:
   print(message)

   choose = int(input('Enter option you want :'))
   if choose == 1:

      # load = load_file()
      # print(load)
      newtitle = input('Enter newtitle here :')
      newauthor = input('enter author of book :')
      newid = input('Enter id here :')
      add_data(title=newtitle,author=newauthor,book_id= newid)
      obj.add_books(newtitle, newauthor, newid)

   elif choose == 2:
      obj.available_books()


   elif choose == 3:
      borrowtitle = input('enter book to borrow :')
      obj.borrow_book(borrowtitle)

   elif choose == 4:
      returntitle = input('enter book to be return :')
      obj.return_books(returntitle)
     
   else:
      choose != 1 or 2 or 3 or 4
      with open('myfile.txt', 'r') as file:
            content = file.read()
            print(content)
      break

#############################################################################################

# def add_data(title,author,book_id,availability=True):
#    file = open("text.txt","a")
#    file.write(f"{title},{author},{book_id},{availability}\n")
#    file.close()

# class Book:
#    def __init__(self, title, author, id):
#       self.title = title
#       self.author = author
#       self.id = id

# class Library:
#     def __init__(self):
#        self.books = []


#     def add_books(self, title, author, id):
#        bk = Book(title, author, id)
#        self.books.append(bk.title)
#        print(self.books)


#     def available_books(self):
#        for book in self.books:
#           print(book)


#     def borrow_book(self,title):
#        if title in self.books:
#           print(f'the book {title} is available , you can borrow')
#           self.books.remove(title) 
#           print(self.books)
#        else:
#           print('this book is not available')

#     def return_books(self, book_retn):
#         if book_retn not in self.books:
#            print(f'{book_retn} is a borrowed book ')
#            print(f'{book_retn} is available now')
#         self.books.append(book_retn)
#         print(self.books)


# obj = Library()

# message = '''  1. add book
#   2. Available books
#   3. Borrow books
#   4. Return books
#             '''

# while True:
#    print(message)

#    choose = int(input('Enter option you want :'))
#    if choose == 1:
#       newtitle = input('Enter newtitle here :')
#       newauthor = input('enter author of book :')
#       newid = input('Enter id here :')
#       add_data(title=newtitle,author=newauthor,book_id= newid)
#       obj.add_books(newtitle, newauthor, newid)

#    elif choose == 2:
#       obj.available_books()


#    elif choose == 3:
#       borrowtitle = input('enter book to borrow :')
#       obj.borrow_book(borrowtitle)

#    elif choose == 4:
#       returntitle = input('enter book to be return :')
#       obj.return_books(returntitle)
     
#    else:
#       break

