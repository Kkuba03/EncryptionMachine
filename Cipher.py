import random
x = ["abcdefghijklłmnoprstuwyzqxv?.<>,!1:234567890/*-+()'!@#$%^&=;' "]
signs = []
for sign in x:
    for s in sign:
        s = str(s)
        signs.append(s)
def encryption_machine(A):
    A = str(A)
    A = A.lower()
    instruction = {}
    for sign in signs:
        randsign = random.choice(signs)
        while randsign in instruction.values():
            randsign = random.choice(signs)
        instruction[sign] = randsign
    print(instruction)
    result = ""
    for letter in A: 
        letter = instruction.get(letter)
        result += str(letter)
    A = result

    return A
print(encryption_machine('Jan paweł 2'))
        






