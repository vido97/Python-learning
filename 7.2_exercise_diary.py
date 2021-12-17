def main():
    filename = input("Enter the name of the file containing your exercise diary:\n")

    try:
        tempfile = open(filename, "r")
        sport = input("What sport are you interested in?\n")
        sum_time = 0
        count_day = 0
        found = False
        time_correct= True
        print("Day        Time")
        for line in tempfile:
            line = line.rstrip()
            parts = line.split(",")
            if parts[1] == sport:
                found = True
                try:
                    if time_correct == True:
                        time = int(parts[2])
                        sum_time += time
                        count_day += 1
                        print(f"{parts[0]}   {parts[2]} min")
                except ValueError:
                    print(f"Incorrect time in the file '{filename:s}'. Program ends.")
                    time_correct=False
        tempfile.close()
        if found and time_correct:
            print("-" * 31)
            print(f"Total exercise time: {sum_time//60:d} h {sum_time%60:d} min")
            print(f"Number of exercise days: {count_day:d}")

        elif found ==False:
            print(f"The sport '{sport:s}' was not found in the file.")

    except OSError:
        print(f"Error in reading the file '{filename:s}'. Program ends.")

main()