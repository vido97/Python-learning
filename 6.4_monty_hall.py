import random

def initialize_doors(number_of_doors):
    door_list=[0]*number_of_doors
    car_index=random.randint(0,number_of_doors-1)
    door_list[car_index] = True
    i=0
    while i < len(door_list):
        if i !=car_index:
            door_list[i]=False
        i+=1
    return door_list

def remove_wrong_doors(chosen_door, doors):
    for door_left in range (1,len(doors)):
        if doors[chosen_door-1] == True and door_left != chosen_door:
            door_left=random.randint(1,len(doors))
            return door_left
        else:
            return doors.index(True) +1

def print_doors(doors, dont_open):
    number_of_doors = len(doors)
    print(" _  "*number_of_doors)
    i=0
    while i < len(doors):
        if i + 1 in dont_open:
            print("| | ", end="")
        elif doors[i] == True:
            print("|C| ", end="")
        else:
            print("|G| ", end="")
        i+=1

    print("")
    print("|_| "*number_of_doors)

    for door_number in range (1,number_of_doors+1):
        print(f"{door_number:^3d}", end=" ")
    print("")

def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)

    number_of_doors = int(input("How many doors?\n"))

    while number_of_doors not in range(3,999) :
        print("The number of doors must be between 3-999!")
        number_of_doors=int(input("How many doors?\n"))
    door_list = initialize_doors(number_of_doors)
    dont_open=[]
    for door_number in range (1,number_of_doors+1):
        dont_open.append(door_number)

    print_doors(door_list, dont_open)

    chosen_door = int(input(f"Choose a door 1-{number_of_doors:d}.\n"))
    while chosen_door not in range(1,number_of_doors+1):
        chosen_door=int(input(f"Choose a door 1-{number_of_doors:d}.\n"))

    print(f"You chose the door number {chosen_door:d}.")
    print("...")

    door_left= remove_wrong_doors(chosen_door, door_list)

    dont_open_2=[]
    dont_open_2.append(chosen_door)
    dont_open_2.append(door_left)

    print_doors(door_list, dont_open_2)

    print(f"{number_of_doors - 2:d} certainly wrong doors were opened. The door number {door_left:d} was left.")

    final_choice=int(input(f"Choose {chosen_door:d} if you want to keep the door you first chose and choose {door_left:d} if you want to change the door.\n"))
    while final_choice != chosen_door and final_choice != door_left :
        final_choice = int(input(f"Choose {chosen_door:d} if you want to keep the door you first chose and choose {door_left:d} if you want to change the door.\n"))

    print_doors(door_list,[])

    if door_list[final_choice-1]==True:
        print("Congratulations! The car was behind the door you chose!")
    else:
        print("A goat emerged from the door you chose! The car was behind the other door :(")

main()