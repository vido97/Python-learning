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
        horizontal = calculate_number_of_seeds(width, height, germination, BEAN_ROW_SPACING, BEAN_SEED_SPACING)
        vertical = calculate_number_of_seeds(height, width, germination, BEAN_ROW_SPACING, BEAN_SEED_SPACING)

    elif veggie == 2:
        horizontal = calculate_number_of_seeds(width, height, germination, RADISH_ROW_SPACING, RADISH_SEED_SPACING)
        vertical = calculate_number_of_seeds(height, width, germination, RADISH_ROW_SPACING, RADISH_SEED_SPACING)

    else:
        horizontal = calculate_number_of_seeds(width, height, germination, CARROT_ROW_SPACING, CARROT_SEED_SPACING)
        vertical = calculate_number_of_seeds(height, width, germination, CARROT_ROW_SPACING, CARROT_SEED_SPACING)

    if vertical > horizontal:
        print(f"Set the rows perpendicular to the height ({height:d} cm) of the field to get maximum harvest.\nYou need {vertical:d} seeds.")
    elif horizontal > vertical:
        print(f"Set the rows perpendicular to the width ({width:d} cm) of the field to get maximum harvest.\nYou need {horizontal:d} seeds.")
    else:
        print(f"Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.\nYou need {horizontal:d} seeds.")
main()