import PyPDF2
import re
import os
from os.path import basename

class Book:
    def __init__(self, filePath):
        self.filePathPDF = filePath
        self.filePathTxt = (re.sub("\.pdf$",".txt",self.filePathPDF))
        self.BookName    = re.search("\\\(.*?)\.\w+$",self.filePathPDF).group(1)
        if os.path.isfile(self.filePathTxt):
            pass
        else:
            self.pdf_to_txt()
        self.get_content()
        self.words={}


    def search_for_word(self,word,characters_to_show=100):
        pattern=re.compile("((.{," + str(characters_to_show) + "})(" + word+ ")(.{," + str(characters_to_show) + "}))",re.DOTALL|re.IGNORECASE)
        #pattern=re.compile("((?<=CHAPTER).*?(.{,100}?)(" + word+ ")(.{,100}))",re.DOTALL|re.IGNORECASE)
        #pattern=re.compile("(?<=CHAPTER).*?((.{,100}?)(" + word+ ")(.{,100}))",re.DOTALL|re.IGNORECASE)
        #re.compile((C\s*H\s*A\s*P\s*T\s*E\s*R\s*))
        
        matches=re.finditer(pattern,self.content)
        matches_edited=[]
        for match in matches:     
            matches_edited.append(self.edit_match(match.group(2), match.group(3), match.group(4)))
        self.words[word]=matches_edited   
        
        
    def edit_match(self, before,word,after):
        return re.sub("\n","",before) + self.make_violet(word) + re.sub("\n","",after)

    def print_result(self, before,word,after):
        print(re.sub("\n","",before) + self.make_violet(word) + re.sub("\n","",after))

    def make_violet(self,text):
        return "\x1b[35m" + text + "\x1b[0m"

    def print_book_name(self, matches_found=None):
        if matches_found:
            print(self.make_violet("##########################\n" + "# " + self.BookName + "\t:\t" + str(matches_found) + " matches found\n##########################\n"))
        else:
            print(self.make_violet("##########################\n" + "# " + self.BookName + "\n##########################\n"))               
                                   
    def get_content(self):
        file = open(self.filePathTxt,"r")    
        self.content=file.read()
        file.close()

    
    def pdf_to_txt(self):
        try:
            pdf_file = open(self.filePathPDF, 'rb')
        except Exception as E:
            print("Can't find file: " + self.filePathPDF)
            print(E)
            return 0
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        all_text=""
        for page_num in range(number_of_pages):
            page = read_pdf.getPage(page_num)
            try:
                page_content = page.extractText()
            except:
                pass
            all_text+=page_content
            print(page_num)
        file = open(self.filePathTxt,"w")
        try:
            file.write(all_text.encode('ascii', 'ignore').decode('ascii'))   
        except Exception as E:
            print("Can't write in file")
            print(E)
            file.close()
        file.close()     
        
        
    def get_name(self):
        return self.BookName