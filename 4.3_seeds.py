BEAN_ROW_SPACING = 50  # cm
BEAN_SEED_SPACING = 15  # cm

RADISH_ROW_SPACING = 20  # cm
RADISH_SEED_SPACING = 4   # cm

CARROT_ROW_SPACING = 30  # cm
CARROT_SEED_SPACING = 2  # cm

def calculate_number_of_seeds(x, y, germination_rate, row_spacing, seed_spacing):
    #calculate amount of plants per direction
    number_of_row= x // row_spacing
    seeds_per_row= y // seed_spacing

    return int((number_of_row*seeds_per_row)/(germination_rate/100))

def main():
    print("This program calculates the number of seeds that you need.")
    width=int(input("Enter the width of the field (cm):\n"))
    height=int(input("Enter the height of the field (cm):\n"))
    veggie= int(input("Which vegetable do you want to grow?\n1. Beans\n2. Radishes\n3. Carrots\n"))
    germination= float(input("Enter the germination rate of the seeds (%):\n"))

    if veggie == 1:
        row_spacing = BEAN_ROW_SPACING
        seed_spacing = BEAN_SEED_SPACING

    elif veggie == 2:
        row_spacing = RADISH_ROW_SPACING
        seed_spacing = RADISH_SEED_SPACING
       
    else:
        row_spacing = CARROT_ROW_SPACING
        seed_spacing = CARROT_SEED_SPACING
        
     horizontal = calculate_number_of_seeds(width, height, germination, row_spacing,seed_spacing)
     vertical = calculate_number_of_seeds(height, width, germination,row_spacing, seed_spacing)
        
    if vertical > horizontal:
        print(f"Set the rows perpendicular to the height ({height:d} cm) of the field to get maximum harvest.")
    elif horizontal > vertical:
        print(f"Set the rows perpendicular to the width ({width:d} cm) of the field to get maximum harvest.")
    else:
        print(f"Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.")
    print(f"You need {horizontal:d} seeds.")
main()
