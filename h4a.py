from h4 import H4

class H4A:
    cipher = H4()
    def __init__(self, blocksize=8):
        self.blocksize = blocksize

    def convtochar(self, nums):
        s = []
        for num in nums:
            s.append(chr(num + 65))
        return "".join(s)

    def sum(self, data):
        h = [0] * self.blocksize
        c = 0
        for char in data:
            h[c] = (h[c] + (ord(char) - 65)) % 26
            c = (c + 1) % self.blocksize
        return h

    def mac(self, data, key, ad=""):
        if len(data) < self.blocksize:
            for x in range((self.blocksize - len(data))):
                data += "A"
        key2 = self.cipher.kdf(key)
        h = self.sum(ad+data)
        m = self.convtochar(h)
        print m
        m = self.cipher.encrypt(m, key2)
        print m
        return ad+m

    def verify(self, data, key, mac, ad=""):
        m = self.mac(ad+data, key)
        if m == mac:
            return True
        else:
            return False
