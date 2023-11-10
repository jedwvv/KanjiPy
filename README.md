# KanjiPy
A simple Python script to learn Kanji at your own pace.  

## Requirement:
- Python>=3.9  

## Who is this for?
- Japanese learners like me who want to extensively test their kanji reading skills (perhaps to take the JLPT exam).
- People who want to personalize a list of kanji to memorize, for example, to learn 100 new kanji words/phrases a week, or 10 kanji words/phrases a day!

Simply run the program in a console that supports utf-8 encoding. To check if your console is supported run `import sys; sys.getdefaultencoding()` in your Python shell. If it prints `'utf-8'` then this program should work.  

## To download this program and my database:
- Run: `git clone https://github.com/jedwvv/KanjiPy.git`

## To use the program:
- Run: `python kanjipy.py`  

## To change to your own personalised Kanji list:
1. Make a json text file in the folder `'databases/'`.  
2. In a dictionary format, enter your kanji entries as key, value pairs where key is the kanji, and value is its hiragana reading. 
3. In the `kanjipy.py` script, change the `filedir` variable to store the directory of your new json file (Line 12). The location is commented near the top of the script for easy access.
  
See existing `databases/` folder for examples of these text files.  
For convenience, you can also modify an existing database within the program by selecting the appropriate menu(s).  
Make sure there are no duplicate kanji words/phrases!
The main reason to make your own list would be if you want to memorize specific kanji words/phrases.

## Notes:
- I am in the process of learning the Kanji from the book:「日本語能力試験ターゲット1000 N1 漢字 」(ISBN: 4010924217). As I study the kanji (in order), I will update the uploaded kanji database, partitioning the 1000+ kanji characters into separate files.
- In the future, I plan to add the kanji characters from 「日本語能力試験ターゲット1000 N2 漢字」(ISBN: 4010924225) which I have already completely studied prior to making this python script. This is for completeness to include most of the [常用漢字/Jōyō Kanji](https://www.kanshudo.com/collections/joyo_kanji), if not all. 
- Since I am following these two books, I adopt the naming convention `N1_A_B.json` or `N2_A_B.json` for my kanji database where A and B denote the starting and ending character index from the corresponding N1 or N2 book. You may ignore these and make your own personalised database as explained above.
- Once those 2000+ N1 and N2 characters are in the database, I will compile into one whole database.


