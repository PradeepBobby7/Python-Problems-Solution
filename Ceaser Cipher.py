alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(start_text,shift_amt,direction1):
    if direction=='decode':
        shift_amt*=-1
    end_text=''
    for letter in start_text:
        position=alphabet.index(letter)
        new_position=shift_amt+position
        new_letter=alphabet[new_position]
        end_text+=new_letter
    print(f" The {direction}ed text is {end_text}.")
ceaser(start_text=text,shift_amt=shift,direction1=direction)