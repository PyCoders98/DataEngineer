""" Implement the cd (change directory) command on Unix as a string processing function

 | cwd      | cd (arg)       | output
 | -------- | -------------- | ------
 | /        | foo            | /foo
 | /foo     | /bar           | /foo/bar
 | /foo/bar | ../../../../.. | /
 | /x/y     | ../p/../q      | /x/q
 | /x/y     | /p/./q         | /p/q
"""

current = "/cd bar cd /bar cd foo/bar cd /x/y"
# current = "/"
print("Enter commands : ", end="")
cwd = ""
l = []
cmd = ""
d1 = {
    "foo": {"bar": {"none": 0}},
    "x": {"p": {"q": {"none": 0}}, "y": {"none": 0}, "q": {"none": 0}},
}
lst = []
temp = d1
while True:
    cd = input("Enter")
    # lst1 = cd.split("/")[1:]
    # lst.append(lst1)
    # if len(l) < 1:
    #     temp = d1
    if "/" in cd:
        lst1 = cd.split("/")
        lst.append(lst1)
        # lst = cd.split("/")[1:]
    else:
        if cd=="..":
            pass
        else:
            print("*****")
            lst.append(cd)
    length = len(cd)
    # lst = filter(lambda x: x != "..", cd)
    # # for l in range(length::-1):
    # #     if lst[l]=="..":
    # #         lst.pop()
    # for i in lst:
    temp = d1
    if "" == cd:
        pass
    if ".." in cd:
        if len(l):
            l.pop()
            lst.pop()
            temp = d1
            # for i in lst:
            #     print(lst)
            #     print(temp)
            #     if i in temp.keys():
            #         temp = temp[i]
            #         print(temp)
        else:
            pass
    if "." in cd:
        pass
    elif cd != "." and cd != "..":
        print(temp)
        l.clear()
        for k in lst:
            print(k, l, "$$$$$")
            if k in temp.keys():
                temp = temp[k]
                l.append(k)
                print(l)
            else:
                print("No such directory !")
        print(l)

    cwd = "/".join(l)
    # cd = input(f"dir{cwd}")

    print(cwd)
