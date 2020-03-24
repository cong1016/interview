def fun(version1, version2):
    la = version1.split('.')
    lb = version2.split('.')
    num = 0
    if len(la) > len(lb):
        num = len(la)
    else:
        num = len(lb)
    for i in range(num):
        try:
            if len(la[i]) != 1 or len(lb[i]) != 1:
                return 0
            if int(la[i]) > int(lb[i]):
                return 1
            elif int(la[i]) == int(lb[i]):
                continue
            elif int(la[i]) == int(lb[i]) == None:
                return 0
            else:
                return -1
        except Exception as e:
            if len(la) > len(lb):
                if int(la[-1]) == 0 and int(lb[-1])== 0:
                    return 0
                return 1
            elif len(la) < len(lb):
                if int(la[-1]) == 0 and int(lb[-1])== 0:
                    return 0
                return -1

if __name__=="__main__":
    print(fun('1.0','1.0.0'))



