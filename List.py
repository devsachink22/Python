l1=[] #declaration of an empty list
l2=[2,] #single item list
l=['sachin','kumar',22,9,1999] #list l with values inside it
print(l) #print all the elements of list l
print(type(l)) #print the type/class of variable l
print(len(l)) #identify the number of elements stored in list l
print(l*4) #print the items stored in list l for 4 times which can also be n times

# List Indexing
print(l[0]) #print the first element of list l
print(l[-1]) # print the last element of list l
print(l[3]) #print the 4th element of list l

# List Slicing or Slicing a list
print(l[1:4]) #print the elements of list l from 1st index value to 3rd index value & not includes the element of 4th index value
print(l[1:]) #print all the elements of list l from 1st index value
print(l[:-4]) #print all the elements of list l before the last 4th element
print(l[1:-1]) #print all the elements of list l from 1st index value to the last 2nd element

# List Slicing Steps or Steps in list slicing
print(l[1:4:3]) #print all the elements of list l from 1st index value to 3rd index value with jumping 2 steps each and not includes the element of 4th index value
print(l[-5:-2:2]) #print all the elements of list l that ranges from the last 5th element to the last 3rd element with jumping 1 step each and not includes the last 2nd element

print(l[::-1]) #reverse a list l
l.append('Jatin') #insert an element 'Jatin' at the last of the list l
print(l)
l.insert(0,2) #insert an element 2 at the 0 index value of list l
print(l)
l[2]='bhatia' #update an element of 2nd index value of list l to 'bhatia'
print(l)
l.pop() #delete the last element of list l
print(l)
l.remove('sachin') #remove an element 'sachin' from list l
print(l)
del(l[2]) #delete the element of 2nd index value of list l
print(l)
del l[3] #delete the element of 3rd index value of list l
print(l)
print(l.count('ar')) #count the number of 'ar' element in list l
print(l.index('bhatia')) #identifies the index value into which an element 'bhatia' is stored inside list l
l.clear() #removes all the elements from list l
print(l)

l1=['Sachin','Kumar']
l2=[22,9,1999]
l=l1.copy() #copy all the elements of l1 list to l list
print(l)
l1.extend(l2) #extend the l1 list with the elements of l2 list
print(l1)
print(l1+l2) #concatination of l1 & l2 to merge the elements of both list inside a single list
print(l1,l2) #nesting of list l1 & l2 to display both lists

ln=[2,1,6,9,4,2.6,14.56,11.54]
print(5 in ln) #checks whether an element 5 is present in ln
print(14.56 in ln) #checks whether an element 14.56 is present in ln
print(max(ln)) #identifies the max value of list ln
print(min(ln)) #identifies the min value of list ln
ln.sort() #sort the list ln in ascending order
print(ln)
ln.sort(reverse=True) #sort the list ln in descending order
print(ln)

# All the elements should be in numeric form in order to perform max, min & sort functions on list
