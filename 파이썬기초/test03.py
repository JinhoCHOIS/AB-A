def add_comma(val):
    s=str(val)
    if len(s)>3 :
        for i in range(-len(s),0):
            if i%3==0 :
                s=s[:i]+','+s[i:]
    return s

def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_12 = add_comma(12)
    print(comma_added_1234) # ‘1,234’
    print(comma_added_12345678) # ‘12,345,678’
    print(comma_added_12) # ‘12’

if __name__=='__main__':
    main()