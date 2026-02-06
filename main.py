


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

joke = input("Do you want to hear a joke? ")
if joke == "no":
    print("Okay suit yourself!")
while joke == "yes": 
    print("Great, Let's Play") #hi
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    if question == "robbers":
        input("Knock Knock ")
        input("Calder")
        print("Calder police - I've been robbed!")
        joke = input("Do you want to hear another joke or are you finished? ")
    elif question == "tanks":
        input("Knock Knock ")
        input("Tank ")
        input("You are welcome! ")
        joke = input("Do you want to hear another joke or are you finished? ")
    elif question == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")
        joke = input("Do you want to hear another joke or are you finished? ")
if joke == "finished":
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")

#------------------------------------------------------------
# Part 1
# Missing Requirements:
# A List: Your program must use at least one list or array to manage data. Currently, you use individual variables.
# You should store your jokes in a list and access them there.
# Student-Developed Procedure: You must define at least one named procedure (function) that takes at least one parameter. 
# Within your procedure, you must have an algorithm that includes sequencing, selection, and iteration all working together to achieve a result.                 


# IT COULD BE FURTHER SIMFLIFIED INTO THIS TO MAKEIT USE LESS SPACE AND FOR IT TO BE MORE EFFICIENT AND ORGANIZED
# It could be further simplified into this to make use less space and for it to be more efficient and organized


# Part 2 
# Missing            #   function ---- it doesn't have a fucntion(so no function)
# could bhe improved #   Parameters ---- It does have a parameter with final_score ( has a parameter but not fully used in a way cause their is no function)
                     #   sequencing ---- it does have sequencing with multiple lines of code
                     #   selection ---- it does have selection with if, elif, and else statements
# I think is missing #   iteration ---- It  does not have the ability to repeat itself until the user wants to listen to another joke or is finished (so no iteration)
                     #   different paths, depending on parameter value ---- It gives you many options with the use of inputs, and outputs that come from with elif, else, and if statements 
 # Missing           #   list ---- It does not have a list (so no list)



# Part 3 : now we will be impoving it to reach the needed requirements

joke = input("Do you want to hear a joke? ")
if joke == "no":
    print("Okay suit yourself!")
while joke == "yes": 
    print("Great, Let's Play") 
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    if question == "robbers":
        input("Knock Knock ")
        input("Calder")
        print("Calder police - I've been robbed!")
        joke = input("Do you want to hear another joke or are you finished? ")
    elif question == "tanks":
        input("Knock Knock ")
        input("Tank ")
        input("You are welcome! ")
        joke = input("Do you want to hear another joke or are you finished? ")
    elif question == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")
        joke = input("Do you want to hear another joke or are you finished? ")
if joke == "finished":
     rate = int(input("Please rate our game 1-10! "))
     final_score = int(rate * 10)
     print(str(final_score) + " percent satisfaction rate")
     friend = input("Would you recommend this game to a friend? ")

     if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
     else:
        print("Sorry you did not enjoy it. ")

# ___________________________________________________________________________________________________ this code under is the improved version which is performance task ready for submission as it reaches the requirements much better and is more organized and simple with the use of lists and functions

jokes = {
    "robbers": ["Knock Knock", "Calder", "Calder police – I've been robbed!"],
    "tanks": ["Knock Knock", "Tank", "You're welcome!"],
    "pencils": ["Knock Knock", "Broken pencil", "Nevermind, it's pointless!"]
}
def tell_joke(joke_lines):
    for line in joke_lines:      
        user = input(line + " ") 
    print()                      

def end_game(final_score):
    for rate in range(1, 11):
        if rate == final_score:
            final_score = rate * 10
            print(str(final_score) + "% satisfaction rate")
            break
    else:
        print("Invalid rating.")

    
    
    
    friend = input("Would you recommend this game to a friend? ")
    if friend in ["yes", "maybe"]:
        print("Thanks, we appreciate it.")
    else:
        print("Sorry you did not enjoy it.")



joke = input("Do you want to hear a joke? ")

if joke == "no":
    print("Okay, suit yourself!")

while joke == "yes":
    print("Great, let's play!")

    question = input("Choose a joke: robbers, tanks, or pencils: ")


    if question in jokes:
        tell_joke(jokes[question])  
    else:
        print("Sorry, I don't know that joke category.")

    joke = input("Do you want to hear another joke or are you finished? ")

if joke == "No" or joke == "finished":
    end_game(final_score=int(input("Please rate our game 1-10! ")))