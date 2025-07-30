import datetime
import operations
import read
import write

operations.welcome()
loop = True
while loop == True:
    
    option = operations.Demonstratingmessages()
    """ This option is the variable which store the information of Demonstratingmessages from operations """
    if option == "1":
        # This option is the variable which store the value given by the user.
        operations.rent_land()
    elif option == "2":
        operations.return_land()
    elif option == "3":
        operations.thankyou()
        loop = False
    else:
        print("Invalid Input...")
    
        
        
    
    
    
