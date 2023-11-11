import sys
import json
import random
from os import system, name
from time import sleep
from datetime import datetime
random.seed(datetime.now().timestamp())

############################################################
#### CHANGE DESIRED DATABASE FILE DIRECTORY UNDER HERE #####
############################################################
filedir = "databases/N1_1_100_v2.json"

class KanjiDataBase:
    def __init__(self):
        self.data = {}
    
    def add_kanjiPhrase( self, kanji: str, reading: str ):
        self.data[kanji] = reading
        
    def remove_kanjiPhrase( self, kanji: str ):
        self.data.pop( kanji, "" )
    
    def save_database( self, filedir: str):
        with open( filedir, "w", encoding="utf8") as f:
            json.dump( self.data, f, ensure_ascii=False, indent=2 )
        
    def load_database( self, filedir: str):
        with open( filedir, "r", encoding="utf8") as f:
            self.data = json.load( f )
    
    def get_size( self ):
        return len( self.data )


    def test_kanjireading( self, number_to_test: int = 1 ):
        """
        This tests the user's knowledge of the kanji readings from the current kanji database.
        Args:
            number_to_test [int]: The number of kanji words/phrases to uniquely sample from the database
        Returns:
            None
        """

        #Make sure number_to_test is always less than or equal to size of current database
        if number_to_test > self.get_size():
            raise Exception("Not enough kanji in database for desired number of kanji to test. Add more kanji or lower test number requirement.")
        
        #Sample number_to_test unique kanji to test,
        test_kanji = random.sample( list(self.data.items()), number_to_test )
        
        #Prompts for the user's guesses begin here.
        print("\nTry to enter the correct reading for the following kanji.")
        for s, (kanji, readings) in enumerate(test_kanji):
            if type(readings) != list:
                readings = [readings]
            while True:
                user_reading = get_user_input_string("\t{}) {}: ".format(s+1, kanji))
                if user_reading in readings:
                    user_input = get_user_input_string("\nSorry, that's not quite right.\nWould you like to try again? 'y' or 'n': ", valid_choices=["y", "n"])
                    if user_input == "y":
                        continue
                    else:
                        print("The correct reading(s) for {} is/are: {}".format(kanji, readings))
                        print("Moving onto the next kanji.")
                        break
                else:
                    print("That's correct!")
                    break

def main():   
    #Initialise and load kanji database
    kanji_data = KanjiDataBase()
    kanji_data.load_database(filedir)
    
    clear()
    print("\nWelcome to KanjiPy! A simple Python script to learn Kanji at your own pace.")

    break_main_loop = False
    while not break_main_loop:
        print("Current Kanji Database Size: {}".format(kanji_data.get_size()))
        print("\n\tWhat would you like to do?")
        print("\t1: Add Kanji to the database")
        print("\t2: Remove Kanji from the database")
        print("\t3: Test your reading of kanji from the current database")
        print("\t4: Exit program")
        user_choice = get_user_input_number("\nEnter number here: ", valid_choices=[1,2,3,4])
        if user_choice == 1:
            while True:
                clear()
                number_of_kanji = get_user_input_number("How many kanji would you like to add: ")
                for n in range(1, number_of_kanji+1):
                    kanji_to_add = get_user_input_string("{}) What kanji would you like to add: ".format(n))
                    reading_to_add = get_user_input_string("{}) What is the reading of this kanji: ".format(n))
                    print("{}) Your kanji and reading inputs are: {} ({}) ".format(n, kanji_to_add, reading_to_add))
                    user_choice = get_user_input_string("{}) Are you sure you would like to add this to the database? Enter 'y' or 'n': ".format(n), valid_choices=["y", "n"])
                    if user_choice == "y":
                        kanji_data.add_kanjiPhrase(kanji_to_add, reading_to_add)
                    else:
                        print("Skipping this kanji.")
                try_again = get_user_input_string("Would you like to add more kanji? Enter 'y' or 'n': ", valid_choices=["y", "n"])
                if try_again == "n":
                    clear()
                    break
        elif user_choice == 2:
            while True:
                clear()
                number_of_kanji = get_user_input_number("How many kanji would you like to remove: ")
                for n in range(1, number_of_kanji+1):
                    kanji_to_remove = get_user_input_string("{}) What kanji would you like to remove: ".format(n))
                    user_choice = get_user_input_string("{}) Are you sure you would like to remove {} from the database? Enter 'y' or 'n': ".format(n), valid_choices=["y", "n"])
                    if user_choice == "y":
                        try:
                            kanji_data.remove_kanjiPhrase(kanji_to_remove)
                        except:
                            print("Nothing happened.")
                try_again = get_user_input_string("Would you like to remove more kanji? Enter 'y' or 'n': ", valid_choices=["y", "n"])
                if try_again == "n":
                    clear()
                    break
        elif user_choice == 3:
            while True:
                number_of_kanji = get_user_input_number("How many kanji would you like to test your reading on: ")
                if number_of_kanji < 0 or number_of_kanji > kanji_data.get_size():
                    print("Please pick a number between 1 and {}".format(kanji_data.get_size()))
                    continue
                else:
                    kanji_data.test_kanjireading( number_to_test=number_of_kanji)
                    try_again = get_user_input_string("Would you like to test more kanji readings? Enter 'y' or 'n': ", valid_choices=["y", "n"])
                    if try_again == "n":
                        clear()
                        break
        else:
            break_main_loop = True
            clear()
    print("Would you like to overwrite the saved database? (If you added new ones)")
    save_newdatabase = get_user_input_string( "Enter 'y' or 'n': ", valid_choices=["y", "n"] )
    if save_newdatabase:
        kanji_data.save_database(filedir)
    print("Thanks for using KanjiPy! Have a good day and good luck with your Kanji studies!")
    sleep(0.5)
                
def get_user_input_number( prompt: str, valid_choices: list = [] ):
    while True:
        try:
            user_input = int( input(prompt) )
            if user_input in valid_choices or len(valid_choices) == 0:
                return user_input
            else:
                raise Exception()
        except KeyboardInterrupt:
            sys.exit(130)
        except:
            if len(valid_choices) > 0:
                print("Please enter a valid number from {}.".format(valid_choices))
            else:
                print("Please enter a valid number.")

def get_user_input_string( prompt: str, valid_choices: list = [] ):
    while True:
        try:
            user_input = input(prompt)
            if user_input in valid_choices or len(valid_choices) == 0:
                return user_input
            else:
                raise Exception()
        except KeyboardInterrupt:
            sys.exit(130)
        except:
            if len(valid_choices) > 0:
                print("Please enter a valid answer from {}.".format(valid_choices))
            else:
                print("Please enter a valid answer.")

#Command to clear terminal for easy reading
def clear():
    if name == 'nt':
        _ = system('cls') #Windows command
    else:
        _ = system('clear') #Nux style command
    print("\nPress Ctrl+C at any time to force exit.")

if __name__ == "__main__":
    main()