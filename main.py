def getLetterCountForBookContent(bookContent):
    word_dict = {}
    for character in list(bookContent.lower()):
        word_dict.update({character: word_dict.get(character, 0) + 1})
    return word_dict.

def getWordCountForBookContent(bookContent):
    words = bookContent.split()
    print(len(words))

def readBook(pathToBook):
    file_contents = ""
    with open(pathToBook) as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def buildBookReport(pathToBook):
    bookContent = readBook(pathToBook)
    print (f"--- Begin report of {pathToBook} ---")
    print(f"{getWordCountForBookContent(bookContent)}")

def main():
    bookContent = readBook("books/frankenstein.txt")
    getWordCountForBookContent(bookContent)
    getLetterCountForBookContent(bookContent)
    buildBookReport(pathToBook)

main()