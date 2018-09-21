# AEADHandCiphers

This module was constructed to provide authentication with additional data for the RedDye H4 cipher (still unbroken) and the classic Vigenere Cipher.  Additional ciphers may be added.

Authentication is essentially a way of ensuring that only the receiver is able to decrypt the message and that the data is in no way tampered with in transit.  Each message authentication code generated by getting the sum of all bytes, evenly summing them into the MAC array and then encrypting the MAC with the cipher.  Each authentication scheme relies on the strength of the individual cipher.

# Usage:

from AEADHandCiphers import AEAD_H4

aead_h4 = AEAD_H4(maclen=8)  #  8 by default

aead_h4.encrypt(data, key, optional_ad)

aead_h4.decrypt(data, key, optional_length_of_ad)

from AEADHandCiphers import AEAD_Vigenere

aead_vi = AEAD_Vigenere(maclen=8)  # 8 by default

aead_vi.encrypt(data, key, optional_ad)

aead_vi.decrypt(data, key, optional_length_of_ad)