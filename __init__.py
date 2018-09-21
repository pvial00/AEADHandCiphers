from vigenere import Vigenere
from h4a import H4A
from h4 import H4

class AEAD_H4:
    def __init__(self, maclen=8):
        self.maclen = maclen
        self.mac = H4A(maclen)

    def encrypt(self, data, key, ad=""):
        data = H4().encrypt(data, key)
        mac = self.mac.mac(data, key, ad)
        return mac+data

    def decrypt(self, data, key, adlen=0):
        ad = data[:adlen]
        m = data[adlen:adlen+self.maclen]
        msg = data[adlen+self.maclen:]
        if self.mac.verify(msg, key, m, ad) == True:
            return H4().decrypt(msg, key)
        else:
            raise ValueError('Message has been tampered with.')
        

class AEAD_Vigenere:
    def __init__(self, maclen=8):
        self.maclen = maclen
        self.mac = H4A(maclen)

    def encrypt(self, data, key, ad=""):
        data = Vigenere(key).encrypt(data)
        mac = self.mac.mac(data, key, ad)
        return mac+data

    def decrypt(self, data, key, adlen=0):
        ad = data[:adlen]
        m = data[adlen:adlen+self.maclen]
        msg = data[adlen+self.maclen:]
        if self.mac.verify(msg, key, m, ad) == True:
            return Vigenere(key).decrypt(msg)
        else:
            raise ValueError('Message has been tampered with.')
        
