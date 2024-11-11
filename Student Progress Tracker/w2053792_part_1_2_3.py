
from graphics import *

# Initializing variables, lists and dictionary
data_list = []
column = [0, 0, 0, 0]
colors = ["palegreen", "yellowgreen", "olive", "lightpink"]
outcomes = ["Progress", "Trailer", "Retriever", "Exclude"]
outcome_index = {"Progress": 0, "Progress (Module trailer)": 1, "Module retriever": 2, "Exclude": 3}

# Function to determine progress based on credits
def progress(Pass, defer, fail):
    if Pass == 120:
        return "Progress"
    elif Pass == 100:
        return "Progress (Module trailer)"
    elif Pass <= 80 and defer >= 0 and fail <= 60:
        return "Module retriever"
    elif fail >= 80:
        return "Exclude"
    
# Function to validate credits
def credits_Check(credits):
    if credits > 120 or credits  not in [0, 20, 40, 60, 80, 100,120]:
        print("Out of range")
        return False
    return True

# Function to create and display histogram
def create_histogram(columns):
    win = GraphWin("Histogram", 550, 600)
    
    # Creating the title for the histogram results to display
    title = Text(Point(150, 25), "Histogram Results")
    title.setSize(17)
    title.setStyle("bold")
    title.setTextColor("gray")
    title.draw(win)
    
    # Creating the total outcomes to display
    total = Text(Point(150, 560), f"{sum(columns)} outcomes in total.")
    total.setSize(15)
    total.setStyle("bold")
    total.setTextColor("gray")
    total.draw(win)

    # Drawing histogram bars and labels
    line = Line(Point(30, 500), Point(520, 500))
    line.draw(win)
              
    # Generating and displaying the histogram bars and labels for each outcomes
    for i in range(4):
        x_start = i * 120
        column = Rectangle(Point((x_start + 40), 500), Point((x_start + 140), (500 - columns[i] * 25)))
        No_of_outcomes = Text(Point((x_start + 90), (490 - columns[i] * 25)), columns[i])
        label = Text(Point((x_start + 90), 520), outcomes[i])
        column.setFill(colors[i])
        No_of_outcomes .setStyle("bold")
        No_of_outcomes .setTextColor("gray")
        label .setStyle("bold")
        label.setTextColor("gray")
        column.draw(win)
        No_of_outcomes.draw(win)
        label.draw(win)

    return win


# User selection for login
while True:
    try:
        user = int(input("Enter 01 for student login.\nEnter 02 for staff login.\nEnter a number: "))
        
        if user not in [1, 2]:
            print("Invalid input. Enter 01 or 02.")
            continue
        
        break
    
    except ValueError:
        print("Invalid input. Integer required.")
        continue

# Taking data from user
while True:
    try:
        Pass = int(input("Enter your total PASS credits: "))
        if not credits_Check(Pass):
            continue
        
        defer = int(input("Enter your total DEFER credits: "))
        if not credits_Check(defer):
            continue
    
        fail = int(input("Enter your total FAIL credits: "))
        if not credits_Check(fail):
            continue
        
        # Checking if the total credits add up to 120
        if Pass + defer + fail != 120:
            print("Total is Incorrect")
            continue
        
        # Calculating the result based on credits
        result = progress(Pass, defer, fail)
        print(result)
        
        if result in outcome_index:
            column[outcome_index[result]] += 1
            
        # Storing the outcome and credit details in a list   
        data_list.append((result, Pass, defer, fail))

        if user == 1 :
            exit()
            
        else:
            while True:
                choice = input("Would you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ")
                # Checking if the input is not 'q' or 'y'
                if choice.lower() in ['q','y']:
                    break
                else:
                    print("Invalid input. Enter 'y' or 'q'.")
                    continue
                    
            if choice.lower() == 'q':
                break
            elif choice.lower() == 'y':
                continue
          
    except ValueError:
        print("Invalid input. Integer required.")
        
# Displaying collected data 
for data in data_list:
    print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")

# Writing collected data to a file
with open('List_data.txt', 'a') as file:
    for data in data_list:
        file.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")
        
# Generating and displaying histogram
create_histogram(column)
