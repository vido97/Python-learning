#The program tells whether coordinates of a point entered by the user are inside a cellular network range
import math

def readfile(filename,cell_tower_list):
    coordinates=[0,0]
    basestation=[]
    tempfile=open(filename,"r")
    firstline = tempfile.readline()
    for line in tempfile:
        if line != firstline:
            line = line.rstrip()
            parts1 = line.split(":")
            parts2= parts1[0].split(",")
            if len(parts1) != 2:
                print("Invalid line: ",line)
            elif len(parts2) != 2:
                print("Invalid coordinates or radius in line: ",line)
            else:
                try:
                    working_range=int(parts1[1])
                    coordinate1=int(parts2[0])
                    coordinate2=int(parts2[1])
                    cell_tower_list.append([[coordinate1,coordinate2],working_range])
                except ValueError:
                    print("Invalid coordinates or radius in line: ",line)
    print("File read.")
    tempfile.close()

def is_inside_cell_tower_range(point, cell_tower_list):
    in_range=False
    for cell_tower in cell_tower_list:
        pointx = point[0]
        pointy = point[1]
        centerx = cell_tower[0][0]
        centery = cell_tower[0][1]
        distance = math.sqrt((pointx - centerx) ** 2 + (pointy - centery) ** 2)
        working_range = cell_tower[1]
        if distance <= working_range:
            in_range=True
            return in_range
    if in_range == False:
        return False

def find_nearest_tower_in_range(point, cell_tower_list):
    cell_tower_in_range=[]
    in_range= False
    nearest_distance=0
    pointx = point[0]
    pointy = point[1]
    for cell_tower in cell_tower_list:
        centerx = cell_tower[0][0]
        centery = cell_tower[0][1]
        distance = math.sqrt((pointx - centerx) ** 2 + (pointy - centery) ** 2)
        working_range = cell_tower[1]
        if distance <= working_range:
            cell_tower_in_range.append([centerx,centery])
            nearest_distance = distance
            in_range = True

    for nearest_tower in cell_tower_in_range:
        distance2 = math.sqrt((pointx - nearest_tower[0]) ** 2 + (pointy - nearest_tower[1]) ** 2)
        if distance2 < nearest_distance:
            nearest_distance = distance2
        if nearest_distance == distance2:
            return nearest_tower

    if len(cell_tower_list) == 0 or in_range == False:
        return [-1,-1]

def main():
    cell_tower_list = []
    point_list = [0,0]

    try:
        filename = input("Enter the name of the file containing the cell tower information:\n")
        readfile(filename,cell_tower_list)
        print("")

        if len(cell_tower_list) == 0:
            print("No cell tower information available.\nProgram ends.")

        else:
            point = input("Enter coordinates. Stop with an empty line.\nEnter the coordinates separated by comma:\n")

            while point != "":
                point_part = point.split(",")
                if len(point_part) != 2:
                    print("Invalid coordinates! Enter two coordinates separated by comma.")
                else:
                    try:
                        point1 = int(point_part[0])
                        point2 = int(point_part[1])
                        if point1 < 0 or point2 <0:
                            print("Invalid coordinates! Coordinates must be positive integers.")
                        else:
                            point_list[0]=point1
                            point_list[1]=point2
                            if is_inside_cell_tower_range(point_list, cell_tower_list) == True:
                                print("The place is inside a cellular network range.")
                                nearest_point=find_nearest_tower_in_range(point_list,cell_tower_list)
                                print(f"The coordinates of the cell tower with the strongest signal: ({nearest_point[0]}, {nearest_point[1]})")
                            else:
                                print("The place is not inside of any cell tower range.")
                    except ValueError:
                        print("Invalid coordinates! Enter the coordinates as integers.")
                print("")
                point = input("Enter the coordinates separated by comma:\n")

            print("Program ends.")

    except OSError:
        print(f"Error in reading the file '{filename:s}'.")
        print("")
        print("No cell tower information available.\nProgram ends.")

main()