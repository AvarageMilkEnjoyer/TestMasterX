#Test program by @AverageMilkEnjoyer#9164
#TestMasterX


Anwser1 = "a"  #Type the correct anwser between the ""
UserAnwser1 = "a" #Type the users anwser here!

Anwser2 = "b"  #Type the correct anwser between the ""
UserAnwser2 = "b" #Type the users anwser here!

Anwser3 = "c"  #Type the correct anwser between the ""
UserAnwser3 = "c" #Type the users anwser here!

Anwser4 = "d"  #Type the correct anwser between the ""
UserAnwser4 = "d" #Type the users anwser here!

Anwser5 = "e"  #Type the correct anwser between the ""
UserAnwser5 = "e" #Type the users anwser here!

RequirementToPass = 3 #How many question they have to get right to pass
MaxQuestions = 5 #How many questions




#Main code: Do not touch!
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
Score = 0
QuestionNumber = 0 

if Anwser1 == UserAnwser1:
    print("Thats correct!")
    Score += 1

if Anwser1 != UserAnwser1:
    print("Not quite right")
    
if Anwser2 == UserAnwser2:
    print("Thats correct!")
    Score += 1

if Anwser2 != UserAnwser2:
    print("Not quite right")

if Anwser3 == UserAnwser3:
    print("Thats correct!")
    Score += 1

if Anwser3 != UserAnwser3:
    print("Not quite right")
    
if Anwser4 == UserAnwser4:
    print("Thats correct!")
    Score += 1

if Anwser4 != UserAnwser4:
    print("Not quite right")
    
if Anwser5 == UserAnwser5:
    print("Thats correct!")
    Score += 1


if Anwser5 != UserAnwser5:
    print("Not quite right")
    
print("End of the quiz!")
print(O+"Your final score is:", Score)

if Score >= RequirementToPass:
    print(G+"You passed!")

if Score <= RequirementToPass:
    print(R+"You did not pass")
    
if Score == RequirementToPass:
    print(P+"The code has bugged! But the user has passed!")
