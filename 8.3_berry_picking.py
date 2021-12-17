BERRY_TYPES = ["blueberry", "lingonberry", "cloudberry", "cranberry", "raspberry", "strawberry"]

def berrytype(file1,namelist):
    tempfile = open(file1, "r")
    firstline = tempfile.readline()
    for line in tempfile:
        if line != firstline and line != "\n":
            line = line.rstrip()
            parts = line.split(",")
            if len(parts) != 3:
                print("Invalid line:", line)
            elif parts[1] not in BERRY_TYPES:
                print("Invalid line:", line)
            else:
                try:
                    type = parts[1]
                    weight = int(parts[2])
                    if type in namelist:
                        namelist[type] = (namelist[type] + weight)
                    else:
                        namelist[type] = weight
                except ValueError:
                    print("Invalid line:", line)
    tempfile.close()
    print("File read.")

def berryprice(file2,pricelist):
    tempfile = open(file2, "r")
    firstline = tempfile.readline()
    for line in tempfile:
        if line != firstline and line != "\n":
            line = line.rstrip()
            parts = line.split(":")
            if len(parts) != 2:
                print("Invalid line:", line)
            elif parts[0] not in BERRY_TYPES:
                print("Invalid line:", line)
            else:
                try:
                    price = float(parts[1])
                    pricelist[parts[0]] = price
                except ValueError:
                    print("Invalid line:", line)

    tempfile.close()
    print("File read.")

def main():
    namelist={}
    pricelist = {}
    try:
        file1 = input("Enter the name of the file containing the berry data:\n")
        berrytype(file1,namelist)
        try:
            file2 = input("Enter the name of the file containing the prices of the berries:\n")
            berryprice(file2, pricelist)
            missing_price = False
            for berry in namelist:
                if berry in BERRY_TYPES and berry not in pricelist:
                    missing_price = True

            if missing_price == True:
                print(f"Some of the berry prices are missing from the file '{file2:s}'.")

            else:
                print("")
                print("Berry type   Picked berries (kg)   Money earned (eur)")
                print("-" * 53)
                kg_sum = 0
                price_sum = 0
                for berry in namelist:
                    kg_sum += namelist[berry]
                    price_sum += namelist[berry] * pricelist[berry]
                    print(f"{berry:12s}{namelist[berry]:19d}{(namelist[berry] * pricelist[berry]):22.2f}")
                print("-" * 53)
                print(f"Total{kg_sum:26d}{price_sum:22.2f}")
        except OSError:
            print("Invalid file:", file2)
    except OSError:
        print("Invalid file:", file1)

    print("")
    print("Program ends.")

main()