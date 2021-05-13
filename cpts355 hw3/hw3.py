#name: Hongqi Guo
#student ID: 011552159

#1a
def sumSales(d): 
    l = {}
    #Use the features of dic to find keys and values.
    for store,data in d.items():
        #data also is dic,find key and value.
        for day,value in data.items():
            if day in l.keys():
                l[day] += value
            else:
                l[day] = value
    return l
#1b
#The helper function is used to extract the data in dic.
def helpersum(x,y):
    l = {}
    #two part. if dic in x or dic in y.
    for dic in x.keys():
        if dic in y.keys():
            #if dic both in x and y,+++++
            l[dic] = x[dic] + y[dic]  
        else:
            #if not,list get dic.
            l[dic] = x[dic]
    for dic in y.keys():
        if dic in x.keys():
            l[dic] = x[dic] + y[dic]  
        else:
            l[dic] = y[dic]
    return l
from functools import reduce
#I used list comprehension to calculate. 
#First, all dic in the map, 
#and then lambda was used to extract the corresponding sum of key and value,
#then reduce was used to calculate in turn.
def sumSalesN(di):
    return dict(reduce((lambda x,y : helpersum(x,y)),map(sumSales,di)))

#2a

def searchDicts(L,k):
    #Reverse it.
    L = L[::-1] 
    for dic in L:
        if k in dic:
            #Use the get function to find the value of k, if no output is none.
            return dic.get(k)


#2b
#Using the helper function
def helperSearch(tL,k,index): 
   #get key and value in index
    for key,value in tL[index][1].items(): 
        if key == k:
            return value      
    if tL[index][0] == index:
        return None 
    return helperSearch(tL,k,tL[index][0])

def searchDicts2(tL, k):
    return helperSearch(tL,k,len(tL) - 1)




#3
#easy part.use list comprehension,we want return key, 
# so find key and value in buses,then chack stop in value.
def busStops (buses,stop):
    return[kay for kay, value in buses.items() if stop in value]

#4

def palindromes(s):
    #empty []
    l = []
    #We want strings of length greater than one.
    shortest = 1
    #if s is empty,return empty.
    if s!='':
        for left in range(len(s)):
            for right in range(len(s),left,-1):
                # if s in l,pass.if not,append s in l.
                if s[left:right] in l:
                    pass
                else:
                    if (s[left:right] in (s[left:right])[::-1]):
                        if len(s[left:right]) > shortest:
                            l.append(s[left:right])

    return sorted(l)

# #5a

class interlaceIter(object):
    
    def __init__(self, iter1, iter2):
        self.iter1 = iter1
        self.iter2 = iter2
        self.next = next(self.iter2)
        self.flag = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.flag==0:
            try:
                self.flag=1
                nextdata = next(self.iter1)
            except StopIteration:
                self.flag = 2
        elif self.flag==1:
            try:
                self.flag = 0
                nextdata = self.next
                self.next = next(self.iter2)

            except StopIteration:
                self.flag = 2
        else:
            raise StopIteration

        return nextdata


#5b
def typeHistogram(myiter, n):
    i = 0
    json_temp = {}
    while i < n:
        try:
            item = next(myiter)
            if type(item).__name__ in json_temp:
                json_temp[type(item).__name__] += 1
            else:
                json_temp[type(item).__name__] = 1
        except StopIteration:
            pass
        i+=1


    return [(key,value) for key, value in json_temp.items()]










L = [1,2,3]
def f(L):
    L[:] = ['a','b','c']
    return L
f(L)
print(L)