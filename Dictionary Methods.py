""""""
"""
Features of Dictionary
Syntax - {}
1.Dictionary is an important data types in python
2.Structure {key:value} 
    -Keys are in object form. Hence, it should be as per syntax
    -n' numbers of key:value pairs can be added
    -We can use float value as key
    -We can have multiple values for a single key
4.Dictionary is mutable data types
    Mutable - Values can be updated 
    Immutable - Values cannot be updated
5.Accepts all types of Data 
    Homogenous - Can only store single type of data 
    Hetrogenous - Can store more than one type of data
6.Background Data Structure of Dictionary is - Hash Table
7.Indexing & Slicing not supported (Key acts as an index to fetch values associated with that keys)
8.Sequence order is preserved
9.Duplicate keys are not allowed. (Duplicate values are allowed)
10.There are many method in Dictionary like ...
"""
print(type({}))
#Create empty Dictionary
print({}) #Method 1
print(dict()) #Method 2

d = {1:100,2:200,3:300} #(1,2,3 are keys & 100,200,300 are values)
print(d)

e= {'Name':'Sagar','Age':26,'Place':'Melbourne'}
print(e)

f = {1.11:111} #(Float value as key)
print(f)

#Do we have indexing ?
print(d)
print(d[1]) #No indexing
print(e['Name']) #Key acts as an index

#Multiple values for single key
a = {1:[10,20,30],2:[40,50,60]}
print(a)
#fetch 50 from a
print(a[2][1]) #Indexing on list & Key for dictionary
#change 50=500
a[2][1] = 500
print(a)

#Methods of Dictionary
#1.Get - Returns the value of the key if key is in the dictionary, else default
b = {1:100,2:200,3:300}
print(b.get(1))
print(b[1])
#Difference between 2 options to fetch keys
#Option 1
print(b.get(30)) #if given key is not present or not part of your dictionary then it will return None.
print(b.get(30,'Value not present')) #instead of None we can add different message
print(b.get(30,-1)) #if we want -1 as an output
#Option 2
#print(d[30]) #if given is not present (Output - KeyError)
#2.Update - To reassign the value of the key in the dictionary
b.update({2:20}) #if key:value is present update it
print(b)
b.update({4:400}) #if key:value is not present add it at the end
print(b)
b[4] = 'java' #changes persist in the same object and id is not changing. Hence, it is mutable
print(b)
#3.Setdefault - Insert key with a value of default if key is not in the dictionary.
b.setdefault(5) #Key 5 is not present
print(b) #if key supplied in setdefault not present, it adds with None value
b.setdefault(6,'Batch 22') #instead of None if we want any other object
print(b)
b.setdefault(4) #if we're trying to add a key which is already present, it will return its value
#4.Pop - Remove specified key and return corresponding value
print(b.pop(1)) #returns value 100
print(b) #removes key
#Can we keep pop empty like a list
#b.pop() ---> TypeError
#If we supply a key which is not present
#b.pop(100)  ---> KeyError
print(b.pop(100,-1)) #if we want to replace error with values(-1)
print(b.pop(100,'NA')) #if we want to replace error with values (NA)
#5.Popitem - Removes the item that was last inserted
print(b.popitem())
print(b)
#Difference between Pop Vs Popitem
#Ans.Pop() can remove any item from a dictionary as long as key is specified
#Popitem() can only remove and return the value of the last element
#6.Values - Fetch only values from dictionary
print(b.values())
#7.Keys - Fetch only keys from dictionary
print(b.keys())
#8.Items - Fetch (key,value) as a tuple
print(b.items())
#9.Fromkeys - Returns a dictionary with the specified keys and specified values
print(dict.fromkeys([100,200,300])) #None values
print(dict.fromkeys([100,200,300],'Python')) #Instead of None values set something different
print(dict.fromkeys([100,200,300],['Python','C++','Java'])) #Its not possible
s = 'raju' #Expected Output - {'r':10,'a':10,'j':10,'s':10}
print(dict.fromkeys(s,10))
print(dict.fromkeys(s)) #None values will be set for all keys
print(dict.fromkeys(['raju'],10)) #Expected Output {'raju:10'}
#Use range as an input
print(dict.fromkeys(range(10)))
print(dict.fromkeys(range(1,10,2))) #Odd numbers in dict
print(dict.fromkeys(range(2,11,2))) #Even number in dict









