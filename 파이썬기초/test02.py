def check_prime(num):

    if num == 1 :
        return 0
    for i in range(2, num) :
        if num%i == 0 :
            return 0
    return 1

def main():
    a = 13
    b = 15
    if check_prime(a):
        print(str(a)+'는 소수입니다.')
    else:
        print(str(a)+'는 소수가 아닙니다.')
    if check_prime(b):
        print(str(b)+'는 소수입니다.')
    else:
        print(str(b)+'는 소수가 아닙니다.')

if __name__=='__main__':
    main()