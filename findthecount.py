#finding the number of words in the sentence,repeated words ,and finding total number of words without repeating words
mySentence=raw_input('enter the sentence: ')
input=raw_input('enter the word: ')
count=0
myWordCounter = 0
myTempWord=''
total=''
for myletter in mySentence:
    if myletter==' ':
        count=count+1
        if myTempWord==input:
          myWordCounter = myWordCounter + 1
        myTempWord='' 
        
    else:
        myTempWord = myTempWord+ myletter
        total=count-myWordCounter
print 'Total repeat count' , myWordCounter
print 'total number of the word ',count  
print 'total words without common words',total  

        
