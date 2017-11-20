
def print_dict(dictionary):
    for keys in sorted(dictionary):
        print(dictionary[keys]['first name'], end=' ')
        print(dictionary[keys]['last name'], end=': ')
        print(dictionary[keys]['position'], end=', ')
        print(dictionary[keys]['department'], end=', $')
        print(dictionary[keys]['salary'], end=' per year ')
        print()


def output(dictionary, name):
    print("Business name: "+name+"\n")
    f = open("Gonzalez_HW1_output.txt", "w")
    f.write("Business name: "+name+"\n\n")
    count = 0
    for keys in sorted(dictionary):
        print(keys, "has", len(dictionary[keys]), "employee(s):")
        f.write("%s has %s employee(s):\n" % (keys,len(dictionary[keys])))
        for i in dictionary[keys]:
            f.write("%s %s: %s, %s, $%s per year\n" % (i['first name'], i['last name'], i['position'], i['department'], i['salary']))
            print(i['first name'], end=' ')
            print(i['last name'], end=': ')
            print(i['position'], end=', ')
            print(i['department'], end=', $')
            print(i['salary'], end=' per year.')
            print()
            count += 1
        f.write("\n")
        print()
    print("Total number of employees:",count)
    f.write("Total number of employees: "+str(count))

def main():
    dep = ()
    emp = {}
    name = ""

    while True:
        try:
            print()
            print("0 = Enter name of Business")
            print("1 = Enter department name")
            print("2 = Add and employee")
            print("3 = Change an employee name")
            print("4 = Promote an employee to a new position")
            print("5 = Give an employee a rise")
            print("6 = Output all employees")
            print("7 = Check if an employee exists")
            print("8 = End the program")
            # This makes sure user enters a number as an option and not anything else.
            choice = int(input("Please select your choice: "))
            print()
        except:
            print("Input is not an option in menu")
            choice = 9
        if choice == 0:
            # Enter name for business if it doesn't exist yet.
            if name == "":
                name = input("What is the name you would like to give? ")
            else:
                print("There's already a name for this business.")

        elif choice == 1:
            # Here is where user inputs department names
            dept = input("Enter Department Name: ")
            if dept in dep:
                print("Department already here.")
            else:
                dep += (dept,)

        elif choice == 2:
            # Entering new employee's information
            first = input("Enter Employee's First Name: ")
            last = input("Enter Employee's Last Name: ")
            emp_name = first + " " + last
            emp_pos = input("Enter " + emp_name + "'s position: ")
            emp_dep = input("Enter " + emp_name + "'s department: ")
            # We must first check to see if department is in the database
            while emp_dep not in dep:
                print("\nDepartment not found. Try again. If you want to add a new department type 'new'")
                emp_dep = input("Enter " + emp_name + "'s department: ")
                # if department not found, can give user the option to input the department
                if emp_dep == "new":
                    dept = input("Enter New Department Name: ")
                    #adds department to tuple containing department names
                    dep += (dept,)
                    emp_dep = dept
                    break
            try:
                # Transform input into numeric form to add later
                emp_sal = eval(input("Enter " + emp_name + "'s salary (integers only, no commas): "))
                # Adds employee to employee dictionary
                emp[emp_name] = {'first name': first, 'last name': last, 'position': emp_pos,
                                 'department': emp_dep, 'salary': emp_sal}
            except:
                print("Input given for salary is not an integer. Please try again.")

        elif choice == 3:
            # option to change employee's name.
            old = input("Enter the Employee's Full Name who you want to change his/her name: ")
            # we must first check to see if employee is in the database.
            if old not in emp:
                print("Input is not in Employee database")
            else:
                first2 = input("Enter the new first name you want to give: ")
                last2 = input("Enter the new last name you want to give: ")
                new = first2 + " " + last2
                emp[new] = emp.pop(old)
                # Updating values in the emp dictionary as well.
                emp[new]["first name"] = first2
                emp[new]["last name"] = last2

        elif choice == 4:
            emp1 = input("Enter the Employee's Full Name who you want to change position: ")
            # check to see that emp is in the database here
            if emp1 not in emp:
                print("Employee not found.")
            else:
                new_pos = input("Enter " + emp1 + " new position: ")
                emp[emp1]["position"] = new_pos

        elif choice == 5:
            emp2 = input("Enter Employee's Full name of who you like to give a raise: ")
            if emp2 not in emp:
                print("Employee not found")
            else:
                try:
                    raise_1 = eval(input("Enter raise amount: "))
                    emp[emp2]["salary"] = emp[emp2]["salary"] + raise_1
                except:
                    print("Input given for raise is not a number. Please try again.")

        elif choice == 6:
            # prints Employee List by calling the function print_dict
            print("Employee List:")
            print_dict(emp)

        elif choice == 7:
            # checks to see if employee is in database.
            check1 = input("Provide name you would like to search for (Case-Sensitive): ")
            if check1 in emp:
                print('Yes,', check1, ' is here')
            else:
                # if employee is not in the database, lets user input new employee
                print("Employee not currently found.")
                # code below is exactly the same as choice = 2 above.
                first = input("Enter Employee's First Name: ")
                last = input("Enter Employee's Last Name: ")
                emp_name = first + " " + last
                emp_pos = input("Enter " + emp_name + "'s position: ")
                emp_dep = input("Enter " + emp_name + "'s department: ")
                while emp_dep not in dep:
                    print("\nDepartment not found. Try again. If you want to add a new department type 'new'")
                    emp_dep = input("Enter " + emp_name + "'s department: ")
                    if emp_dep == "new":
                        dept = input("Enter New Department Name: ")
                        dep += (dept,)
                        emp_dep = dept
                        break
                try:
                    emp_sal = eval(input("Enter " + emp_name + "'s salary (integers only, no commas): "))
                    emp[emp_name] = {'first name': first, 'last name': last, 'position': emp_pos, 'department': emp_dep,
                                     'salary': emp_sal}
                except:
                    print("Input given for salary is not a number. Please try again.")

        elif choice == 8:
            # Prints Departments and the employees in it.
            # First create a dictionary to contain the department lists
            dep_list = {}
            # The keys for dep_list are the values in the tuple that contain department names while the values
            # are empty lists to be populated by the employee dictionary
            for i in dep:
                dep_list[i] = list()
            #Sorts employee dictionary by last names so that they are added alphabetically to the department lists
            for keys in sorted(emp, key=lambda k: emp[k]["last name"]):
                dep_list[emp[keys]['department']].append(emp[keys])
            print("Goodbye\n")
            # calls output function to create output text file
            output(dep_list, name)
            break
        else:
            # tells user he/she did not enter a correct input.
            print("Wrong Input. Please try again")


main()
