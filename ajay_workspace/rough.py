def generate_book_id():
    file = open("t1.txt","r")
    data = file.readlines()
    if data:
        t = data[-1].split(",")
        new_id = int(t[0])
        return new_id+1
    return 101
        
print(generate_book_id())