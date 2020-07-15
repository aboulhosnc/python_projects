
import re
#[A-Z][a-z]*(?=(.){3}yes)

print ("Enter the string to test\n")
# string = input()

# string = 'Texas = no, California = yes, Florida = yes, Michigan = no'
string = '01:32:54:67:89:AB'
print('String is : {} \n'.format(string))
print("Enter the pattern to test \n")
# pattern = input()
# pattern = 'California(?=(.){3}yes)'
# pattern = '[A-Z][a-z]*(?=\s\=\syes)'
# pattern = '(\w+)(?! = yes)'
# pattern = '[A-Z][a-z]*(?!  = no)'
# pattern = '[A-Z][a-z]*(?!\s=\syes)'
# pattern = '[A-Z][a-z]*(?!\s=\sno)'
# pattern = '[A-Z][a-z]+\\b(?! = yes)'
pattern = '([\\dA-F]{2})(:)([\\dA-F]{2})\\2([\\dA-F]{2})\\2([\\dA-F]{2})\\2([\\dA-F]{2})\\2([\\dA-F]{2})'
# pattern = '(California|Florida)'
# pattern = '[A-Z][a-z]*'
print('pattern is {}\n'.format(pattern))

result = re.findall(pattern, string)
print('Result is : {} '.format(result))
