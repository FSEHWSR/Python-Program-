import datetime

def update_Land(dic):
    file = open("Lands.txt","w")
    for key,value in dic.items():
        file.write(key+",")
        for each in range(len(value)-1):
             file.write(value[each]+",")
        file.write(value[4])
        file.write("\n")

    
    file.close()


def generate_bill(data,Name,Address,phoneNumber):

    Year = (datetime.datetime.now().year)
    Month = (datetime.datetime.now().month)
    Day = (datetime.datetime.now().day)
    Hour = (datetime.datetime.now().hour)
    Minute = (datetime.datetime.now().minute)
    Second = (datetime.datetime.now().second)
    microSecond = (datetime.datetime.now().microsecond)
    
    print("*" * 120)
    print("                                    Invoice of Land                                                                          ")
    print("-" * 120)
    print("Date:- " + str(Year) + "-" + str(Month) + "-" + str(Day))
    print("Customer Name: " + Name)
    print("Phone Number: " + phoneNumber)
    print("Address: " + Address)
    print("-" * 120)
    print("Kitta", "\t\t", "City", "\t\t", "    Direction", "\t", "     Anna","\t" ,"Price","\t\t","Required Months","\t\t","Final Price")
    print("-" * 120)
    final_Price = 0
    
    
    
    
    
    text = "Rent_" + Name + str(Year) + str(Month) + str(Day) + str(Hour)+ str(Minute)+str(Second)+str(microSecond)+ ".txt"
    with open(text, "w") as file:
        
        file.write("*" * 120 + "\n")
        file.write("                                    Invoice of Land                                                                          \n")
        file.write("Date:- " + str(Year) + "-" + str(Month) + "-" + str(Day) + "\n")
        file.write("Customer Name: " + Name + "\n")
        file.write("Phone Number: " + phoneNumber + "\n")
        file.write("Address: " + Address + "\n")
        
        file.write("-" * 120 + "\n")
        file.write("-" * 120 + "\n")
        file.write("Kitta"+"\t\t"+"City"+"\t\t"+"   Direction"+"\t"+"     Anna"+"\t"+"Price"+"\t\t"+"Required Months"+"\t\t"+"Final Price"+"\n" )

        for each in data:
            print(each[0]+"\t\t"+each[1]+"\t\t"+ each[2]+"\t\t"+each[3]+"\t"+each[4]+"\t\t\t"+each[5]+"\t\t\t\t"+each[6])
            file.write(each[0]+"\t\t"+each[1]+"\t   "+ each[2]+"\t\t\t"+each[3]+"\t"+each[4]+"\t\t\t"+each[5]+"\t\t"+each[6]+"\n")
            final_Price = final_Price + int(each[6])
        print("-" * 120)
        print("The final price of the land is "+ str (final_Price)+" .")
        print("\n")
        print("-" * 120)

        file.write("-" * 120+"\n")
        file.write("The final price of the land is "+ str (final_Price)+" .")
        
        
            
def return_bill(data,Name,Address,phoneNumber):

    Year = (datetime.datetime.now().year)
    Month = (datetime.datetime.now().month)
    Day = (datetime.datetime.now().day)
    Hour = (datetime.datetime.now().hour)
    Minute = (datetime.datetime.now().minute)
    Second = (datetime.datetime.now().second)
    microSecond = (datetime.datetime.now().microsecond)
    
    print("*" * 160)
    print("                                    Invoice of Land                                                                          ")
    print("-" * 160)
    print("Date:- " + str(Year) + "-" + str(Month) + "-" + str(Day))
    print("Customer Name: " + Name)
    print("Phone Number: " + phoneNumber)
    print("Address: " + Address)
    print("-" * 160)
    print("Kitta", "\t\t", "City", "\t\t", "    Direction", "\t", "     Anna","\t" ,"Price","\t\t","Stated Months","\t\t","Current Month","\t\t","Fine""\t\t","Initial Price")
    print("-" * 160)
    final_Price = 0
    total_fine = 0
    
    
    
    
    
    
    text = "Return_" + Name + str(Year) + str(Month) + str(Day) + str(Hour)+ str(Minute)+str(Second)+str(microSecond)+ ".txt"
    with open(text, "w") as file:
        
        file.write("*" * 160 + "\n")
        file.write("                                    Invoice of Land                                                                          \n")
        file.write("Date:- " + str(Year) + "-" + str(Month) + "-" + str(Day) + "\n")
        file.write("Customer Name: " + Name + "\n")
        file.write("Phone Number: " + phoneNumber + "\n")
        file.write("Address: " + Address + "\n")
        
        file.write("-" * 160 + "\n")
        file.write("-" * 160 + "\n")
        file.write("Kitta"+"\t\t"+"City"+"\t"+"    Direction"+"\t"+"      Anna"+"\t"+"Price"+"\t\t"+"Stated Months"+"\t\t"+"Current Month"+"\t\t"+"Fine""\t\t"+"Initial Price"+"\n")
    
        for each in data:
            print(each[0],"\t\t",each[1],"\t\t",each[2],"\t\t",each[3],"\t",each[4],"\t\t",each[5],"\t\t\t",each[6],"\t\t",each[7],"\t\t",each[8])
            file.write(each[0]+"\t\t"+each[1]+"\t"+ each[2]+"\t\t"+each[3]+"\t"+each[4]+"\t\t\t"+each[5]+"\t\t  "+each[6]+"\t\t     "+each[7]+"\t\t"+each[8]+"\n")
            final_Price = final_Price + int(each[8])
            total_fine = total_fine + int(float(each[7]))
        grand_total = total_fine + final_Price
            
        print("-" * 160)
        print("The fine price of the land is "+ str (total_fine)+"\n")
        print("-" * 160)
        print("The final price after fine of the land is "+ str (final_Price)+"\n")
        print("-" * 160)
        print("The grand total price of the land is "+ str (grand_total)+"\n")
        print("-" * 160)

        file.write("-" * 160+"\n")
        file.write("The fine price of the land is "+ str(total_fine)+"\n")
        file.write("-" * 160+"\n")
        file.write("The final price after fine of the land is "+ str (final_Price)+"\n")
        file.write("-" * 160+"\n")
        file.write("The grand total price of the land is "+ str (grand_total)+"\n")
        file.write("-" * 160+"\n")
        
            


