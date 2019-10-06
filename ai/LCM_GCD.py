import random
def LCM(l):  # 최소공배수
    myl = l.copy()
    for i in range(len(l) - 1):
        lcm = myl[i] * myl[i + 1] / GCD(myl[i:i + 2])
        myl[i + 1] = lcm
    return int(lcm)
def GCD(l):  # 최대공약수    
    for k in range(min(l), 0, -1):
        b = 0
        for j in range(len(l)):
            if l[j] % k == 0:
                b += 1
        if b == len(l):
            return k
def main():
    a = []
    for i in range(10):
        a.append(random.randint(1, 100))  # 1에서 100 중 정수 하나
    print(a)
    lcm_value = LCM(a)
    gcd_value = GCD(a)
    print('최소공배수: ', lcm_value, ' 최대공약수: ', gcd_value)
if __name__ == '__main__':
    main()