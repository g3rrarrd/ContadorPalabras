import fileManager 

if __name__ == "__main__":
    fm = fileManager.fileManager("textCount.txt", 0)
    fm.file_creator()

    print("Que es lo que estas pensando?\n")
    text = input()

    fm.file_writer(text)

    print("Me has demostrado tus pensamientos en %d palabras \n" % fm.words_counter())
    print("Cantidad de letras usadas: %s" % fm.letter_counter())
