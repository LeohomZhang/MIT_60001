# Problem Set 2, hangman.py
# Name: Hongda Zhang (MIT engineering student)
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def noguess(guesses_remaining):
    if guesses_remaining <0:
        return False
    else:
        return True

def unique(string):
    lis=list(string)
    count=0
    for i in string:
        if i in lis:
            lis.remove(i)
            count+=1
    return count

def uniqueletter(string):
    lis=[]
    for i in string:
        if i not in lis:
            lis.append(i)
    return lis
        


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    for m in secret_word:
        return m in letters_guessed
     


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    L1=list(secret_word)
    L2=L1[:]
    for m,i in enumerate(L2):
        if i not in letters_guessed:
            L1[m]='_ '
    L3=''.join(L1)
    return L3
        
    
            
        

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s=list(string.ascii_lowercase)
    for m in letters_guessed:
        if m in s:
            s.remove(m)

    s3=''.join(s)
    return s3
          
                
    
    
   

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_number = 3
    guesses_number =6
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('you have',warnings_number,'warnings left')
    print('- - - - - - - - - - - - -')
    print('you have',guesses_number,'guesses left')
    print('Available letters: abcdefghijklmnopqrstuvwxyz')
    letters_guessed=[]
    letters_wrong=[]
    check=True
    guesses_remaining=guesses_number
    warnings_remaining=warnings_number
    while check:
        #guesses_remaining=guesses_number
        #warnings_remaining=warnings_number
        print('guesses_remaining',guesses_remaining)
       
        #check if warning>0
        if warnings_number >=0:
            print('warnings_remaining',warnings_number)
        lg=input('Please guess a letter: ')
        lglow=lg.lower()
        # user inputs invalid type and loses one warning
        if lg.isalpha() is False:
            warnings_number-=1
            if warnings_number>=0:
                print('Oops! That is not a valid letter. You have',warnings_number,'warnings left:',get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining-=1
            check=noguess(guesses_remaining)
        
        #duplicated guess
        elif lglow in letters_guessed:
            warnings_number-=1
            if warnings_number>=0:
                print('Oops! That is not a valid letter. You have',warnings_number,'warnings left:',get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining-=1
            check=noguess(guesses_remaining)
        
        #User get the correct letter
        elif lglow in list(secret_word) and lglow not in letters_guessed:
            letters_guessed.append(lglow)
            print('Good guess!',get_guessed_word(secret_word, letters_guessed))
            print('- - - - - - - - - - - - - ')
            #guesses_number -=1
            print('You have',guesses_remaining,'guesses left')
            print('Available letters:',get_available_letters(letters_guessed))
        
        #incorrect guess   
        elif lglow not in list(secret_word):
            letters_wrong.append(lglow)
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
            print('- - - - - - - - - - - - - ')
            guesses_remaining -=1
            print('You have',guesses_remaining,'guesses left')
            print('Available letters:',get_available_letters(letters_guessed))
            check=noguess(guesses_remaining)
        
        lis=sorted(uniqueletter(secret_word))
        print("lis",lis)
        letters_guessed=sorted(letters_guessed)
        print("letter",letters_guessed)
        if lis == letters_guessed:
            print('Congrats! You won!')
            return "Your total score for this game is: "+ str(unique(secret_word)*guesses_remaining)

    
    return "Sorry, you ran out of guesses. The word was " + str(secret_word)
 
    
#secret_word = choose_word(load_words())
#print(hangman(secret_word))


            
    
    
#str.isal

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

#help(str.isalpha)
# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #my_word=my_word.strip(" ")
    check2=True
    if len(my_word)==len(other_word):
        for i in range(len(my_word)):
            if my_word[i]=="_":
                pass
            elif not my_word[i] == other_word[i]:
                check2=False
    else:
        return False
    return check2
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word=my_word.replace(" ","")
    lis=[]
    for i in wordlist:
        check=match_with_gaps(my_word,i)
        if check:
            lis.append(i)
    if len(lis)>0:
        return lis
    else:
        return "No matches found"

#myword="a_ i_ "
#res=show_possible_matches(myword)     

#print(res)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_number = 3
    guesses_number =6
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('you have',warnings_number,'warnings left')
    print('- - - - - - - - - - - - -')
    print('you have',guesses_number,'guesses left')
    print('Available letters: abcdefghijklmnopqrstuvwxyz')
    letters_guessed=[]
    letters_wrong=[]
    check=True
    guesses_remaining=guesses_number
    warnings_remaining=warnings_number
    while check:
        #guesses_remaining=guesses_number
        #warnings_remaining=warnings_number
        print('guesses_remaining',guesses_remaining)
       
        #check if warning>0
        if warnings_number >=0:
            print('warnings_remaining',warnings_number)
        lg=input('Please guess a letter: ')
        lglow=lg.lower()
        # user inputs invalid type and loses one warning
        if lg.isalpha() is False:
            warnings_number-=1
            if warnings_number>=0:
                print('Oops! That is not a valid letter. You have',warnings_number,'warnings left:',get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining-=1
            check=noguess(guesses_remaining)
        #print("test:lg",lg)
        #print("test:my_word",get_guessed_word(secret_word, letters_guessed))
        if lg == "*":
            my_word= get_guessed_word(secret_word, letters_guessed)
            print(my_word)
            print(show_possible_matches(my_word))
        
        #duplicated guess
        elif lglow in letters_guessed:
            warnings_number-=1
            if warnings_number>=0:
                print('Oops! That is not a valid letter. You have',warnings_number,'warnings left:',get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining-=1
            check=noguess(guesses_remaining)
        
        #User get the correct letter
        elif lglow in list(secret_word) and lglow not in letters_guessed:
            letters_guessed.append(lglow)
            print('Good guess!',get_guessed_word(secret_word, letters_guessed))
            print('- - - - - - - - - - - - - ')
            #guesses_number -=1
            print('You have',guesses_remaining,'guesses left')
            print('Available letters:',get_available_letters(letters_guessed))
        
        #incorrect guess   
        elif lglow not in list(secret_word):
            letters_wrong.append(lglow)
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
            print('- - - - - - - - - - - - - ')
            guesses_remaining -=1
            print('You have',guesses_remaining,'guesses left')
            print('Available letters:',get_available_letters(letters_guessed))
            check=noguess(guesses_remaining)
        
        lis=sorted(uniqueletter(secret_word))
        print("lis",lis)
        letters_guessed=sorted(letters_guessed)
        print("letter",letters_guessed)
        
        if lis == letters_guessed:
            print('Congrats! You won!')
            print("Your total score for this game is: "+ str(unique(secret_word)*guesses_remaining))
            return None

    
    print("Sorry, you ran out of guesses. The word was " + str(secret_word))
    return None




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
