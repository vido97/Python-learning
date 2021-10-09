#The risk calculator information from user , scores the answers and calculates the risk. 
#The risk of developing type 2 diabetes is low, when the score is 0 points, moderate when the score is at least 1 point but under 5 points and high when the score is 5 or more points.

def main():
    age=int(input("Enter your age.\n"))
    weight=float(input("Enter your weight in kilograms.\n"))
    height=float(input("Enter your height in centimeters.\n"))
    heredity=str(input("Has your parent or sibling been diagnosed with type 1 or type 2 diabetes? Enter yes or no.\n"))

    score=0
    BMI = weight / ((height * 0.01) ** 2)
    
    if 45 <= age <=54:
        score += +2
    elif 55<= age <= 64:
        score +=3
    elif age >64:
        score += 4

    
    if 25 <= BMI <= 30:
        score += 1
    elif BMI >30:
        score += 2

    if heredity == "yes":
        score += 5

    if score ==0:
        print("You have a low risk of getting type 2 diabetes.")
    elif 0< score < 5:
        print("You have a moderate risk of getting type 2 diabetes.")
    else:
        print("You have a high risk of getting type 2 diabetes.")

main()
