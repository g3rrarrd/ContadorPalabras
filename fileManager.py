class fileManager:

    def __init__(self, namefile, counter):
        self.__namefile = namefile
        self.__counter = counter

    def file_creator(self):
        try:
            file = open(self.__namefile, 'w')
            file.close()
        except FileExistsError as fee:
            print(fee)

    def file_writer(self, text):
        try:
            file = open(self.__namefile, 'w')
            file.write(text)
            file.close()
        except FileNotFoundError as fee:
            print(fee)
        except FileExistsError as fe:
            print(fe)

    def words_counter(self):
        try:
            file = open(self.__namefile, 'r')            
            f = file.readline()
            f = f.split(" ")
            self.__counter = len(f)
            file.close()
            return self.__counter
        except FileNotFoundError as fee:
            print(fee)

    def letter_counter(self):
        try:
            counter = {}
            file = open(self.__namefile, 'r')
            for line in file:
                for char in line:
                    char = char.lower()
                    if (char in counter):
                        counter[char] += 1
                    else:
                        counter[char] = 1
            file.close()
        except Exception as e:
            print(e)
        return counter
    
