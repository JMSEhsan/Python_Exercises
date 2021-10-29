# Ref.: Head First Learn To Code
# Function returns things

def get_back(weight):
    if weight > 20:
        return 'WOOF WOOf'
    else:
        return 'woof woof'

nm = input('Enter name: ')       
wt = input('Enter the weight: ')

fn = get_back(wt)
print(nm+"'s bark is", fn)
