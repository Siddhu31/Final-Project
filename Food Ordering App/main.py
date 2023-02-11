import sys
import time
import json
from Admin import Admin
from User import User

print("-------------------------------------------->>>>>Welcome to Foodie App <<<<<-------------------------------------------------\n")
time.sleep(5)
demo1 = User()
print(demo1.login("admin123@foodie.com", "Foodie@123"))

while True:
    l = []
    rs = 0
    order_history = {}
    print("+=" * 50)
    print("------>>>>>Press P 👉👉 For Place New Order")
    print("------>>>>>Press U 👉👉 For Update Profile")
    print("------>>>>>Press H 👉👉 For Get History From App")
    print("------>>>>>Press E 👉👉 For Exit From App")
    print("=+" * 50)
    user_input = input("Press Button :")
    if user_input == "P" or user_input == "p":
        with open("Food Item.json", "r") as f:
            temp = json.load(f)
        print("1.", temp["1"]["Quantity"], " ", temp["1"]["Food Name"], "..........................",
              temp["1"]["Price"], "Rupee")
        print("2.", temp["2"]["Quantity"], " ", temp["2"]["Food Name"], "..........................",
              temp["2"]["Price"], "Rupee")
        print("3.", temp["3"]["Quantity"], " ", temp["3"]["Food Name"], "..........................",
              temp["3"]["Price"], "Rupee")
        print("4.", temp["4"]["Quantity"], " ", temp["4"]["Food Name"], "..........................",
              temp["4"]["Price"], "Rupee")
        print("5.", temp["5"]["Quantity"], " ", temp["5"]["Food Name"], "..........................",
              temp["5"]["Price"], "Rupee")
        print("6.", temp["6"]["Quantity"], " ", temp["6"]["Food Name"], "..........................",
              temp["6"]["Price"], "Rupee")
        print("7.", temp["7"]["Quantity"], " ", temp["7"]["Food Name"], "..........................",
              temp["7"]["Price"], "Rupee")
        print("8.", temp["8"]["Quantity"], " ", temp["8"]["Food Name"], "..........................",
              temp["8"]["Price"], "Rupee")
        print("9.", temp["9"]["Quantity"], " ", temp["9"]["Food Name"], "..........................",
              temp["9"]["Price"], "Rupee")
        print("10.", temp["10"]["Quantity"], " ", temp["10"]["Food Name"], "..........................",
              temp["10"]["Price"], "Rupee")
        print("Press 0 for End ")
        print()
        print("------------------------->>>>>Press 999 For Place Your Order <<<<------------------------")
        ch = 1
        while ch != 0:
            ch = int(input(" Press Button For Order----> "))
            if ch == 1:
                rs += 200
                l.append(temp["1"]["Food Name"])

            elif ch == 2:
                rs += 450
                l.append(temp["2"]["Food Name"])

            elif ch == 3:
                rs += 210
                l.append(temp["3"]["Food Name"])

            elif ch == 4:
                rs += 140
                l.append(temp["4"]["Food Name"])

            elif ch == 5:
                rs += 220
                l.append(temp["5"]["Food Name"])

            elif ch == 6:
                rs += 220
                l.append(temp["6"]["Food Name"])

            elif ch == 7:
                rs += 10
                l.append(temp["7"]["Food Name"])

            elif ch == 8:
                rs += 35
                l.append(temp["8"]["Food Name"])

            elif ch == 9:
                rs += 230
                l.append(temp["9"]["Food Name"])

            elif ch == 10:
                rs += 50
                l.append(temp["10"]["Food Name"])

            elif ch == 999:
                print(l)
                order_history = {"Order History": l, "Total Bill": rs}
                with open("Bill.json", "w") as f:
                    json.dump(order_history, f, indent=5)
                time.sleep(2)
                print("Total Bill : - ", rs)
                print(" 🎆🎊🎊-*-*-*-*-*-*-*Your Order Got Placed-*-*-*-*-*-*-*🎆🎊🎊")
                print("You'll Get Your Order Soon")
                print()
                print("*-*-*-*-*-*-*-*-*Thanks For Using Foodie App*-*-*-*-*-*-*-*-*")
                break

    elif user_input == "H" or user_input == "h":
        with open("Bill.json", "r") as f:
            temp = json.load(f)
            print(temp)

    elif user_input == "U" or user_input == "u":
        demo1.update_profile()

    elif user_input == "E" or user_input == "e":
        time.sleep(3)
        print("*-*-*-*-*-*-*-*-*Thanks For Using Foodie App*-*-*-*-*-*-*-*-*")
        sys.exit()
