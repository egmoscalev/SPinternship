"""
Задание является не обязательным, но его выполнение поможет лучше
ознакомиться с итераторами.
Реализовать класс BlockTranspositionCipher, который будет шифровать и
расшифровывать текст методом блочной перестановки с помощью текстового
ключа.
Основная идея:
1. Ключ — строка, состоящая из уникальных английских букв. Пример:
acb
2. Шифрование — алгоритм, который преобразует исходный текст в
набор зашифрованных символов.
3. Дешифрование — алгоритм, который преобразует набор
зашифрованных символов в исходный текст.
14Ключ и его обработка:
• ключ состоит только из букв английского алфавита
• символы в ключе должны быть уникальны (регистр букв не имеет
значения — "A" и "a" считаются одинаковыми)
• ключ преобразуется в числовой массив. Каждому символу
присваивается его порядковый номер в алфавите (a = 0, b = 1, ..., z =
25)
Правила шифрования:
• исходный текст делится на блоки длины, равной длине ключа
• если длина блока не кратна длине ключа, то оставшийся блок
дополняется пробелами
• в каждом из блоков символы переставляются согласно порядку из
ключа
Пример алгоритма шифрования:
Ключ: "acb"
Текст: "helloworld"
Блоки: ["hel", "low", "orl", "d "]
Блоки после перестановки: ["hle", "lwo", "olr", "d
Результат: "hlelwoolrd "
"]
Правила дешифрование:
• исходный порядок восстанавливает символы в каждом блоке
• лишние пробелы после дешифровки удаляются
Валидации и работа с ошибками:
• проверяется, что ключ состоит только из букв английского алфавита 
• проверяется, что все буквы в ключе уникальны, игнорируя регистр
• если ключ не соответствует требованиям, вызывается исключение
ValueError с понятным сообщением об ошибке
"""

def allCharsUnique(string):
    
    dictionary = {}

    for i in string:
        dictionary.setdefault(i,0)
        dictionary[i] += 1
        if dictionary[i] > 1:
            return False
    
    return True

def isEnglish(string):

    for i in string:
        n = ord(i)
        if not (n >= 97 and n <= 122):#lowercase
            return False
    
    return True


class BlockTranspositionCipher:

    def __init__(self,plaintxt,key, decrypt = False):

        self.decrypt = decrypt
        self.keylen = len(key)
        self.set_plaintxt(plaintxt)
        self.n = len(self.plaintxt) // self.keylen #сколько блоков
        self.set_key(key)
        self.current = 0

    def set_key(self, key):
        if not isinstance(key,str):
            raise ValueError('Key should be a string')
        
        key = key.lower()
        
        if not allCharsUnique(key):
            raise ValueError('All key characters should be unique')

        if not isEnglish(key):
            raise ValueError('All key characters should be English')
        

        mylist = [ord(i) - 97 for i in key]


        sortedlist = sorted(mylist)
        d = {value: key for key, value in enumerate(sortedlist)} #{key: value for key, value in zip(keys, values)}
        newlist = [d[i] for i in mylist]
        dictionary = {key: value for key, value in enumerate(newlist)}
        #'в каждом из блоков символы переставляются 
        #согласно порядку из ключа' я понял так:
        # 1 узнать как надо переставить символы в ключе, чтобы они были в алфавитном порядке
        # 2 переставить символы в блоке так же

        if self.decrypt:

            self.key = {value: key for key, value in dictionary.items()}#swaps keys and values
            return
        
        self.key = dictionary

    def set_plaintxt(self, plaintxt):

        while (len(plaintxt) % self.keylen != 0):
            plaintxt += ' '

        print(plaintxt)
        self.plaintxt = plaintxt

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < self.n:

            result = ''
            i = 0
            while i < self.keylen:
                idx = self.key[i] + self.current * self.keylen
                result += ''.join(self.plaintxt[idx])
                i +=1  

            self.current += 1

            if self.decrypt:
                result = result.replace(' ','')
            return result
        
        else:
            raise StopIteration
        

#Пример 1: Шифрование с явной итерацией по блокам

text = "HELLOWORLD"
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

#15Пример 2: Полное шифрование

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

#Пример 3: Дешифрование с итерацией

print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")

#Пример 4: Полное дешифрование с обрезкой пробелов

decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")