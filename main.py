
def uloha_1(n):
    for i in range(n):
        print("#"*n)


def uloha_2(n):
    print("#" * n)
    for i in range(n - 2):
        print("#" + " " * (n - 2) + "#")
    print("#" * n)


def uloha_3(n):
    for i in range(n):
        print("#"*(i + 1))


def uloha_4(n):
    promenna = 1
    for i in range(n,-1,-1):
        print("." * i + "#" * promenna)
        promenna += 2


def uloha_6(n):
    promenna = 1
    for i in range(n,-1,-1):
        print("." * i + "#" * promenna)
        promenna += 2
    promenna -= 4
    for i in range(1,n+1):
        print("." * i + "#" * promenna)
        promenna -= 2

def uloha_8(n):
    stridani = {1:"#", -1:"."}
    jedna = 1
    for i in range(n):
        rada = ""
        for y in range(n):
            rada += stridani[jedna]
            jedna *= -1
        print(rada)
        if(n%2==0): jedna *= -1

def uloha_9(n, m):
    stridani = {1:"#", -1:"."}
    jedna = 1
    for i in range(n):
        rada = ""
        for y in range(n):
            rada += stridani[jedna]*m
            jedna *= -1
        if(n%2 ==0):jedna *= -1
        print("\n".join([rada]*m))


n = 10
m = 5

uloha_1(n)
uloha_2(n)
uloha_3(n)
uloha_4(n)
uloha_6(n)
uloha_8(n)
uloha_9(n,m)

