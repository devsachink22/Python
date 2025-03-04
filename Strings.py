s="This is my python code." #declaration of variable s with static string
print(s) #fetches the data stored in variable s
print(type(s)) #identifies the type/class of data stored in variable s
print(len(s)) #identifies the number of elements stores in string s
print(s*3) #print the data stored in string s for 3 times which can also be n number of times

# String Indexing
print(s[0]) #print the first character of string s
print(s[-1]) # print the last character of string s
print(s[3]) #print the 4th character of string s

# String Slicing or Slicing a string
print(s[1:7]) #print all the characters of string s from 1st index value to 6th index value & not includes the character of 7th index value
print(s[1:]) #print all the characters of string s from 1st index value
print(s[:-4]) #print all the characters of string s before the last 4th character
print(s[6:-1]) #print all the characters of string s from 6th index value to the last 2nd character

# String Slicing Steps or Steps in string slicing
print(s[1:19:3]) #print all the characters of string s from 1st index value to 18th index value with jumping 2 steps each and not includes the character of 19th index value
print(s[-17:-3:4]) #print all the characters of string s that ranges from the last 17th character to the last 4th character with jumping 3 steps each and not includes the last 3rd character 

print(s[::-1]) #reverse a string s
print(s.find('is')) #find the index value of first occurence of 'is' word/letter in string s
print(s.count('h')) #find the number of 'h' character/word in string s
print(s.replace('python','java')) #replace word/letter 'python' with 'java' in string s
print(s.lower()) #convert all the letters/words in string s to lower case
print(s.upper()) #convert all the letters/words in string s to upper case
print(s.capitalize()) #convert the first letter of first word in string s to upper case
print(s.title()) #convert the first letter of all the words in string s to upper case

# In Function
print('sachin' in s) #checks whether a word/letter 'sachin' is present in string s
print('code' in s) #checks whether a word/letter 'code' is present in string s

s2='It is an interpreter language.'
print(s+s2) #concatination of s & s2 strings to merge all the characters.

# Strip Function
print(s.strip()) #removes empty spaces from the left & right of the string s
print(s.lstrip()) #removes empty spaces from the left of the string s
print(s.rstrip()) #removes empty spaces from the right of the string s
print(s.strip('Th')) #removes letter/word 'Th' from the left & right of the string s
