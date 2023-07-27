from tabulate import tabulate 
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

        # initialising attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''

        # simply returns the cost attribute
        return self.cost

    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''

        # simply returns the quantity attribute 
        return self.quantity

    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.
        '''

        # returns all attributes in string format in a easy to read way
        return f'''\nCountry: \t{self.country}
Code: \t\t{self.code}
Product: \t{self.product}
Cost: \t\t{self.cost}
Quantity: \t{self.quantity}'''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    # using try except to check if the file exists 
    # reading all of the data from the text file and enumerating each line so that i can skip the first line
    # creating a shoe object with the contents of each line
    # appending shoe object to list of shoes objects
    try:
        with open("inventory.txt" , "r") as inv_file:
            for i,line in enumerate(inv_file):
                if i == 0:
                    pass
                else:
                    data = line.strip().split(",")  
                    shoe = Shoe(data[0],data[1],data[2],data[3],data[4]) 
                    shoe_list.append(shoe)
        print("\nAll shoes read into list successfully.")

    except Exception:
        print("File does not exist.")

def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    # capturing user input for the creation of the shoe object
    valid = True
    country = input("Enter they country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    try: 
        cost = float(input("Enter the cost: "))
    except:
        print("Invalid float.")
        valid = False

    try:
        quantity = int(input("Enter the quantity: "))
    except:
        print("Invalid integer.")
        valid = False

    # shoe object created using the variables from the user
    if valid == True:
        shoe = Shoe(country,code,product,cost,quantity)

        # shoe object added to list of all shoe objects
        shoe_list.append(shoe)

        with open("inventory.txt" , "a") as inv_file:
            inv_file.write(f"{country},{code},{product},{cost},{quantity}\n")
    else:
        print("One or more of the values that you entered are invalid. Please try again and pay close attention to the type of data you are entering.")

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    # creating a two dimensional array to dispaly all of the shoe information
    table = [['Country','Code','Product','Cost','Quantity']]

    # loop through all food objects and add each one as a list to the 2D arrya
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    # printing out the table using the tabulate module in python
    # i learned this here:
    # https://www.youtube.com/watch?v=Smf68icE_as&t=500s
    print(tabulate(table, headers = "firstrow", tablefmt = "fancy_grid"))



def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    # variable to store lowest quantity is created and set to the first shoe in the list of all shoe objects
    lowest_quant = shoe_list[0] 

    # loop through the entire shoe list
    # check if the quantity of the current object is less than that of the already set first object
    # if it is, the lowest quantity variable is then set to the current element
    for i in range(1,len(shoe_list)):
        if int(shoe_list[i].quantity) < int(lowest_quant.quantity):
            lowest_quant = shoe_list[i]

    # printing all information of object with lowest quantity
    print(lowest_quant)

    # user choice captured for if they want to restock the shoe
    choice = input("\nWould you like to restock on this shoe? (y/n): ").lower()

    # if the user chooses yes
    if choice == 'y':

        # they are asked the amount to restock by
        # this is added to the already existing quantity of the shoe and saved as rs_amount (re-stock amount)
        rs_amount = int(input("\nEnter the amount you would like to restock by: ")) + int(lowest_quant.quantity)

        # empty replace string created
        replace = ""

        # text file opened in read only mode
        with open("inventory.txt", "r") as inv_file:

            # each line of the file is looped through
            for line in inv_file:
                line = line.strip()

                # if the code of the shoe in the text file is the same as the lowest quantity object code
                # new is set to line
                # then the quantity in new is replaced with the updated restock amount
                if line.strip().split(',')[1] == lowest_quant.code:
                    new = line
                    new = new.replace(line.strip().split(',')[4], str(rs_amount))
                else:
                    new = line

                # for each iteration, replace is concatenated with new and a new line
                replace = replace + new + '\n'
        
        # the text file is then opened again in write mode and replace string is written to the file
        with open ("inventory.txt" , "w") as inv_file:
            inv_file.write(replace)

        # success message shown to user
        print(f"\nShoe was re-stocked successfully and now has a total of {rs_amount}.")

    elif choice == 'n':
        print("\nShoe will not be re-stocked.")
        pass

    else:
        print("\nYou did not enter a valid option.")
        pass

def search_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    # found flag set to false
    found = False

    # shoe code captured from user and stored in variable shoe_code
    shoe_code = input("\nEnter the code of the shoe: ")

    # loop through all shoe objects and if the code of a shoe object matches the input of the user, found is made True
    # the for loop is then broken out of to ensure shoe object is kept as the object with the matching code
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            found = True
            break

    # if the code was found, the shoe object is printed
    if found == True:
        print(shoe)

    # if the code is not found, an error message is presented to the user
    else:
        print(f"\nThe shoe code {shoe_code} does not exist.")  

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    # loop through all shoe objects in list
    # value calculated with value = cost * quantity
    # shoe product and code as well as calculated value are printed for each shoe object
    for shoe in shoe_list:
        value = float(shoe.cost) * float(shoe.quantity)
        print(f"\nName:\t\t{shoe.product}\nCode:\t\t{shoe.code}\nTotal Value:\tR{value}")

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    # highest quantity set to the first object in the shoe list
    highest_quant = shoe_list[0]

    # loop through all shoe objects and check if their quantity is greater than the current highest quantity
    # if it is, the highest quantity is then changed to the current object
    for shoe in shoe_list:
        if int(shoe.quantity) > int(highest_quant.quantity):
            highest_quant = shoe

    # the shoe with the highest quantity is then printed out
    print(f"\nThis shoe is for sale.\nShoe details:\n{highest_quant}")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main():

    read_shoes_data()

    while True:

        option = input('''\nRead shoe data\t\t -> rsd
Capture Shoe Details\t -> csd
View All\t\t -> va
Re-stock\t\t -> rs
Search Shoe\t\t -> ss
Value Per Item\t\t -> vpi
Highest Quantity\t -> hq
Exit\t\t\t -> e
: ''').lower()
        
        if option == 'rsd':
            read_shoes_data()
        
        elif option == 'csd':
            capture_shoes()
        
        elif option == 'va':
            view_all()
            
        elif option == 'rs':
            re_stock()

        elif option == 'ss':
            search_shoe()

        elif option == 'vpi':
            value_per_item()

        elif option == 'hq':
            highest_qty()

        elif option == 'e':
            print("\nGoodbye!")
            exit()
        
        else:
            print("\nYou have entered an invalid option. Please try again.")
main()