#Strings


from typing import type_check_only


first_name = 'Dennis \n'
print ()
last_name = 'Micheal'
#String Here !
print (first_name + last_name)

#To combine strings we use the (+) sign so as to combine them together. This is'String Concatenation'.

sentence = 'The quick brown fox jumps over the lazy dog.'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))


#Input of First and Last name variables to make strings
print(input(first_name + last_name))
print (input('What is your first Name?'))
print (input ('How are you?'))
print (input('What is your last name?'))

print ( 'Bonjour ' + first_name.capitalize() + ' ' +last_name.capitalize())

school_name ='Strathmore'

print (input(school_name))
print (input('Where do you go to school?  ' + first_name + ' ' + last_name))


#Format Strings
# {} is used to specify the parameters
# E.G. [output = 'Hello, {} {}'.format (first_name + last_name)] 

first_name = 'James'
last_name = 'Peter'

#Output 
output = 'Hello ' + last_name + first_name
print (output)


#Output with curly brackets
#The curly brackets assist with the order of variables. The variables number always starts from 0 going up
output = 'Hello, {} {}'.format (first_name, last_name)
output = 'Hello, {0} {1}'.format (first_name, last_name)
output = f'Hello, {first_name}  {last_name}'

print (output)


weather = input('The weather is quite cloudy and cold today')

if weather = True
    else: 'Include comment'
finally = type_check_only

