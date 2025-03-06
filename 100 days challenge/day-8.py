import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceaser(original_text,shift_amount,en_de):
    final=""
    for i in original_text:
        if i not in alphabet:
            final+=i
        else:
            if en_de=="decode":
                shift_amount*=-1
            a=alphabet.index(i)+shift_amount
            a%=len(alphabet)
            final+=alphabet[a]
    print(f"Here is the {en_de}d result: {final}")
    next=input("Type 'yes' if you want to go again or type 'no'.\n").lower()
    while next!="no":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(text,shift,direction)
ceaser(text,shift,direction) 
print("Goodbye.")