
def count(text):
    words = text.split()
    print(len(words))
    return words

def readtext(path):
    with open(path,'r') as f :
        file_contents = f.read();
        return file_contents

def countletters(words):
   countLetterDict = {};
   for i in words: 
    for j in i : 
       lowerJ =j.lower()
       if(lowerJ.isalpha()):
         countLetterDict[lowerJ] = 1+ countLetterDict.get(lowerJ,0);
   return countLetterDict;

def sort_on(dict):
    return dict['num']
   
def sortingDict(countLetterDict):
    orderDict = []
    for item,value in countLetterDict.items():
         orderDict.append({"character":item,"num":value});
    orderDict.sort(reverse=True, key = sort_on)
    return orderDict

def main():
 path = "books/frankenstein.txt"
 text =readtext(path)
 words=count(text)
 countLetterDict =countletters(words)
 orderDict  =sortingDict(countLetterDict)

 
 print(f"--- Begin report of {path} ---")
 print(f"{len(words)} words found in the document")
 print()

 for item in orderDict:
    if not item["character"].isalpha():
        continue
    print(f"The '{item['character']}' character was found {item['num']} times")

 print("--- End report ---")


 


if __name__ == '__main__':
    main()