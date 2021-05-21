import random
import datetime
class Hotel:
    room =[]
    def __init__(self):
        self.roomName = {}
        self.roomPhoneNo = {}
        self.roomCheckIn = {}
        self.roomCheckOut = {}
        self.roomType = {}
        self.roomPrice = {}
        self.NoOfDays = {}
        self.restaurant = {}
        self.Address = {}

    def Booking(self):
        n = random.randint(100, 999)
        Hotel.room.append(n)
        Name=str(input('Enter your Name:-'))
        phoneNo=input('Enter your Phone Number:-')
        Address=input("Enter your Address:- ")

        if Name!="" and phoneNo!='' and Address!="":
            self.roomName.update({n: Name})
            self.roomPhoneNo.update({n:phoneNo})
            self.Address.update({n:Address})
        else:
            print('\nDear customer please enter the above details')

        print('\nDear customer Please select the type of Booking :)\n')
        print('1.Current Booking')
        print('2.Advanced Booking')
        type = int(input("\nEnter the type of booking--> "))
        if type == 1:
            CI = datetime.datetime.now()
            print(f"\n\t\tYour check-in Date is:-{CI.strftime('%d-%B-%Y')}\n\t\tYour check-in Time is:-{CI.strftime('%I:%M:%S')}\n")
            NoOfDays = int(input('Enter the number of Days for your stay:-'))
            self.NoOfDays.update({n:NoOfDays})
            td = datetime.timedelta(days=NoOfDays)
            CO = CI + td
            print(f"\n\t\tYour check-Out Date is:-{CO.strftime('%d-%B-%Y')}\n\t\tYour check-Out Time is:-{CO.strftime('%I:%M:%S')}\n")
            checkin = CI.strftime('%d-%B-%Y')
            self.roomCheckIn.update({n:checkin})
            checkout= CO.strftime('%d-%B-%Y')
            self.roomCheckOut.update({n:checkout})
            print('\n')
        else:
            CI = input("Enter Your check-in Date(D-M-Y):-")
            NoOfDays = int(input('Enter the number of Days for ur stay:-'))
            self.NoOfDays.update({n: NoOfDays})
            CO = input("Enter Your check-Out Date(D-M-Y):-")
            self.roomCheckIn.update({n:CI})
            self.roomCheckOut.update({n:CO})
            print('\n')
        while 'c':
            print('----------Room Type-----------------')
            print('1.2-bed Non-AC')
            print('2.2-bed AC')
            print('3. 3-bed Non-AC')
            print('4. 3-bed AC')
            print('\t\tPress 5 for Room Prices')
            op = int(input('Enter Suitable Number:-'))
            self.roomType.update({n: op})

            if op == 1:
                roomType= '2-bed Non-AC'
                self.roomType.update({n:roomType})
                print('------------Room Type:- 2-bed Non-AC')
                print(f"-------------Your Room number is:- {n}")
                roomPrice = 3000
                self.roomPrice.update({n:roomPrice})
                print("------------Price:- 3000")
                break

            elif op == 2:
                roomType = '2-bed AC'
                self.roomType.update({n:roomType})
                print('------------Room Type:- 2-bed AC')
                print(f"-------------Your Room number is :-{n}")
                roomPrice = 4000
                self.roomPrice.update({n:roomPrice})
                print("------------Price:- 4000")
                break

            elif op == 3:
                roomType = '3-bed Non-AC'
                self.roomType.update({n: roomType})
                print('------------Room Type:- 3-bed Non-AC')
                Hotel.room.append(n)
                print(f"-------------Your Room number is :-{n}")
                roomPrice = 4000
                self.roomPrice.update({n: roomPrice})
                print("-------------Price:- 4000")
                break
            elif op == 4:
                roomType = '3-bed AC'
                self.roomType.update({n: roomType})
                print('------------Room Type:- 3-bed AC')
                print(f"-------------Your Room number is :- {n}")
                roomPrice = 5000
                self.roomPrice.update({n: roomPrice})
                print("------------Price:- 5000")
                break

            elif op == 5:
                print(' 2-bed Non-AC:- 3000 per/day')
                print(' 2-bed AC:- 4000 per/day')
                print(' 3-bed Non-AC:- 4000 per/day')
                print(' 3-bed AC:- 5000 per/day')
                # print('Press q to quit and c to continue')
                # op = input()
                # if op == 'q':
                #     exit()
                # else:
                #     break

            else:
                print('Please enter a valid choice!')
                break

    def Rooms_Info(self):
        print('---------Hotel Room Info --------------\n')
        print('2-Bed Non AC')
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water.\n")
        print("STANDARD NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water + Window/Split AC.\n")
        print("3-Bed NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
        print("Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water.\n")
        print("3-Bed AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
        print("1 Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water + Window/Split AC.\n\n")
        # print('Press q to quit and c to continue')
        # op = input()
        # if op == 'q':
        #     exit()

    def Restaurant(self,n):
        temp_r=0
        print("-------------------------------------------------------------------------")
        print("                           HOTEL THE GRANDEUR ")
        print("-------------------------------------------------------------------------")
        print("                            Menu Card")
        print("-------------------------------------------------------------------------")
        print("\n BEVARAGES                              26 Dal Fry................ 140.00")
        print("----------------------------------      27 Dal Makhani............ 150.00")
        print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
        print(" 2  Masala Tea.............. 25.00")
        print(" 3  Coffee.................. 25.00      ROTI")
        print(" 4  Cold Drink.............. 25.00     ----------------------------------")
        print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
        print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
        print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
        print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
        print(" 9  Cheese Toast Sandwich... 70.00")
        print(" 10 Grilled Sandwich........ 70.00      RICE")
        print("                                       ----------------------------------")
        print(" SOUPS                                  33 Plain Rice.............. 90.00")
        print("----------------------------------      34 Jeera Rice.............. 90.00")
        print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
        print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
        print(" 13 Veg. Noodle Soup....... 110.00")
        print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
        print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
        print("                                        37 Plain Dosa............. 100.00")
        print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
        print("----------------------------------      39 Masala Dosa............ 130.00")
        print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
        print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
        print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")
        print(" 19 Palak Paneer........... 120.00")
        print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")
        print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
        print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
        print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
        print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")
        print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
        choice = 1
        print("\nEnter the Dish numbers u want to order\n\t\t press '0' to Exit \n")
        while choice != 0:
            choice = int(input(" -> "))
            if choice == 1 or choice == 31 or choice == 32:
                rs = 20
                temp_r = temp_r + rs
            elif choice <= 4 and choice >= 2:
                rs = 25
                temp_r = temp_r + rs
            elif choice <= 6 and choice >= 5:
                rs = 30
                temp_r = temp_r + rs
            elif choice <= 8 and choice >= 7:
                rs = 50
                temp_r = temp_r + rs
            elif choice <= 10 and choice >= 9:
                rs = 70
                temp_r = temp_r + rs
            elif (choice <= 17 and choice >= 11) or choice == 35 or choice == 36 or choice == 38:
                rs = 110
                temp_r = temp_r + rs
            elif choice <= 19 and choice >= 18:
                rs = 120
                temp_r = temp_r + rs
            elif (choice <= 26 and choice >= 20) or choice == 42:
                rs = 140
                temp_r = temp_r + rs
            elif choice <= 28 and choice >= 27:
                rs = 150
                temp_r = temp_r + rs
            elif choice <= 30 and choice >= 29:
                rs = 15
                temp_r = temp_r + rs
            elif choice == 33 or choice == 34:
                rs = 90
                temp_r = temp_r + rs
            elif choice == 37:
                rs = 100
                temp_r = temp_r + rs
            elif choice <= 41 and choice >= 39:
                rs = 130
                temp_r = temp_r + rs
            elif choice <= 46 and choice >= 43:
                rs = 60
                temp_r = temp_r + rs
            elif choice == 0:
                pass
            else:
                print("Wrong Choice..!!")
        print(f"----Total Bill:- Rs {temp_r}/-")
        print("\n\t\t It will be added to your Total during Payment!!")
        print('----------------Thank You for the order-------------- :)')
        print(f'\n\t\tHave a nice Day {self.roomName[n]}-------------\n')
        self.restaurant.update({n:temp_r})

    def Payment(self,n):
        print('-----------MODE OF PAYMENT------- ')
        print('1.Credit/Debit card')
        print('2.Paytm/PhoenPe')
        print('3.Using UPI')
        print('4.Cash')
        choice = input()
        if choice not in ['1', '2', '3', '4']:
            print('please Enter a valid option')
        else:
            choice = int(choice)
        if choice == 1 or 2 or 3 or 4:
            print("\n\n --------------------------------")
            print("           Hotel THE GRANDEUR")
            print(" --------------------------------")
            print("              Bill")
            print(" --------------------------------\t")
            print(f'\n Name: {self.roomName[n]} \t\n Phone No.: {self.roomPhoneNo[n]} \t\n Address: {self.Address[n]}\t')
            print(f"\n Check-In: {self.roomCheckIn[n]} \t\n Check-Out:  {self.roomCheckOut[n]}\t")
            print(f"\n Number of Days: {self.NoOfDays[n]} \t\n Room Charge per/day: {self.roomPrice[n]}\t")
            print(f"\n Room Type:  {self.roomType[n]} \t\n Room Charges:  Rs{self.roomPrice[n] * self.NoOfDays[n]}/-\t")
            print(" Restaurant Charges: \t", self.restaurant[n])
            print(" --------------------------------")
            print(f"\n Total Amount: Rs{(self.roomPrice[n] * self.NoOfDays[n]) + self.restaurant[n]}/- \t")
            print(" --------------------------------")
            print("          Thank You")
            print("          Visit Again :)")
            print(" --------------------------------\n")

    def Customer_Records(self,n):
        print(f"\t  Name: {self.roomName[n]} \n\t  Phone No.: {self.roomPhoneNo[n]} \t\n \t  Address: {self.Address[n]}\t")
        print(f"\n\t Number of Days: {self.NoOfDays[n]} \n\t Room Charge per/day: {self.roomPrice[n]} \t")
        print(f"\n\t Room Type:  {self.roomType[n]} \n\t Room Charges:  {self.roomPrice[n] * self.NoOfDays[n]} \t")
        print(f"\n\t Check-In: {self.roomCheckIn[n]} \n\t Check-Out:  {self.roomCheckOut[n]} \t")

MiniPro=Hotel()
while True:
    print(f'\n\n\t\t\t\t\t\tWelcome To the THE GRANDEUR Hotel.\nEnter your choice to continue\n')
    print('\t\t\t1.Booking\n')
    print('\t\t\t2.Rooms_Info\n')
    print('\t\t\t3.Restaurant\n')
    print('\t\t\t4.Customer Records\n')
    print('\t\t\t5.Payment and Check-Out\n')
    print('\t\t\t6.Change/Upgrade Room\n')

    user_choice = input()
    if user_choice not in ['1', '2', '3', '4', '5','6']:
        print('please Enter a valid option\n')
    else:
        user_choice = int(user_choice)
    if user_choice == 1:
        MiniPro.Booking()
    elif user_choice == 2:
        MiniPro.Rooms_Info()
    elif user_choice == 3:
        n = int(input('Enter Your Room No.:-'))
        MiniPro.Restaurant(n)
    elif user_choice == 4:
        n = int(input('Enter Your Room No.:-'))
        MiniPro.Customer_Records(n)
    elif user_choice == 5:
        n = int(input('Enter Your Room No.:-'))
        MiniPro.Payment(n)
    elif user_choice == 6:
        print("Dear customer You will be checked-Out from Your current room \nand Shifter to ur new Room\n")
        n = int(input('Enter Your Current Room No.:-'))
        MiniPro.Payment(n)
        print('Please Ignore the Bill if you have Changed/Upgraded Ur room \nbefore the current checkout Date ')
        print("\nYour Request is Processed Please Enter the below details for Room change/Upgrade\n")
        MiniPro.Booking()

    print('Press q to quit and c to continue')
    user_choice2 = input()
    if user_choice2 == 'q':
        exit()
    elif user_choice2 == 'c':
        continue
