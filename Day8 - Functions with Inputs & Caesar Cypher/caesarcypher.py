alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = 'Welcome to the Caesar Cypher, type ENCODE or DECODE to start'

print(message)

exitCypher = False

def stringify(input_list):
    stringified_list = ''.join(input_list)
    return stringified_list

def encode(text, shift):
    listified_text = list(text)

    shifted_positions = []
    shifted_letters = []
    unshifted_positions = []

    for i in range(len(listified_text)):
        #this is where the magic happens
        shifted_position = (alphabet.index(listified_text[i]) + shift) % 26
        shifted_positions.append(shifted_position)

        unshifted_position = shifted_position - shift
        unshifted_positions.append(unshifted_position)

    for i in range(len(shifted_positions)):
        letter = alphabet[shifted_positions[i]]
        shifted_letters.append(letter)

    print(stringify(shifted_letters))

def decode(text, shift):

    listified_text = list(text)
    shifted_positions = []
    shifted_letters = []
    unshifted_positions = []
    unshifted_letters = []

    for i in range(len(listified_text)):
        shifted_position = (alphabet.index(listified_text[i]) - shift ) % 26
        shifted_positions.append(shifted_position)

        # unshifted version
        unshifted_position = shifted_position
        unshifted_positions.append(unshifted_position)

    for i in range(len(shifted_positions)):
        letter = alphabet[shifted_positions[i]]
        shifted_letters.append(letter)

        # unshifted version
        unshifted_letter = alphabet[unshifted_positions[i]]
        unshifted_letters.append(unshifted_letter)

    print(stringify(unshifted_letters))


while not exitCypher:

    direction = input()

    if direction == 'encode':
        print('Write the text you want to encode')
        text_to_encode = input()
        print('Give the shift of the encoding')
        encoding_shift = int(input())

        encode(text_to_encode, encoding_shift)

    elif direction == 'decode':
        print('Write the encoded text you want to decode')
        text_to_decode = input()
        print('Give the shift of the encoding')
        encoding_shift = int(input())

        decode(text_to_decode, encoding_shift)

    print('If you want to exit the Cypher, type exit, if you want to continue, type continue')

    user_input = input()
    if user_input == 'exit':
        exitCypher = True
    elif user_input == 'continue':
        print(message)

