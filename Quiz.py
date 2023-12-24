def Quiz():
    print("Welcome to My Quiz Game!!")
    play = input("Do you want to Play this Quiz Game? ")
    if(play.lower() == "no"):
        quit()
    print("Lets Start th Game!!")
    score = 0
    
# === Questions ===
    answer = input("what is the full form of CPU? ") #Question-1
    if answer.lower() == "central processing unit":
        print("Correct!!")
        score +=1
    else:
        print("Incorrect!!")

    answer = input("What is the Full Form of PDF? ") #Question-2
    if answer.lower() == "portable document format file":
        print("Correct!!")
        score +=1
    else:
        print("Incorrect!!")

    answer = input("What is the use of Hard Disk in computer? ")   # Question-3
    if answer.lower() == "save data":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    answer = input("How many Bytes are there in 1 Kilobyte(KB)? ")   # Question-4
    if answer.lower() == "1024":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    answer = input("To close any open programme in the computer which 2 keys are combined used for it?  ")   # Question-5
    if answer.lower() == "alt+f4" or "alt + f4":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")
        
    answer = input("What is the Full Form of GPU?  ")   # Question-6
    if answer.lower() == "graphics processing unit":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    answer = input("Name the component which is the brain of computer? ")   # Question-7
    if answer.lower() == "cpu":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    answer = input("Which type of device is the monitor of the computer, Input\Output Device? ")   # Question-8
    if answer.lower() == "input":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    answer = input("Who is the Father of Computer? ")   # Question-9
    if answer.lower() == "charles babbage":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    answer = input("What is know as Temporary Memory or Volatile Memory in Computer? ")   # Question-10
    if answer.lower() == "ram":
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

    print(f"You Got {score} Correct Question!!")
    print("Well Done :)")
Quiz()

# === CODE HAS BEEN ENDED ====