from random import choice


def draw_hangman(x):
   s = [
      """
         ________
         |      |
         |      
         |      
         |      
      ___|      
      """,
      """
         ________
         |      |
         |      O
         |      
         |      
      ___|      
      """,
      """
         ________
         |      |
         |      O
         |      |
         |      
      ___|      
      """,
      """
         ________
         |      |
         |      O
         |     /|
         |      
      ___|      
      """,
      """
         ________
         |      |
         |      O
         |     /|\\
         |      
      ___|      
      """,
      """
         ________
         |      |
         |      O
         |     /|\\
         |     / 
      ___|      
      """,
      """
         ________
         |      |
         |      O
         |     /|\\
         |     / \\
      ___|      
      """
   ]
    
   print(s[7 - x])


word_list = ["orange", "banana", "apple", "grape",  "blueberry"]
word = choice(word_list)
blank = []
try_= 7
for i in word:
    blank+='-'

while  try_:
    if '-' in blank:
        u =  input("Enter :  ")
        
        for i in range(len(word)):
            if u[0] == word[i]:
                blank[i] = u[0]
        draw_hangman(try_)
        if not(u[0] in word):

                try_-= 1
        print(blank)
    
    else:
        print("Winner")
        break
    
if try_ == 0:
    print("End")
    
