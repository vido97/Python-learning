#Write a program that determines the minimum scores of the exam for grades 1-5
#and the exam grades for the students according to the score limits.

def determine_grade_limits(max_points, passing_percentage):
    min_point= max_points*(passing_percentage/100)
    point_distance = (max_points-min_point)/5
    COUNT=5
    point_list = [0.0] * COUNT
    point_list[0]= min_point
    for i in range (0,COUNT):
        point_list[i]= min_point + (point_distance*i)
    return point_list

def grade_points(exam_points, grade_limits):
    if exam_points < grade_limits[0]:
        return 0
    elif grade_limits[0] <= exam_points < grade_limits[1]:
        return 1
    elif grade_limits[1] <= exam_points < grade_limits[2]:
        return 2
    elif grade_limits[2] <= exam_points < grade_limits[3]:
        return 3
    elif grade_limits[3] <= exam_points < grade_limits[4]:
        return 4
    else:
        return 5

def main():
    max_points = float(input("Enter the maximum points of the exam.\n"))
    passing_percent= int(input("Enter the passing percentage of the exam.\n"))
    grade_limits = determine_grade_limits(max_points, passing_percent)

    input_point_list = []
    exam_points= input("Enter the exam points of the students. Stop with empty line.\n")

    if exam_points != "":
        exam_points_f = float(exam_points)
        input_point_list.append(exam_points_f)

    while exam_points != "":
        exam_points = input()
        if exam_points != "":
            exam_points_f = float(exam_points)
            input_point_list.append(exam_points_f)

    print(f"Points Grade")

    for point in input_point_list:
        grade = grade_points(point, grade_limits)
        print(f"{point:<6.1f}{grade:3d}")

main()