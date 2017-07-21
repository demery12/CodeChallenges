# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
def myf(n,k,c):
    k=int(k)
    index = 0
    for item in c:
        if item == 2:
            continue
        elif item == 0:
            temp = k
            while temp != 0 and c[index+temp]!=1:
                temp -=1
            if temp == 0:
                return -1
            else:
                for i in range(index,index+temp+k+1):
                    if c[i]==1:
                        c[i]=3
                    elif c[i]==0:
                        c[i]=2
                    else:
                        pass
                c[index+temp]=4
        elif item == 1:
            pass
        print c
def myd(n,k,c):
    k=int(k)
    index=0
    d={}
    num=0
    for item in c:
        l=[]
        for i in range(index-k,index+k+1):
            if i>0 and i<len(c) and c[i] ==1:
                l.append(i)
        if l==list():
            return -1
        d[index]=l
        index+=1
    print d
    index = 0
    for item in c:
        print d
        if item==0:
            on=d[index][-1]
            num+=1
            hit_list=[]
            for item in d:
                if on in d[item]:
                    hit_list.append(item)
            for item in hit_list:
                del d[item]
                
        index+=1
    return num
'''
def myi(n,k,c):
    k=int(k)
    index=k
    on=0
    while index<len(c):
        if c[index] !=0:
            on+=1
            index+=2*k+1
        else:
            count=1
            index-=1
            while index>-1 and count<=k:
                if c[index]==1:
                    on+=1
                    break
                else:
                    count +=1
                    index -=1
            if count>k:
                return -1
    index-= 2*k+1 #cud b bad #was bad
    if index+k<len(c)-1:
        if c[index+k+1]==1:
            on+=1
        else:
            back = 0
            while back<=k:
                if c[index]==1:
                    on+=1
                    break
                else:
                    back+=1
                    index-=1
            if back>k:
                return -1
    return on
                    
n,k=raw_input().split(' ')
c = raw_input().split(' ')
c=[int(i) for i in c]
print myi(n,k,c)
