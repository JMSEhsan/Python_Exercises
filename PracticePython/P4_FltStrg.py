# Multiplication using integer and string

input = input('Enter a number or characters to multiply by 6: ')
mltpl = input * 6

try:
    float(input)
    mltplNo = float(input) * 6
except ValueError:
    print(input+' is not a number')
    mltplNo = False
print('The answer in the form of string is:', mltpl)

if (bool(mltplNo) == True or mltplNo is not False):
    print('If a number, the answer in the form of float is: ', mltplNo)