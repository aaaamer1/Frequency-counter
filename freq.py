
import sys
from collections import Counter

def demo_command_line():
    # the first argument is the program name
    #print(sys.argv[0])
    # so the filename is the second argument
    filename = sys.argv[1]
    #print(filename)
    with open(filename) as file: #opens input argument file
        lst= [word for lines in file for word in lines.split()] #uses for loop to split words by spaces
    lst = sorted(lst) #sorts list of words lexicographically
    counter = dict() #creates empty dictionary
    for i in lst:
        if i in counter:
            counter[i] += 1 #add element to dictionary
        else:
            counter[i] = 1
    numb = len(lst) #counts number of words in list of sorted words
    with open(filename + ".out", 'w') as outfile:
        for i in counter:
            outfile.write(i + " " + str(counter[i]) + " " + str(round((counter[i]/numb),3)) + "\n") #prints word, the count of word, and the frequency
    outfile.close()
    file.close()
    
    return(filename)




















if __name__ == "__main__":
    cmdline = sys.argv
    if len(cmdline) < 2:
        print("Too few arguments. Usage: python3 freq.py <input file name>")
        exit
    elif len(cmdline) > 2:
        print("Too many arguments. Usage: python3 freq.py <input file name>")
        exit
    else: demo_command_line()
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    pass
