def main():
    name = input("Enter a filename:\n")
    laptimes = {}
    best_lap= float('inf')
    try:
        resultfile = open(name, "r")
        for line in resultfile:
            line = line.rstrip()
            parts = line.split(":")
            if len(parts) != 2:
                print("ERROR in line:", line)
            else:
                driver = parts[0]
                try:
                    time = float(parts[1])
                    # COMPLETE: update the dictionary laptimes when needed.
                    if driver not in laptimes:
                        laptimes[driver]=time
                    if driver in laptimes:
                        if time < laptimes[driver]:
                            laptimes[driver]=time
                except ValueError:
                    print("ERROR: incorrect lap time:", parts[1])
        resultfile.close()

        # Output the best lap times.
        if laptimes == {}:
            print("The file did not contain any correct lap times.")
        else:
            print("Results")
            print("Driver                Time (s)")
            drivers = sorted(laptimes)
            for driver in drivers:
                # COMPLETE the line below such that it prints
                # driver's name and his fastest lap time.
                print(f"{driver:20s}{laptimes[driver]:8.3f}")

    except OSError:
        print("Error in reading file {:s}. Closing program.".format(name))


main()