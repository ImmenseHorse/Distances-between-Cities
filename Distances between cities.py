#This program was written by Duc Nguyen on Jan 18, 2020.
#This program asks the user for the starting city and for the destination city,
#and then tells the user the distance between the two places (in km). This
#program will continue until the user indicates they are done.

CITIES = "cities.txt"
DISTANCES = "distances.txt"

def Fill1D(filename):
    """This function accepts a filename and returns a one-dimensional list of
    stripped strings"""

    in_file = open(filename, "r")
    onedlist = in_file.readlines()
    in_file.close()
    
    for x in range(len(onedlist)):
        onedlist[x] = onedlist[x].strip()
    return onedlist


def Fill2D(filename,length):
    """This function accepts a filename, a length and returns a two-dimensional
    list of stripped strings"""

    in_file = open(filename, "r")
    
    twodlist = []
    for x in range(length):
        row = []
        for y in range(length):
            row.append(in_file.readline().strip())
        twodlist.append(row)
    return twodlist

def GetValidInput(alist,prompt,errormessage):
    """This function accepts a one-dimensional list, a prompt, and an error
    message, and then returns the index in the list that corresponds with the
    user's reply"""

    print()
    keepgoing = True
    while keepgoing:
        entry = input(prompt)
        for x in range(len(alist)):
            if entry.capitalize() == alist[x]:
                return x
        print(errormessage)
        entry = input(prompt)
        
def main():    
    print("This program will determine the distance between the following cities:")
    print("Toronto Montreal Vancouver Fredericton Edmonton")

    onedlist = Fill1D(CITIES)
    twodlist = Fill2D(DISTANCES,5)
    
    reply = "y"
    while reply == "y":
        row = GetValidInput(onedlist,"Starting city: ","Invalid city")
        print()
        column = GetValidInput(onedlist,"Destination city: ","Invalid city")
                
        print("The distance between",onedlist[row],"and",onedlist[column],"is",
              twodlist[row][column],"km.")

        reply = input("Do another one? (y/n) ").lower()
main()
    




    
    


