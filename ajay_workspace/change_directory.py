""" Implement the cd (change directory) command on Unix as a string processing function

 | cwd      | cd (arg)       | output
 | -------- | -------------- | ------
 | /        | foo            | /foo
 | /foo     | /bar           | /foo/bar
 | /foo/bar | ../../../../.. | /
 | /x/y     | ../p/../q      | /x/q
 | /x/y     | /p/./q         | /p/q
"""

print("Enter commands : ", end="")
cwd = ""
l = []
cmd = ""
d1 = {
    "foo": {"bar": {None: 0}},
    "x": {"p": {"q": {None: 0}}, "y": {None: 0}, "q": {None: 0}},
}
lst = []
temp = d1
while True:
    cd = input("Enter")
    if "/" in cd:
        lst1 = cd.split("/")
        lst.append(lst1)

    else:
        if cd == "..":
            if len(lst):
                lst.pop()
                print("pop", lst)
        elif cd in temp.keys():
            lst.append(cd)
            print("lst add", lst)
    length = len(cd)
    temp = d1
    if "" == cd:
        pass
    if ".." in cd:
        # lst.pop()
        if len(l):
            l.pop()
        else:
            pass
    if "." in cd:
        pass
    elif cd != "." and cd != "..":
        print(temp)
        l.clear()
        print("lst", lst)
        for k in lst:
            if k in temp.keys():
                temp = temp[k]
                l.append(k)
                print(l)
            else:
                print("No such directory !")
    cwd = "/".join(l)
