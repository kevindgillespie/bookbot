def sort_on(dict):
    return dict["count"]

#this for sure could be better
def getLetterCountForBookContent(bookContent):
    letter_dict = {}
    letter_list = []
    for character in list(bookContent.lower()):
        letter_dict.update({character : letter_dict.get(character, 0) + 1 })
    for letter in letter_dict:
        letter_list.append({"character" : letter, "count": letter_dict.get(letter)})
    letter_list.sort(reverse=True, key=sort_on)
    for letter_entry in letter_list:
        if(letter_entry["character"].isalpha()):
            print(f"The '{letter_entry["character"]}' character was found {letter_entry["count"]} times")

def getWordCountForBookContent(bookContent):
    return len(bookContent.split())

def readBook(pathToBook):
    file_contents = ""
    with open(pathToBook) as f:
        file_contents = f.read()
    return file_contents

def buildBookReport(pathToBook):
    bookContent = readBook(pathToBook)
    print (f"--- Begin report of {pathToBook} ---")
    print(f"{getWordCountForBookContent(bookContent)} words found in the document")
    print("")
    getLetterCountForBookContent(bookContent)
    print("--- End Report ---")

def main():
    pathToBook = "books/frankenstein.txt"
    buildBookReport(pathToBook)

main()
