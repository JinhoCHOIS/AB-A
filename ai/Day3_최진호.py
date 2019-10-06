
# coding: utf-8

# In[34]:


with open("score.txt", "r") as f :
    data = f.readlines()
    a=[]; b=[]; c=[]
    for i in data :
        a.append(i.split())
  
    for i in a : 
        b.append(float(i[1])*0.4+float(i[2])*0.6)
        
        
    for i in b :   
        if i>=90 :
            c.append('(A)')
        elif i>=80 :
            c.append('(B)')
        elif i>=70 :
            c.append('(C)')
        elif i>=60 :
            c.append('(D)')
        else :
            c.append('(F)')
   
with open("report.txt","w") as g:
    for i in range(len(data)) :
        da= "%s %s %s %s %s\n" %(a[i][0], a[i][1], a[i][2], b[i], c[i])
        g.write(da)
    

