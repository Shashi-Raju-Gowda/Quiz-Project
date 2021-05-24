questions_dict = {"Easy":{"1: Who is the father of geometry?":["A. Aristotle","B. Euclid","C. Pythagoras","D. Kepler"],
"2: Entomology is science that is related to?":["A. Behavior of human being","B. Insects","C. The origin and history of technical and scientific terms","D. Formation of Rocks"],
"3: Federation Cup, World Cup, Allywyn International Trophy and Challenge Cup are related to?":["A. Tennis","B. Volleyball","C. Basketball","D. Cricket."],
"4: Each year World Red Cross and Red Crescent Day is celebrated on?":["A. 08th May","B. 18th May","C. 08th June","D. 18th June"]},
"Intermediate":{"1: Country that has the highest in Barley Production?":["A. China","B. India","C. Russia","D. France"],
"2: The metal whose salts are sensitive to light is?":["A. Zinc","B. Silver","C. Copper","D. Aluminium"],
"3: The Central Rice Research Station is situated in?":["A. Chennai","B. Cuttack","C. Bangalore","D. Quilon"]},
"Hard":{"1: The purest form of iron is?":["A. Wrought iron","B. Steel","C. Pig iron","D. Nickel steel"],
"2: Fathometer is used to measure?":["A. Earthquakes","B. Rainfall","C. Ocean depth","D. Sound intensity"],
"3: The staple food of the Vedic Aryan was?":["A. Barley and rice","B. Milk and its products","C. Rice and pulses","D. Vegetables and fruits"]}}
answers_list = ["B","A","A","A","C","B","B","A","C","B"]

def play():
    user_answers=[]
    UserloginAccount()
    print("\n==========QUIZ START==========")
    for i,j in questions_dict["Easy"].items():
        print("\nQuestion Level: Easy")
        print("\t",i)
        print("Options:")
        for k in j:
            print("\t",k)
        ans = input("\n\t Enter your option:")
        user_answers.append(ans)
    for i,j in questions_dict["Intermediate"].items():
        print("\nQuestion Level: Intermediate")
        print("\t",i)
        print("Options:")
        for k in j:
            print("\t",k)
        ans = input("\n\t Enter your option:")
        user_answers.append(ans)
    for i,j in questions_dict["Hard"].items():
        print("\nQuestion Level: Hard")
        print("\t",i)
        print("Options:")
        for k in j:
            print("\t",k)
        ans = input("\n\t Enter your option:")
        user_answers.append(ans)
		
    count = 0
    for i in range(len(user_answers)):
        if user_answers[i] == answers_list[i]:
            count += 1
    print("\nYour Score is :",count)    
    user_answers = []
    print("\nKey Answers: \n1:  'B'\n2:  'A'\n3:  'A'\n4:  'A'\n5:  'C'\n6:  'B'\n7:  'B'\n8:  'A'\n9:  'C'\n10: 'B'")


def addquizQuestions():
    print("\n======Login Successfull!!=====")
    print("\n")
    typeofquestion = input("Please choose the difficulty of question you would like to add (Easy\tIntermediate\tHard):  ")
    removequestions(typeofquestion)
    question = input("Please enter the question: ")
    options = []
    for i in range(65,69):
        temp = input("Please enter the option: ")
        final = chr(i)+". "+temp
        options.append(final)
    if typeofquestion == "Easy":
        questions_dict["Easy"][question] = options
        print("\nQuestion updated successfully!!")
    elif typeofquestion == "Intermediate":
        questions_dict["Intermediate"][question] = options
        print("\nQuestion updated successfully!!")
    elif typeofquestion == "Hard":
        questions_dict["Hard"][question] = options
        print("\nQuestion updated successfully!!")
    else:
        print("Please choose the correct parameter")

def removequestions(typeof):
    print("\nPlease delete a question first before updating any new questions.\n")
    if typeof == "Easy":
        for i,j in questions_dict["Easy"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Easy"].pop(i)
                break
            else:
                continue
    elif typeof == "Intermediate":
        for i,j in questions_dict["Intermediate"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Intermediate"].pop(i)
                break
            else:
                continue
    elif typeof == "Hard":
        for i,j in questions_dict["Hard"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Hard"].pop(i)
                break
            else:
                continue
    else:
        print("Please choose the correct parameter")

def UserloginAccount():
	print("\n==========PLAYER'S DATA PANEL==========")
	playername = input("Please enter your name: ")
	playerRollNo = input("Please enter your roll_no: ")
	print("\nWish you best of luck!!"+"\t"+playername,playerRollNo)

def exit():
    print("=================THE END=================")

def rules():
	print('''\n==========RULES==========
1. Each round consists of 10 questions. To answer, you must press A/B/C/D (case-sensitive).
2. Your final score and the key answers will be given at the end.
3. Each question carries 1 point. There's no negative marking for wrong answers.
4. Level of first 4 questions are Easy followed by 3 Intermediate and 3 Hard.
	''')

def about():
	print('''\n==========ABOUT US==========
Hello All, 
I'm SHASHI Raju Gowda pursuing my Data-Scientist Course in Edyoda University.
This is a part of my coding assessment written in Python.
Wish me a good luck to secure a good marks.
Hope you all enjoying this code :-)''')

if __name__ == "__main__":
    choice = 1
    while choice != 7:
        print('\n=========WELCOME TO QUIZ MASTER==========')
        print('-----------------------------------------')
        print('1. PLAY QUIZ')
        print('2. ADD QUIZ QUESTIONS')
        print('3. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
        print('4. ABOUT US')
        print('5. EXIT')
        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            play()
        elif choice == 2:
            print("\nYou need ADMIN permission to access this.")
            supername = input("\nCredentials please: ")
            if supername == "SuperUser":
                addquizQuestions()
            else:
                print(supername,"your authentication is not valid, access denied!!")
        elif choice == 3:
            rules()
        elif choice == 4:
            about()
        elif choice == 5:
            exit()
            break
        else:
            print('\n*****Please choose the valid input!!*****')
