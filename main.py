
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





def uloha_4_11(n):
    for i in range(n,0,-1):
        print("." * i)
        print(i)


def uloha_4(n):
    sirka =  2 * n - 1


def uloha_4_1(n):
    for i in range(n):
        print("." * (i + 1) +"#" * (i - 1))



def uloha_8(n):
    for i in range(n):
        pass


n = 10

uloha_1(n)
uloha_2(n)
uloha_3(n)

