def mean_and_var(*val):
    hap1=0;hap2=0;res1=0;res2=0
    n=len(val)

    for i in val :
        hap1+=i[0]
        hap2+=i[1]
    m1 = hap1 / n; m2 = hap2 / n
    m=(m1, m2)

    for i in val :
        res1+=((i[0]-m1)**2)
        res2+=((i[1]-m2)**2)
    va1 = res1 / n; va2 = res2 / n
    var=(va1, va2)

    return m, var

def main():
    v1=(0, 1)
    v2=(0.5, 0.5)
    v3=(1, 0)
    m, var = mean_and_var(v1, v2, v3)
    print('평균: ', m, '분산: ', var)

if __name__=='__main__':
    main()