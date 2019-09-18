import random

def LCM(l):
    n=len(l)

    for i in range(n) :
        if %l[i]==int() :
                     ans /= l[j]
                else :
                    ans *= l[j]
    return ans

def GCD(l):
    for i in l :




    return

def main():
    a=[]
    for i in range(10):
        a.append(random.randint(1, 100)) # 1에서 100 중 정수 하나
        print(a)
    lcm_value=LCM(a)
    gcd_value=GCD(a)
    print('최소공배수: ', lcm_value, ', 최대공약수: ', gcd_value)

if __name__=='__main__':
    main()