def numInv(num):
    num=str(num)
    inv=""
    for i in range(len(num)-1,0,-1):
        inv+=num[i]
    print(inv)

numInv(12345)