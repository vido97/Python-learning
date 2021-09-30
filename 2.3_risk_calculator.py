def main():
    line1=input("Enter your age.\n")
    age=int(line1)
    line2=input("Enter your weight in kilograms.\n")
    weight=float(line2)
    line3=input("Enter your height in centimeters.\n")
    height=float(line3)
    line4=input("Has your parent or sibling been diagnosed with type 1 or type 2 diabetes? Enter yes or no.\n")
    heredity=str(line4)

    score=0

    if age <45:
        score =score+0
    elif 45 <= age <=54:
        score =score +2
    elif 55<= age <= 64:
        score=score+3
    elif age >64:
        score=score+4

    BMI = weight / ((height * 0.01) ** 2)
    if BMI <25:
        score=score+0
    elif 25 <= BMI <= 30:
        score = score +1
    elif BMI >30:
        score=score+2

    if heredity == "yes":
        score=score+5

    if score ==0:
        print("You have a low risk of getting type 2 diabetes.")
    elif 1<= score < 5:
        print("You have a moderate risk of getting type 2 diabetes.")
    else:
        print("You have a high risk of getting type 2 diabetes.")

main()
