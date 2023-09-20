# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#        position = alphabet.index(letter)
#        new_position = position + shift_amount
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')

# def decrypt(decode_text, decode_shift):
#     cipher_text = ""
#     for letter in decode_text:
#        position = alphabet.index(letter)
#        new_position = position - decode_shift
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#     print(f'The decoded text is {cipher_text}')


# run = True
# while True:

#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     if direction == "encode":
#         encrypt(plain_text=text, shift_amount=shift)
#     elif direction == "decode":
#         decrypt(decode_text=text, decode_shift=shift)
#     else:
#         print("You typed wrong, try again")
#         break

#     question = input("Do you want to run the program again? Y or N\n").lower()
#     if question == "y":
#         run = True
#     elif question == "n":
#         break
#         print("Bye")
#     else:
#         print("You typed a wrong option, Bye!")
#         break


#Another way to do it:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    