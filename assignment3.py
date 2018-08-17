#question1:->create a list with user defined inputs?
list1=[]
entry1=input("enter an element ")
list1.append(entry1)
entry2=input("enter next element ")
list1.append(entry2)
entry3=input("enter last element ")
list1.append(entry3)
print(list1)

#or
lisst1=[]
print("Enter values you want to insert in list(8 values)")
for i in range(0,8):
    x=input()
    lisst1.append(x)
print(lisst1)

#Question2:->Add the following list to above created list?

'''list1=[]
entry1=input("enter an element ")
list1.append(entry1)
entry2=input("enter next element ")
list1.append(entry2)
entry3=input("enter last element ")
list1.append(entry3)'''
list2=['google','apple','facebook','microsoft','tesla']
new=list1+list2
print(new)

#or
'''lisst1=[]
print("Enter values you want to insert in list(8 values)")
for i in range(0,8):
    x=input()
    lisst1.append(x)'''
list2=['google','apple','facebook','microsoft','tesla']
neew=lisst1+list2
print(neew)

#Question3:->Count the number of times an object occurs in a list?
liist=[1,2,3,4,5,6,7,8,2,3,5,3,2,4,2,1,2,2,4]
print("list is:",liist)
print("Enter an element we want to find the frequency")
check=int(input())
count=liist.count(check)
print("total count is :",count)

#Question4:->Create a list with numbers and sort it in ascending order?
liisst=[]
print("Enter elements which you want to insert in list")
for i in range (10):
    x=int(input())
    liisst.append(x)
print("List after inserting the elements")
print(liisst)
liisst.sort()
print("List after sorting")
print(liisst)

#Question5:->Given are two one-dimensional arraysA and B which are sorted in ascending
#order.Write a program to merge them into a single sorted arrayC thet contains
#every item from arraysA and B,in ascending order [list].
arrayA=[1,2,3,57,75,92]
print("First list elements are:",arrayA)
arrayB=[34,45,76,84,98]
print("Second list elements are:",arrayB)
arrayC=arrayA+arrayB
arrayC.sort()
print("List after merging 2 arrays(A and B):",end=' ')
print(arrayC)

'''#Question6(optional):->Implement stack and Queue using lists?
lsit=[1,2,3,4,5,6,7,8,9]
p=len(lsit)
print("Stack means last in first out")
print("Queue means first in first out")
print("List is:",lsit)
print("Stack implementation")
for i in range (0,len(lsit)):
    print(lsit.pop(),end=" ")
print(end='\n')
lsit1=[1,2,3,4,5,6,7,8,9]
print("Enter values in list")
for i in range (0,p):
    x=input()
    lsit.append(x)
print("Queue implementation")
for i in range (0,len(lsit)):
    print(lsit[i],end=" ")
print(end='\n')'''

#Question6:->count even and odd numbers in the list?
listt=[23,45,22,65,80,98,67,44,67,89,70,97,94]
count=0
count1=0
print("List is :",listt)
for i in range(0,len(listt)):
    if (listt[i]%2==0):
        count=count+1
    else:
        count1=count1+1
print("total no. of even values in list are :",count);
print("total no. of odd values in list are :",count1);

#Question1(touple):->Print a tuple in reverse order.
toupl1=(10,20,30,69,76,80,64,76)
new1=reversed(toupl1)
print("Touple in reverse order",tuple(new1))

#Question2:->Find largest and smallest elements of a tuples.
toup=(3,5,6,8,56)
print("elements in touple are : ",toup)
large=max(toup)
small=min(toup)
print("Largest element in touple is : ",large)
print("Smallest element in touple is : ",small)

#Question1:->Convert a string to uppercase?
string1=input("Enter a string : ")
temp=string1.upper()
print(temp)

#Question2:->Print true if the string contains all numeric characters?
str1=input("Enter a string")
temp=str1.isdigit()
print(temp)

#Question3:->Replace the word "World" with your name in the string "Hello World"?
stringg="Hello World"
temp=stringg.replace('World','Chirag Narang')
print(temp)

