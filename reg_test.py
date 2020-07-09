
import re
#[A-Z][a-z]*(?=(.){3}yes)

print ("Enter the string to test\n")
# string = input()

string = 'Texas = no, California = yes, Florida = yes, Michigan = no'
print('String is : {} \n'.format(string))
print("Enter the pattern to test \n")
# pattern = input()
# pattern = 'California(?=(.){3}yes)'
pattern = '(California|Florida)'
print('pattern is {}\n'.format(pattern))

result = re.findall(pattern, string)
print('Result is : {} '.format(result))
