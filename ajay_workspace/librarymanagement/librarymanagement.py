def add_book(book_id1, book_name, author_name, booked=False):
    book_id = book_id1
    book_name = book_name
    author_name = author_name
    booked = booked
    file = open("t1.txt", "a")
    file.write(f"{book_id},{book_name},{author_name},{booked}\n")
    print("-" * 20)
    print("Added successfully...")
    print("-" * 20)
    file.close()


def borrow_book(book_id):
    file = open("t1.txt", "r")
    file_data = file.readlines()
    f_data = file_data
    file.close()
    f = open("t1.txt", "w")
    for num, i in enumerate(f_data):
        data = i[:-2].split(",")
        if book_id == data[0]:
            data[-1] = str(True)
            file_data[num] = ",".join(data) + r"\n"
    print("-" * 20)
    print("Borrowed Successfully...")
    print("-" * 20)
    f.writelines(file_data)
    f.close()


def return_book(book_id):
    file = open("t1.txt", "r")
    file_data = file.readlines()
    f_data = file_data
    file.close()
    f = open("t1.txt", "w")
    for num, i in enumerate(f_data):
        data = i[:-2].split(",")
        if book_id == data[0]:
            data[-1] = "False"
            file_data[num] = ",".join(data) + r"\n"
    f.writelines(file_data)
    print("-" * 20)
    print("Returned Successfully...")
    print("-" * 20)
    f.close()


def view_available_books():
    f = open("t1.txt", "r")
    print("-" * 53)
    print(
        "|",
        " book_id ",
        "|",
        "author_name".center(20),
        "|",
        "book_name".center(20),
        "|",
    )
    print("-" * 53)
    for i in f.readlines():
        if "False" in i:
            book_id, author_name, book_name, _ = i.split(",")
            print(
                "|",
                book_id.center(4),
                "|",
                author_name.center(20),
                "|",
                book_name.center(20),
                "|",
            )
    print("-" * 53)


def check_already_exist(book_id, indicator=False):
    file = open("t1.txt", "r")
    file_data = file.readlines()
    flag = False
    if indicator:
        print("indicator")
        for i in file_data:
            data = i.split(",")
            print(book_id, data[0], data[-1][:-2], "False")
            if book_id == data[0] and data[-1][:-2] == "False":
                file.close()
                return "not borrowed"
            elif book_id == data[0] and data[-1][:-2] == "True":
                return "borrowed"
        else:
            return "index Error"
    else:
        for i in file_data:
            data = i.split(",")
            if book_id == data[0]:
                file.close()
                flag = True
                break
        return flag


def operation():
    while True:
        print("1 for Add book.")
        print("2 for Booking a book.")
        print("3 for return book.")
        print("4 for view available books.")
        print("5 For Exit.")
        n = int(input("Press key to perform operation : "))
        if n == 1:
            book_id = input("Enter book book_id : ")
            if check_already_exist(book_id):
                print("-" * 20)
                print("Book Already Exists! ")
                print("-" * 20)
            else:
                book_author = input("Enter author name : ")
                book_name = input("Enter Book name : ")
                add_book(book_id, book_author, book_name)
        elif n == 2:
            book_id = input("Enter book book_id You want to borrow : ")
            borrow_book(book_id)
        elif n == 3:
            book_id = input("Enter book book_id You want to return : ")
            x = check_already_exist(book_id, indicator=True)
            if x == "not borrowed":
                print("-" * 20)
                print("Book Already Exists!")
                print("-" * 20)
            elif x == "borrowed":
                return_book(book_id)
            else:
                print("no book available")
        elif n == 4:
            view_available_books()
        else:
            break


operation()
