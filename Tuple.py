t1=() #declaration of empty tuple
t2=(2,) #single element tuple
print(t2)
t=('Sachin','Kumar',22,9,1999,'Jatin',"Kumar",28,8,2004) # tuple t with values inside it
print(t) #print all the elements of tuple t
print(type(t)) #identify the tupe/class of variable t
print(len(t)) #count the number of elements in tuple t
print(t*2) #print all the elements of tuple t twice which can also be n times

# Tuple Indexing
print(t[0]) #print the first element of tuple t
print(t[-1]) # print the last element of tuple t
print(t[3]) #print the 4th element of tuple t

# Tuple Slicing or Slicing a tuple
print(t[1:4]) #print the elements of tuple t from 1st index value to 3rd index value & not includes the element of 4th index value
print(t[1:]) #print all the elements of tuple t from 1st index value
print(t[:-4]) #print all the elements of tuple t before the last 4th element
print(t[1:-1]) #print all the elements of tuple t from 1st index value to the last 2nd element

# Tuple Slicing Steps or Steps in tuple slicing
print(t[1:4:3]) #print all the elements of tuple t from 1st index value to 3rd index value with jumping 2 steps each and not includes the element of 4th index value
print(t[-5:-2:2]) #print all the elements of tuple t that ranges from the last 5th element to the last 3rd element with jumping 1 step each and not includes the last 2nd element

print(t[::-1]) #reverse the tuple t
print(t.count(22)) #count the number of 22 element in tuple t
print(t.index('Jatin')) #identifies the index value of element 'Jatin' in tuple t
print(t+t2) #concatination of t and t2 tuple in order to merge all the elements inside a single tuple
t3=(t,t2) #nesting of t and t2 tuple in order to display both tuples inside a single tuple
print(t3)

tn=(2,1,6,9,4,2.6,14.56,11.54)
print(max(tn)) #identifies the maximum value from tuple tn
print(min(tn)) #identifies the minimum value from tuple tn
print(14 in tn) #identifies whether 74 element in present inside tuple tn
print(74.36 in tn) #identifies whether 74.36 element in present inside tuple tn

# It is mandatory that all the elements should be in numeric form in order to perform max & min operations on tuple
