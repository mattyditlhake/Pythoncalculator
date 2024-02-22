#define each conversion that has to take place
def meter_to_kilometer(meter):
    return meter/1000
def kilometer_to_meter(kilometer):
    return kilometer*1000
def feet_to_meters(feet):
    return feet*0.3048
def meter_to_feet(meters):
    return meters/0.3048
def miles_to_kilmeters(miles):
    return miles*1.60934
def kilometer_to_miles(kilmeters):
    return kilmeters/1.60934

#This is the main function which holds the conversions are are going to take place
def main():
    #This is a welcoming message hence it is written in a print() statement
    print("Welcome to the conversion calculator!!")
    
    #While statement has
    while True:
        print("\nChoose conversion option:")
        print("1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        print("3. Feet to Meters")
        print("4. Meters to Feet")
        print("5. Miles to Kilometers")
        print("6. Kilometers to Miles")
        print("0. Exit")
        
        #This statement which has variable=input(""), prompts the user to input a value
        choice = input("Enter your choice(0-6):") #In this case choice=input("Enter your choice(0-6)") this the user the available choices
        #The choice variable is assigned to a value in the first statement which prompts(choice=input("")) and in this next statement a comparison between the assigned values is made 
        if choice == '0':
            print("Exiting the Coversion Calculator. Goodbye!")
            break
        try:
            #This is the variable that holds the number which has to be converted.
            value = float(input("Enter the value to convert:"))
        except ValueError:
            print("Invalid input.Please enter a valid number")
            continue 
        #This piece of code indicates what will happen if the user presses 1
        if choice =='1':
            results=meter_to_kilometer(value)
            print(f"{value}meters is equal to {results} kilometers")
        #This is what will happen if the user presses 2    
        elif choice =='2':
            results=kilometer_to_meter(value)
            print(f"{value}kilometer is equal to {results} meter")
        elif choice =='3':
            results=feet_to_meters(value)
            print(f"{value}feet is equal to {results}meters")
        elif choice == '4':
            results=meter_to_feet(value)
            print(f"{value}meters is equal to {results}")
        elif choice =='5':
            results=miles_to_kilmeters(value)
            print(f"{value}miles to {results}kilometers")
        elif choice == '6':
            results=kilometer_to_meter(value)
            print(f"{value}kilometers is equal to {results}miles")
        else:
            print("Invalid Choice")
        
        
if __name__=="__main__":
    main()