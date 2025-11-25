Data Security Using Cryptography and Steganography

🔒 Project Overview

  This project implements a dual-layer security system for secure data transmission. It combines Audio Steganography with strong Cryptography techniques to ensure that sensitive information is not only hidden but also scrambled, making detection and unauthorized access extremely difficult.

  The system works by first embedding secret text data into a carrier audio file (.wav) using the Least Significant Bit (LSB) steganography algorithm. The resulting "stego-audio" file is then encrypted using either Triple DES (TDES) or Fernet algorithms, rendering the audio file unplayable and unreadable until decrypted.

🚀 Key Features

  Audio Steganography: Hides secret text messages inside .wav audio files using LSB encoding without significantly altering the audio quality.

  Triple DES Encryption: Implements the Triple Data Encryption Standard (3DES) to encrypt the stego-audio file.

  Fernet Encryption: Provides an alternative symmetric encryption method using the Fernet (AES-based) implementation.

  Data Integrity: Ensures the hidden message can be retrieved exactly as it was sent after decryption.

  Two-Layer Protection: Even if the encryption is broken, the attacker still needs to detect and decode the steganography.

🛠️ Methodology

  The project follows a specific workflow to secure data:

   1. Encoding (Sender)

    Steganography: The secret text is converted into binary. The LSB of the audio frame bytes is replaced with the message bits.

    Encryption: The modified audio file (containing the hidden text) is encrypted using a symmetric key (TDES or Fernet).

    Output: An encrypted file that looks like random noise and cannot be played as audio.

  2. Decoding (Receiver)

    Decryption: The receiver uses the shared key to decrypt the file, restoring it to a playable .wav audio file.

    Steganography Extraction: The application reads the LSBs of the audio frames to reconstruct the hidden text message.

📦 Installation & Requirements

  Ensure you have Python 3.x installed. You will need the following external libraries:

    pip install pycryptodome cryptography


    pycryptodome: Required for Triple DES implementation.

    cryptography: Required for Fernet implementation.

    wave: Standard Python library for audio manipulation.

💻 Usage

  The project consists of two main scripts corresponding to the two encryption methods.

    Option 1: Using Triple DES (DES.py)

    Run the script:

    python DES.py


  Encode:

    Select Option 1.

    Enter the TDES Key (must be robust).

    Enter the text you wish to hide.

    The script generates an encrypted Audio_1.wav.

  Decode:

    Select Option 2.

    Enter the same TDES Key.
  
    The script decrypts the audio and extracts the hidden message.

    Option 2: Using Fernet (Ferrnet.py)

    Run the script:

    python Ferrnet.py


  Encode:

    Select Option 1.

    The script automatically generates a key (filekey.key) and encrypts the audio after hiding the text.

  Decode:

    Select Option 2.

    The script reads filekey.key to decrypt the audio and prints the hidden message.

Note: Ensure you have a source audio file (e.g., audiocheck.net_pinknoise.wav) in the correct path or update the path in the code before running.

👥 Contributors

  This project was developed as part of the Bachelor's Degree in Information Technology requirements at KIIT Deemed to be University.

    Rahul Bagaria (2129140)


⚠️ Disclaimer

This tool is intended for educational and research purposes only. Please use responsibly.
