
print("ATTENTION!!! \nThis is NOT a medical diagnosis!")
print("Be honest. It will take 3-5 minutes.")
print("If you feel bad, then ask for help.")



questions = [
    "Sadness",
    "Pessimism",
    "Past Failure",
    "Loss of Pleasure",
    "Guilty Feelings",
    "Punishment Feelings",
    "Self-Dislike",
    "Self-Criticalness",
    "Suicidal Thoughts or Wishes",
    "Crying",
    "Agitation",
    "Loss of Interest",
    "Indecisiveness",
    "Worthlessness",
    "Loss of Energy",
    "Changes in Sleeping Pattern",
    "Irritability",
    "Changes in Appetite",
    "Concentration Difficulty",
    "Tiredness or Fatigue",
    "Loss of Interest in Hobbies or Activities"
]

score = 0 

for question in questions:
    print("\n" + question)
    print("0 - Not at all")
    print("1 - Mildly")
    print("2 - Moderately")
    print("3 - Severely")
    

    while True:
        try:
            answer = int(input("Your answer (0-3): "))
            if 0 <= answer <= 3:
                score += answer
                break
            else:
                print("Only numbers from 0 to 3!")
        except ValueError:
            print("Please, enter the number")        
print("\n" + '=' * 40)
print(f"Your total score {score} / 63")       

if score <= 13:
    print("No depressive symptoms")
elif score <= 19:
    print("Mild depression ")    
elif score <= 28:
    print("Moderate depression")    
else:
    print("Severe depression - it is highly recommended to talk to a specialist")

input("\nPress enter to exit...")       



