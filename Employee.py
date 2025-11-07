# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: 
# name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects 
# to hold the following data.

# Name	        ID Number	Department	    Job Title
# Susan Meyers	47899 	    Accounting	    Vice President
# Mark Jones	39119	    IT	            Programmer
# Joy Rogers	81774	    Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title


# Create three Employee objects
emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display the data for each employee
print("Employee 1:")
print("Name:", emp1.get_name())
print("ID Number:", emp1.get_id_number())
print("Department:", emp1.get_department())
print("Job Title:", emp1.get_job_title())
print()

print("Employee 2:")
print("Name:", emp2.get_name())
print("ID Number:", emp2.get_id_number())
print("Department:", emp2.get_department())
print("Job Title:", emp2.get_job_title())
print()

print("Employee 3:")
print("Name:", emp3.get_name())
print("ID Number:", emp3.get_id_number())
print("Department:", emp3.get_department())
print("Job Title:", emp3.get_job_title())
