str = ""
lst = []
while True:
    cd = input(f"dir{str}$")
    if "cd" in cd:
        try:
            lst2 = (cd.replace("cd", "/")).split("/")
            lst2.remove("")
            lst2[0] = lst2[0].strip(" ")
        except Exception as e:
            pass
        print(lst2)

        for j in range(len(lst2)):
            for i in range(len(lst2)):
                if " " in lst2[i]:
                    break
            else:
                if ".." in lst2[j]:
                    count = cd.count("..")
                    lst = cd.split("/")
                    for i in range(len(lst)):
                        if ".." in lst[i]:
                            if str != "":
                                index = str.rindex("/")
                                str2 = str[0:index]
                                str = str2
                        elif "." in lst[i] or "./" in lst[i]:
                            pass
                elif "." in lst2[j]:
                    pass

                elif "cd " in lst2[0]:
                    str += cd.replace("cd ", "/")
                else:
                    if lst2[j] == "":
                        pass
                    else:
                        str += "/" + lst2[j]
