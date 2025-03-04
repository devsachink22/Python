d1={} #declaration of an empty dictionary
d2={2:3,} #single item dictionary
print(d2)
d={'firstname':'sachin',
'lastname':'kumar',
'age':25,
'profession':'engineer'} #dictionary d with key-value pairs inside it
print(d) #print the dictionary d ass it is
print(len(d)) #identify the number of key-value pairs inside dictionary d
print(type(d)) #identify the type/class of variable d
print(d.keys()) #print all the keys available in dictionary d
print(d.items()) #print all the key-value pairs of dictionary d
print(d.values()) #print all the values stored in the keys of dictionary d
print(d['age']) #fetch the value of particular key from dictionary d
print(d.get('lastname')) #fetch the value of particular key from dictionary d
d['age']=28 #update the value of particular key in dictionary d
print(d)
d.update({'firstname':'jatin'}) #update the value of particular key in dictionary d
print(d)
d['citizen']='indian' #insert a key-value pair at the last of dictionary d
print(d)
d.update({'phonenumber':'0987654321'}) #insert a key-value pair at the last of dictionary d
dc=d.copy() #copy all the key-value pairs from dictionary d to dc
print(dc)
print(d)
d.popitem() #removes the last key-value pair from the dictionary d
print(d)
d.pop('lastname') #removes the value of particular key from the dictionary d
print(d)
d.clear() #removes all the key-value pairs from the dictionary d
print(d)
del d #delete the complete dictionary d and make it as unexistable

# Dictionary Nesting/Nesting of Dictionary
dn={
    'child1':
        {'firstname':'amit',
        'lastname':'kumar'},
    'child2':
        {'firstname':'chetna',
        'lastname':'gogna'},
    'child3':
        {'firstname':'mohit',
        'lastname':'verma'},
}
print(dn['child2']['lastname']) #retrieval from nested dictionary

# If a key is not existed in dictionary then update function will insert a new key-value pair inside dictionary at the last position otherwise it will update an existing value of that particular key
