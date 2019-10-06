
# coding: utf-8

# In[1]:



#project 1 - 성적 관리 프로그램

 
import os

input_file = input()

 

if os.path.exists(input_file) :

    f = open("input_file", "r")

elif input_file == '':

    f = open("students.txt", "r")

data = f.readlines() 

k = data.copy()

list_d=[]

 

for i in k :

    list_d.append(i.split())

# 공백 기준으로 스플릿 하니까 성과 이름도 구분

for i in list_d :

    i[1] = '%14s' %(i[1] + ' ' + i[2]) # 전체길이14, 왼쪽공백4

    i.remove(i[2])

    i.append((float(i[2])+float(i[3]))/2) # 현재 문자열 원소 str에서 / 나누기 연산을 시행할 수 없으므로 float로 형변환     

                                          # 평균을 i[4]에 저장, i[4]상태로 대입 불가하므로 i.append 사용

# 따라서 성이 있는 i[1]에 공백과 i[2]의 값을 추가 시켜서 i[1]에 성과 이름이 모두 들어가게 만듦   

#----------- 함수 정의 파트 -----------

def show():

    for i in list_d :

        i[4]=((float(i[2])+float(i[3]))/2)                                 

        if i[4]>=90 :                         

            i.append('A')

        elif i[4]>=80 :

            i.append('B')

        elif i[4]>=70 :

            i.append('C')

        elif i[4]>=60 :

            i.append('D')

        else :

            i.append('F') # 평균 점수에 따라서 학점 부여

    list_d.sort(key=lambda e : e[4], reverse=True) #람다의 정의, 원리, 기존 함수와의 차이 등 정리

                                              #sort의 기본값인 오름차순과 내림차순의 적용에 대해서 설명

    print("    Student            Name    Midterm    Final    Average    Grade")

    print("---------------------------------------------------------------------")

    for i in range(len(list_d)) :

        print("   %s  %s      %s         %s       %.1lf       %s" %(list_d[i][0], list_d[i][1], list_d[i][2], list_d[i][3], list_d[i][4], list_d[i][5]))

        

def search():

    input_id=input("Student ID: ")
    temp=0
    
    for i in list_d :
        if input_id in i:          
            print("    Student            Name    Midterm    Final    Average    Grade")
            print("---------------------------------------------------------------------")
            print("   %s  %s      %s         %s       %.1lf       %s" %(i[0], i[1], i[2], i[3], i[4], i[5]))
            temp=1
            
    if temp==0:
        print("NO SUCH PERSON.")
        
def regrade(a): #changescore시 학점 재부여할 때 코드가 너무 길어지고 반복하므로 따로 함수 생성
    if a>=90 :                         
        return 'A'
    elif a>=80 :
        return 'B'
    elif a>=70 :
        return 'C'
    elif a>=60 :
        return 'D'
    else :
        return 'F'

def changescore():
    input_id=input("Student ID: ")
    temp=0
    for i in list_d:
        if input_id in i:
            temp=1
            input_term=input("Mid/Final? ")         
            if input_term=='mid':
                input_score=int(input("Input new score: "))
                if 0<=input_score<=100:
                    print("    Student            Name    Midterm    Final    Average    Grade")
                    print("---------------------------------------------------------------------")
                    print("   %s  %s      %s         %s       %.1lf       %s" %(i[0], i[1], i[2], i[3], i[4], i[5]))
                    i[2]=input_score
                    i[4]=(float(i[2])+float(i[3]))/2
                    i[5]=regrade(i[4])
                    print("Score changed.")
                    print("   %s  %s      %s         %s       %.1lf       %s" %(i[0], i[1], i[2], i[3], i[4], i[5]))
                        
            if input_term=='final':
                input_score=int(input("Input new score: "))
                if 0<=input_score<=100:
                    print("    Student            Name    Midterm    Final    Average    Grade")
                    print("---------------------------------------------------------------------")
                    print("   %s  %s      %s         %s       %.1lf       %s" %(i[0], i[1], i[2], i[3], i[4], i[5]))
                    i[3]=input_score
                    i[4]=(float(i[2])+float(i[3]))/2
                    i[5]=regrade(i[4])
                    print("Score changed.")
                    print("   %s  %s      %s         %s       %.1lf       %s" %(i[0], i[1], i[2], i[3], i[4], i[5]))
    if temp==0:
        print("NO SUCH PERSON.")
        
def add():
    input_id=input("Student ID: ")
    temp=0
    for i in list_d:
        if input_id in i:
            temp=1
                
    if temp==1:
        print("ALREADY EXISTS.")
        return
    
    k=['', '', 0, 0, 0.0]
    k[0]=input_id
    input_name=input("Name: ")
    k[1]=input_name
    k[1]='%14s' %k[1]
    input_mid=input("Midterm Score: ")
    k[2]=input_mid
    input_fin=input("Final Score: ")
    k[3]=input_fin
    list_d.append(k)
    print("Student added.")
    print(list_d)
    
        
def searchgrade():
    input_grade=input("Grade to search: ")
    temp=0
    new_list=[]
    gra_list=['A', 'B', 'C', 'D', 'F']
    if input_grade in gra_list:
        for i in list_d:
            if input_grade==i[5]:
                new_list.append(i)
                temp=1
    else:
        return
        
    if temp==1:
        print("    Student            Name    Midterm    Final    Average    Grade")
        print("---------------------------------------------------------------------")
        for i in new_list:
            print("   %s  %s      %s         %s       %.1lf       %s" %(i[0], i[1], i[2], i[3], i[4], i[5]))
                
    if temp==0:
        print("NO RESULTS.")
        
def remove():
    if len(list_d)==0:
        print("List is empty.")
        return
    input_id=input("Student ID: ")
    temp=0
    for i in list_d :
        if input_id in i:          
            list_d.remove(i)
            print("Student removed.")
            temp=1
            break
    
    if temp==0:
        print("NO SUCH PERSON.")
        
def quit():
    input_yon=input("Save data?[yes/no] ")
    if input_yon == 'yes':
        input_file=input("File name: ")
        g=open(input_file,"w")
        for i in range(len(list_d)):
            girok="%s    %s    %s    %s" %(list_d[0], list_d[1], list_d[2], list_d[3])
            g.write(girok)
        g.close()
        f.close()
        
    

#----------------- 함수 정의 파트 끝 ---------------------    

show()

 

while 1 :

    b = input("# ")

    c = b.lower()

#string 받은 input을 모두 소문자로 통일시킨 후 함수 실행, 모두 동일값

    if c=='show':

        show()

    elif c=='search':

        search()

    elif c=='changescore':

        changescore()
        
    elif c=='add':

        add()

    elif c=='searchgrade':

        searchgrade()


    elif c=='remove':

        remove()

    elif c=='quit':

        quit()

    else :

        b = input("# ")

        c = b.lower()

        

#7 개의 명령어가 아닌 경우 while 반복, 다시 입력 받음

