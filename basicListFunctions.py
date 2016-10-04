#    Create an empty list named cars
#   Accept user input (raw_input) with types of cars
#    Add each new car to the end of the list
#    Stop accepting input when the user types done
#    Make sure that done does not exist in the list
#    Sort the cars alphabetically
#    Print the list of cars

cars = []
new_cars = ""
print ("Please enter type of car, when finished, please type done: \n")
while new_cars != "done":
    new_cars = raw_input("Enter a type of car: \n")
    if new_cars != "done":
        cars.append(new_cars)
cars.sort()
print ("\n")
print ("The list of cars you entered are: \n")
for car in cars:
    print car
