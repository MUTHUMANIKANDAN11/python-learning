def encode(text, shift):
    encode_text = ""
    for chr in text:
        if chr in alphabets:
            ind = alphabets.index(chr)
            chr = alphabets[(ind + shift) % 26]
        encode_text += chr
    print(f"The encoded text is {encode_text}")

def decode(text, shift):
    decode_text = ""
    for chr in text:
        if chr in alphabets:
            ind = alphabets.index(chr)
            chr = alphabets[(ind - shift) % 26]
        decode_text += chr
    print(f"The decoded text is {decode_text}")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("\nType your message: ").lower()
shift = int(input("\nType the shift number: "))

if direction == "encode":
    encode(text, shift)

elif direction == "decode":
    decode(text, shift)
    