locx = 0
locy = 0

def main():
    global locx, locy
    print("Option \n [1] Location \n [2] Move \n [3] Reset \n [any other input to exit]")
    choice = int(input("Enter your choice>>"))


    match choice:
        case 1:
            print(f"Current location: ({locx}, {locy})")
            main()
        case 2:
            direction = input("Move N, S, E, W>>").lower()
            match direction:
                case "n":
                    locy += int(input("How many steps?>>"))
                case "s":
                    locy -= int(input("How many steps?>>"))
                case "e":
                    locx += int(input("How many steps?>>"))
                case "w":
                    locx -= int(input("How many steps?>>"))

            print(f"Robbie moved to location: ({locx}, {locy})")
            main()
        case 3:
            locx = 0
            locy = 0
            print("Resetting...")
            main()
        case _:
            print("Exiting...")
            quit()

main()