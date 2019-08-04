# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class CaesarCipher(object):
    def __init__(self, shift):
        encoder = [str()] * 26
        decoder = [str()] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self.__forward = ''.join(encoder)
        self.__backward = ''.join(decoder)

    @staticmethod
    def __transform(original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

    def encrypt(self, message):
        return self.__transform(message, self.__forward)

    def decrypt(self, secret):
        return self.__transform(secret, self.__backward)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print("Secret:", coded)
    answer = cipher.decrypt(coded)
    print("Message:", answer)
