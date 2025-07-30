import read
import write

def welcome():
    """ While starting the Software, A WELCOME screen will be appear"""
    print("*" * 100)
    print("|","                                                                                                 |")
    print("|                    WELCOME to the Nepal's Land Rental Property!                                  |")
    print("|                       Developed by HIRDESH CHAUHAN...                                            |")
    print("|","                                                                                                 |")
    print("*" * 100)

def showDetail(dic):
    #to show the land details..........
    print("*" * 100)
    print("-" * 100)
    print("Kitta", "\t\t", "City", "\t\t", "    Direction", "\t", "     Anna","\t" ,"Price","\t\t","Status")
    print("-" * 100)
    print("*" * 100)
    for key,value in dic.items():
        print ((key)+"\t\t"+value[0]+"\t\t"+value[1]+"\t\t"+value[2]+"\t"+value[3]+"\t\t"+value[4])
        print()
def Demonstratingmessages():
    """ When the program runs, an introduction screen will show up. """
    print("\n")
    print("-" * 100)
    print("\n")
    print("Select the desirable option of the Land Rental Property!")
    print("(1) || Press 1 to rent a Land from the Land Rental Property!")
    print("(2) || Press 2 to return a Land to the Land Rental Property!")
    print("(3) || Press 3 to exit from the application.")
    print("\n")
    print("-" * 100)

    option = input("Enter your desirable option: ")
    print()
    return option
mon = {} #dictionary is made to store the month which is rented by user
price = {} #dictionary is made to store the price which is rented by user in case of extra month user have pay fine

def rent_land():
    tempSellbill = []
    global mon,price
    correct = False
    while correct == False:
        
        Name = input("Enter your name: ")
        Phone_num = input("Enter your number: ")
        Address = input("Enter your current temporary or permanent address: ")
        if Name.replace(" ","").isalpha() and Phone_num.isdigit() and Address.isalpha():
            # .isalpha check whether the given input is in alphabet or not and .isdigit check whether the given input is in number or not.
            correct = True
            dic = read.getFileContent()
            
            showDetail(dic)
            kittas = dic.keys() #Here only the key are stored where key is Kitta.

            ask = False
            while ask == False:
                validKitta = False
                while validKitta == False:
                    try:
                        Kitta = int (input("Enter kitta number: "))
                        if str(Kitta) in  kittas:
                            Kitta = str (Kitta)
                            
                            if dic[Kitta][-1] == "Available":
                                validAnna = False
                                while validAnna == False:
                                    
                                    Anna = int (input("Enter the anna of the land: "))
                                    
                                    if str(Anna)== dic[Kitta][2]:
                                        print("The kitta number "+ Kitta+" and anna "+ str(Anna)+" is rented successfully.")
                                        validAnna = True
                                        validMonths = False
                                        while validMonths == False:
                                            try:
                                                Months = int (input("Enter the duration of the months that you want to rent the land: "))
                                                if Months >0:
                                                    validMonths = True
                                                else:
                                                    print("Re-enter the duration of the months that you want to rent the land.")
                                            except:
                                                print("Please enter the duration of month in number.")
                                        dic[Kitta][-1] = "Not Available"
                                        tprice = Months * int (dic[Kitta][3])
                                        price[Kitta] = tprice
                                        mon[Kitta] = Months
                                        
                                        tempSellbill.append([Kitta,dic[Kitta][0],dic[Kitta][1],dic[Kitta][2],dic[Kitta][3],str(Months), str(tprice)])
                                        
                                    else:
                                        print("You have entered wrong anna of that kitta number.")
                            
                            else:
                                print("The entered kitta number is not available.")
                            validKitta = True
                            
                        else:
                            print("You entered wrong kitta number.")
                            print()
                    except:
                        print("Wrong Input!")
                counter = False
                while counter == False:
                    Ask = input("Do you want to rent more(yes/no)?")
                    if Ask.lower() == "yes":
                        ask = False
                        counter = True
                        showDetail(dic)
                    elif Ask.lower() == "no":
                        counter = True
                        ask = True
                        print("Thank you for using our Application! Your invoice is given below.")
                        print("\n")
                        write.update_Land(dic)
                        write.generate_bill(tempSellbill,Name,Address,Phone_num)
                    else:
                        
                        print("Invalid Input! Please enter yes or no...")
                
        else:
            print("Please enter the correct information.....!")
        
def return_land():
    tempSellbill = []
    global mon,price
    correct = False
    while correct == False:
        
        Name = input("Enter your name: ")
        Phone_num = input("Enter your number: ")
        Address = input("Enter your current temporary or permanent address: ")
        if Name.replace(" ","").isalpha() and Phone_num.isdigit():
            correct = True
            dic = read.getFileContent()
            
            showDetail(dic)
            kittas = dic.keys()

            ask = False
            while ask == False:
                validKitta = False
                while validKitta == False:
                    try:
                        
                    
                        Kitta = int (input("Enter kitta number: "))
                        Kitta = str (Kitta)
                        if Kitta in  kittas:
                            
                            if dic[Kitta][-1] == "Not Available":
                                
                                check = False
                                while check == False:
                                    try:
                                        months = int(input ("For how many months you had rented the "+ str(Kitta)+" kitta number?: "))
                                        if months <= 0:
                                            print("Enter a positive number")
                                        else:
                                            check = True
                                    except:
                                        print("Enter only number!")
                                try:
                                    if (int(months)) >  (int(mon[Kitta])): 
                                        fine = 1.2 * int (dic[Kitta][3]) * (int(months)-mon[Kitta]) # 1 is the full price of the land for exceeding months and 0.2 is the fine of the land 
                        
                                    else:
                                        fine = 0
                                    dic[Kitta][-1] = "Available"
                                    tempSellbill.append([Kitta,dic[Kitta][0],dic[Kitta][1],dic[Kitta][2],dic[Kitta][3],str(mon[Kitta]),str(months),str(fine),str(price[Kitta])])
                                except:
                                    print("Without renting land you can't return. Try again... ")
                            else:
                                print("The land will not able to return without renting.")
                            validKitta = True        
                        else:
                            print("The land is does not exist in database.")
                    except:
                        print("Please input valid information!!!")
                counter = False
                while counter == False:
                    Ask = input("Do you want to return more(yes/no)?")
                    if Ask.lower() == "yes":
                        counter = True
                        ask = False
                        showDetail(dic)
                    elif Ask.lower() == "no":
                        counter = True
                        ask = True
                        print("Thank you for using our Application! Your invoice is given below.")
                        print("\n")
                        write.update_Land(dic)
                        write.return_bill(tempSellbill,Name,Address,Phone_num)
                    else:
                        print("Invalid Input! Please enter yes or no...")
        else:
            print("Please enter the correct information.....!")
                            

def thankyou():
    print ("Thank for using the application")
    
    
