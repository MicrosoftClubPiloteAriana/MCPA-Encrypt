# MCPA-Encrypt

This is a simple GUI application built using tkinter in Python. It allows users to encrypt and decrypt text messages using a custom encryption algorithm.

## Features

- Encrypt text messages using a custom encryption algorithm.
- Decrypt encrypted messages to retrieve the original text.
- User-friendly graphical interface.

## Installation

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/MicrosoftClubPiloteAriana/MCPA-Encrypt.git
   ```

3. Install the required dependencies:

   ```bash
   pip install tkinter
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Enter the text you want to encrypt or decrypt into the text input area.
2. Click the "Encrypt" button to encrypt the entered text.
3. Click the "Decrypt" button to decrypt an encrypted message.
4. The encrypted or decrypted text will be displayed in the text input area.

## Custom Encryption Algorithm

The encryption algorithm used in this application involves the following steps:

1. Convert characters of the text to their ASCII codes.
2. Add random characters to the ASCII codes.
3. Replace some ASCII codes with a symbol.
4. Append a key to the encrypted message to aid decryption.

## Credits
Mohamed Nasraoui,
Baha Aouadi
