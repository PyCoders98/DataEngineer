""" Implement the cd (change directory) command on Unix as a string processing function

 | cwd      | cd (arg)       | output
 | -------- | -------------- | ------
 | /        | foo            | /foo
 | /foo     | /bar           | /foo/bar
 | /foo/bar | ../../../../.. | /
 | /x/y     | ../p/../q      | /x/q
 | /x/y     | /p/./q         | /p/q
"""

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

    cd = input(f"ajay@ajay/{cwd}:$ ")
    cd = cd.replace("cd ", "")
    if cd=="ls":
        print(tuple(temp.keys()))
        continue
    if "/" in cd:
        lst1 = cd.split("/")
        lst.extend(lst1)
        lst = [i for i in lst if "" != i]
        lst1.clear()
    else:
        lst.append(cd)
    length = len(cd)
    temp = d1
    if "" == cd:
        pass
    if "." in lst:
        for i in range(lst.count(".")):
            index = lst.index(".")
            lst.pop(index)
    elif cd != ".":
        if ".." in lst:
            # ["a","b","c","..","..","..","..","foo"]
            for i in range(lst.count("..")):
                index = lst.index("..")
                if index-1 >= 0:
                    lst.pop(index)
                    lst.pop(index-1)
                else:
                    lst.pop(index)

        for k in lst:
            if k in temp.keys():
                temp = temp[k]
            else:
                lst.pop()
                print("No such directory !")
    cwd = "/".join(lst)
