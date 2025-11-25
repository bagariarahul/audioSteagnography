import wave
from Crypto.Cipher import DES3
from hashlib import md5
key = input("Enter TDES Key : ")
key_hash = md5(key.encode('ascii')).digest() 
tdes_key = DES3.adjust_key_parity(key_hash)
cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
def case(a):
    if a == 1:
        encode()
    elif a == 2:
        decode()
    elif a == 3:
        quit()
    else:
        print("\nEnter valid Choice!")

def encode():
    print("\nEncoding Starts..")
    audio = wave.open(r"C:\Users\audiocheck.net_pinknoise.wav", mode="rb") #Path
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    string = str(input("Enter Text to be Incription : "))
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    for i in range(0, 10):
        print(frame_bytes[i])
    newAudio = wave.open('Audio_1.wav', 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)
    newAudio.close()
    audio.close()
    print(" |----> Successfully encoded text inside Audio_1.wav using Steganography ")
    print("Applying Triple DES Encryption on Audio 1 file ")
    with open('Audio_1.wav', 'rb') as input_file:
        file_bytes = input_file.read()
    encrypted = cipher.encrypt(file_bytes)
    with open('Audio_1.wav', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("Audio file encrypted with DES3 Algorithm Successful ")

def decode():
    print("Audio file decryption with DES3 Algorithm Successful ")
    key = input("Enter TDES Key: ")
    key_hash = md5(key.encode('ascii')).digest() # 16-byte key
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
    
    with open('Audio_1.wav', 'rb') as input_file:
        file_bytes = input_file.read()
    
    decrypted = cipher.decrypt(file_bytes)
    
    with open('Audio_1.wav', 'wb') as dec_file:
        dec_file.write(decrypted)
    
    print("Audio file decrypted with DES3 Algorithm")
    print("\nDecoding Starts.. Steganography ")
    
    audio = wave.open("Audio_1.wav", mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("###")[0]
    print("Successfully decoded:", decoded)
    audio.close()


def main():
    while True:
        print("\nSelect an option:\n1) Encode\n2) Decode\n3) Exit")
        choice = input("\nChoice: ")
        if choice == '1':
            encode()
        elif choice == '2':
            decode()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
