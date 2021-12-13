def main():
    length=input("Enter the lengths of the jumps (cm) separated by commas.\n")

    if length == "":
        print("No accepted results.")

    else:
        length_list = length.split(",")
        length_list.sort()
        longest = int(length_list[len(length_list)-1])
        print(f"The best result is {longest:d} cm.")
main()