import PyPDF2
import sys
import re
import os.path
from Book import *

books_pdflist = ["books\\" + f for f in os.listdir('books') if re.search(r'\.pdf$', f)]

books=[]
for bookPath in books_pdflist:
    book = Book(bookPath)
    books.append(book)    


word="Harry"
max_match_count=0
for book in books:
    book.search_for_word(word,200)
    if (len(book.words[word]) != 0):
        book.print_book_name(len(book.words[word]))  

print("#######################\n")    
for book in books:
    if (len(book.words[word]) == 0):
        continue
    book.print_book_name()
    counter=max_match_count
    for matches in book.words[word]: 
        counter-=1
        print("\n" + matches + "\n")
        if counter==0:
            break


          

