class Vigenere:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(range(65,91)):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in range(65,91):
                        alphabet.append(chr(y))
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in range(65,91):
                        letter = alphabet.popleft()
                        alphabet_dict[chr(y)] = letter
                        alphabet_dict_rev[letter] = chr(y)
                self.alphabets[chr(x)] = alphabet_dict
                self.alphabets_rev[chr(x)] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets[keyi]
                sub = sub_dict[secret[x]]
                cipher_text += sub
        return cipher_text

    def decrypt(self, secret):
        plain_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets_rev[keyi]
                sub = sub_dict[secret[x]]
                plain_text += sub
        return plain_text

class AutoKeyVigenere:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(range(65,91)):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in range(65,91):
                        alphabet.append(chr(y))
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in range(65,91):
                        letter = alphabet.popleft()
                        alphabet_dict[chr(y)] = letter
                        alphabet_dict_rev[letter] = chr(y)
                self.alphabets[chr(x)] = alphabet_dict
                self.alphabets_rev[chr(x)] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = []
        for k in range(len(secret)):
            keyi = self.key.pop(0)
            sub_dict = self.alphabets[keyi]
            sub = sub_dict[secret[k]]
            self.key.append(secret[k])
            cipher_text.append(sub)
        return "".join(cipher_text)

    def decrypt(self, secret):
        plain_text = []
        for k in range(len(secret)):
            keyi = self.key.pop(0)
            sub_dict = self.alphabets_rev[keyi]
            sub = sub_dict[secret[k]]
            plain_text.append(sub)
            self.key.append(plain_text[k])
        return "".join(plain_text)
