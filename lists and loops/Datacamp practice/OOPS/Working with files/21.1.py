#Ask the user what acronym they want to look up?
#open the file for reafing
#Read each line of the file
#Check if current acronym matches the users acronym
#Print the definition

#Location is important...
look_up =input("What software acronym would you like to look up?\n")
found = False
with open('acronyms.txt') as file:
    for line in file:
        if look_up in line :
            print(line)
            found = True
            break
if not found:
    print('The acronym does not exist')