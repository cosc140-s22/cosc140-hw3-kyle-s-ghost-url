#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist

def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")
    playernumber = 1
    word = ""
    while True:
      l = getletter(playernumber)
      word+=l
      print(word)
      if loser(word, words):
        print(f"Player {playernumber} has just lost")
        break
      if playernumber == 1:
        playernumber = 2
      else:
        playernumber = 1

def getletter (player):
  while True:
    letter = input(f" Player {player}, give a letter: ")
    if not letter.isalpha() or len(letter) != 1:
      print("Give me exactly one letter")
    else:
      return letter.upper()

      
def isword (fragment, words):
  return fragment in words

def startword(fragment, words):
  for word in words:
    if word.startswith(fragment):
      return True
  return False

def loser(word, words):
  if len(word) > 3 and isword(word, words):
    return True
  if not startword(word, words):
    return True
  return False
    
  #you can start your code here, inside main

main()
