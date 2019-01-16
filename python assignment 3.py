# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 00:26:57 2019

@author: thanusha
"""
#problem statement 1.1
#reduce function
listx=[1,3,2,5]
listy=[42,11,47,13]    #sample list input
def myreduce(list1):   #defining function myreduce with keyword def 
    sum=0              
    for x in list1:    # iterating over the list 
        sum= sum+x  # summing the element
    return sum      # return the result
print(myreduce(listy)) # calling the function and printing the result   
#problem statement 1.2
#filter function
list_need =range(-5,5)  #sample list input
def myfilter(listz):    #defining function myfilter with keyword def 
    newl=[]             # empty list created
    for y in listz:     # iterating over the list 
        if y<0:        # performing filtering operation using if conditions
            newl.append(y) # adding the filtered result to empty list
    return newl            # return the resultant list
print (myfilter(list_need))      # calling the function and printing the result 

#problem statement 3
#using list comprehension
#Q1 
q1=[x for x in "ACADGLID"]     # iterating over string 
print(q1)
#Q2
q2=[x*a for x in "xyz" for a in range(1,5)] # using operation like nested for loop over the string in given range
print(q2)
 #Q3
q3=[x*a for x in range(1,5) for a in "xyz"]
print(q3)
#q4
q4=[[x+1] for a in range(1,4) for x in range(a,a+3)]
print(q4)
#q5
q5=[[a+x for a in range(1,5)] for x in range(1,5)]
print(q5)
#q6
q6=[(x,a)for a in range(1,4) for x in range(1,4)]
print(q6)



# longest word required


word_list=["thanusha","pabbisettyvnetakakarthik", "pabbisettyvenkatavihaansai","sudharshan", "venkatavihaan"]
def longestWord(word_list):       # function defination
   longest=""                    # null string
   b=0                           # using a temporary variable for filtering purpose
   for x in word_list:   # iterating over the input list
     a=len(x)            # finding the length of each word using len() function
      
     if a>b:              # using if condition to perform requried operation
           b=a
        #print(a,b)
           longest=x
   return longest           # return the resultant after iteration is done
print("longest word in list is", longestWord(word_list)) #calling  the function and printing the result
