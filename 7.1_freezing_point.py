def main():
    name = input("Enter a filename:\n")
    count = 0
    try:
        tempfile = open(name, "r")
        for line in tempfile:
                line = line.rstrip()
                temperature = float(line)
                if temperature < 0:
                    count += 1
        tempfile.close()
        if count == 0:
            print("There were no temperatures below the freezing point.")
        else:
            print(f"{count:d} temperatures were below the freezing point.")
    except OSError:
        print(f"Error in reading file {name:s}. Closing program.")
    except ValueError:
        print(f"Incorrect line in file {name:s}. Closing program.")

main()