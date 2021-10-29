# Ref.: Head First Learn To Code
# Function returns things

def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOf'
    else:
        return 'woof woof'

dogName = input('Enter name: ')       
wt = int(input('Enter the weight: '))

dogBark = get_bark(wt)
print(dogName+"'s bark is", dogBark)
