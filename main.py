from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)

def cesar(text, shift, direction):
    n = len(text)
    text_list = []
    for i in text:
        if i.isalpha() == True:
            index_letter = alphabet.index(i)
            if direction == 'encode':
                shifted = index_letter + shift
            elif direction == 'decode':
                shifted = index_letter - shift
            if shifted > 25:
                shifted = shifted%25-1

            shifted_letter = alphabet[shifted]
            text_list.append(shifted_letter)
        else:
            shifted_letter = i
            text_list.append(shifted_letter)
    x = ''.join(text_list)
    print(f'The encrypted text: {x}')

#TODO: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
running = True
while running == True:


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cesar(text, shift, direction)
    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if continue_program == 'yes':
        running = True
    elif continue_program == 'no':
        print('\n*Program ends* \n')
        running = False
