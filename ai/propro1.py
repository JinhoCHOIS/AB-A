#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    if input_id in d:
        print("    Student            Name    Midterm    Final    Average    Grade")
        print("---------------------------------------------------------------------")
        print("   %s  %s      %s         %s       %.1lf       %s" %(input_id[0], input_id[1], input_id[2], input_id[3], input_id[4], input_id[5]))
    else:
        print("NO SUCH PERSON.")

def changescore():
     input_id=input("Student ID: ")
    if input_id in d:
       
    else:
        print("NO SUCH PERSON.")

    

    

#----------------- 함수 정의 파트 끝 ---------------------    

show()

 

while 1 :

    b = input("# ")

    c = b.lower()

#string 받은 input을 모두 소문자로 통일시킨 후 함수 실행, 모두 동일값

    if c=='show':

        show()

#     elif b=='search':

#         search()

#     elif b=='changescore':

#         changescore()

#     elif b=='searchgrade':

#         searchgrade()

#     elif b=='add':

#         add()

#     elif b=='remove':

#         remove()

#     elif b=='quit':

#         quit()

    else :

        b = input("# ")

        c = b.lower()

        

#7 개의 명령어가 아닌 경우 while 반복, 다시 입력 받음

