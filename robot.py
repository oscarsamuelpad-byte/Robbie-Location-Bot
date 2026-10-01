locx = 0
locy = 0
old_locy = 0
old_locx = 0
battery = 100
def main():
    global locx, locy, battery
    print("Option \n [1] Location \n [2] Move \n [3] Reset \n [4] Charge Battery \n[any other input to exit]")
    choice = int(input("Enter your choice>>"))


    match choice:
        case 1:
            print(f"Current location: ({locx}, {locy}), Battery is {battery}%")
            main()
        case 2:
            direction = input("Move N, S, E, W>>").lower()
            match direction:
                case "n":
                    if (-10 < locx < 10) and (-10 < locy < 10):
                        if battery > 0:
                            old_locy = locy
                            move_amount = int(input("How many steps?>>")) 
                            locy += move_amount
                            battery -= (move_amount*10)
                            move_amount = 0
                            if -10 >= locy >= 10:
                                print("Robbie has hit a wall")
                                locy = old_locy
                        else:
                            print("Battery needs recharge")
                    else:
                        print("You've hit a wall")
                case "s":
                    if (-10 < locx < 10) and (-10 < locy < 10):
                        if battery > 0:
                            old_locy = locy
                            move_amount = int(input("How many steps?>>"))
                            locy -= move_amount
                            battery -= (move_amount*10)
                            move_amount = 0
                            if -10 >= locy >= 10:
                                print("Robbie has hit a wall")
                                locy = old_locy
                        else:
                            print("Battery needs recharge")
                    else:
                        print("You've hit a wall.")
                case "e":
                    if (-10 < locx < 10) and (-10 < locy < 10):
                        if battery > 0:
                            old_locx = locx
                            move_amount = int(input("How many steps?>>"))
                            locx += move_amount
                            battery -= (move_amount*10)
                            move_amount = 0
                            if -10 >= locx >= 10:
                                print("Robbie has hit a wall")
                                locx = old_locx
                        else: 
                            print("Battery needs charge.")
                    else:
                        print("You've hit a wall")
                case "w":
                    if (-10 < locx < 10) and (-10 < locy < 10):
                        if battery > 0:
                            old_locx = locx
                            move_amount = int(input("How many steps?>>"))
                            locx -= move_amount
                            battery -= (move_amount*10)
                            move_amount = 0
                            if -10 >= locx >= 10:
                                print("Robbie has hit a wall")
                                locx = old_locx
                        else: 
                            print("Battery needs charge")
                    else:
                        print("You've hit a wall")

            print(f"Robbie moved to location: ({locx}, {locy}), Battery is {battery}%")
            main()
        case 3:
            locx = 0
            locy = 0
            print("Resetting...")
            main()
        case 4:
            battery_needed = 100 - battery
            battery = battery_needed + battery
            main()
        case _:
            print("Exiting...")
            quit()

main()