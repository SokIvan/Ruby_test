def kontr_sum(mas):
    k = 0
    for i in range(len(mas)):
        k+=(max(mas[i])-min(mas[i]))
    return k






if __name__ == "__main__":
    print(kontr_sum([
        [1,2,3,4],
        [8,3,2],
        [3,7,4,5],
    ]))