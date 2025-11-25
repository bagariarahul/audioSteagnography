import wave
# import required module
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

def case(a):
    if a == 1:
        encode()
    elif a == 2:
        decode()
    elif a == 3:
        quit()
    else:
        print("\nEnter valid Choice!")

from cryptography.fernet import Fernet
import wave

def encode():
    print("\nEncoding Starts..")
    
    audio = wave.open(r"C:\Users\Downloads\audiocheck.net_pinknoise.wav", mode="rb") #Path
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    string = str(input("Enter Text to be Encrypted : "))
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
    print(" |----> Successfully encoded inside Audio_1.wav")
    print("Applying Fernet Algorithm to Encrypt Audio 1 file ")
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)
    # opening the original file to encrypt
    with open('Audio_1.wav', 'rb') as file:
        original = file.read()
    # encrypting the file
    encrypted = fernet.encrypt(original)
    # opening the file in write mode and
    # writing the encrypted data
    with open('Audio_1.wav', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("Audio file encrypted with Fernet Algorithm Successful ")

def decode():
    print("Audio file decryption with Fernet Algorithm Starts:")
    
    # using the key
    fernet = Fernet(key)
    
    # opening the encrypted file
    with open('Audio_1.wav', 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    
    # opening the file in write mode and writing the decrypted data
    with open('Audio_1.wav', 'wb') as dec_file:
        dec_file.write(decrypted)
    
    print("Audio file decryption with Fernet Algorithm Successful")
    print("\nDecoding Starts: Steganography ")
    
    audio = wave.open("Audio_1.wav", mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("###")[0]
    print("Successfully decoded: "+decoded)
    audio.close()
    
def main():
     while (1):
        print("\nSelect an option: \n1)Encode\n2)Decode\n3)exit")
        val = int(input("\nChoice:"))
        case(val)
if __name__ == "__main__":
    main()
