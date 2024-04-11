from art import caesar_cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

should_continue = True


def caesar(start_text, shift_amount, cipher_direction):
    """
    This function encrypt or decrypt any text the user has chosen . then display it one the screen
    :param start_text:
    :param shift_amount:
    :param cipher_direction:
    :return: None
    """
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            idx = alphabet.index(char) + shift_amount
            end_text += alphabet[idx]
        else:
            end_text += char
    print(f"Here is the {cipher_direction}d result: {end_text}")


print(caesar_cipher)
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(text, shift, direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if go_again == 'no':
        should_continue = False
        print("Goodbye")
