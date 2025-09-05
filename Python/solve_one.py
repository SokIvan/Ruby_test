def capcha(str):
    if (len(str)==0):
        return
    k = 0
    if (len(str) == 1):
        return int(str)*2
    for i in range(len(str)-1):
        if str[i]==str[i+1]:
            k+=int(str[i])
    if str[i+1] == str[0]:
        k+=int(str[0])
        
    return k

if __name__ == "__main__":
    print(capcha("823113328"))
    print(capcha(""))
    print(capcha("2"))