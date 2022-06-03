# Pickling and Handling Exceptions in Python:

## Introduction: 
This paper aims to demonstrates pickling and exception handling feature in python. I explained these features by creating a python script that displays the birth year of a user when the user inputs their current age. The latest version of PyCharm Community version is used for this assignment on a Mac OS.

## Python script displaying the birth year of an user based on their current age:

My script asks the user to input their current age and based on that, it displays the birth year of the user.

I started by creating a new sub-folder called Assignment07 inside of the \_PythonClass folder (you created in Module 01) in the Documents folder on a Mac OS. Then I created a new project in PyCharm that uses the \_PythonClass\Assignment07 folder as its location.

Then global variables used throughout the code were defined as seen in Figure 1.

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/Picture1.png)
## Figure 1. Snippet of the python script defining the global variables

To keep my data processing distinct from my display, I employ custom functions. I have functions for saving and reading data. These not only pickle or unpickle data, but also contain a try/except block to capture failures. This can happen when there is no file with that name, like when reading a file, or if there is some subtle error with the file name or data (basically the arguments) for saving the data.

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/Picture2.png)

## Figure 2. Pickling data using Try and Except

Enter the age to list in memory option first asks the user to enter their current age, then asks user which operations they want to conduct on them, and then finally, it displays their year of birth as output.

Try/except blocks were used to catch if the user does not enter their age between 0 and 100 as shown in figure 3.

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/3.png)

## Figure 3. Exception handling in python using Try and Except

The script is the class consists of functions that process the data to read, add, remove and write data to the file. Code was added after explaining the parameters to add, remove and write data to the list.

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/4.png)

## Figure 4. Snippet of the python script to add data to the file

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/5.png)

## Figure 5. Snippet of the python script to display a menu of choices to the user as output

Run the Script by right clicking on the file and choosing Run.

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/6.png)

## Figure 6. Snippet of output displayed in PyCharm Shell after running the python script.

I chose the 1st option to enter my age to list in memory. On entering my age as 25, the program displayed my birth year as 1997 as shown in Figure 6.

Run the script on the Terminal window

![](https://github.com/nikitadaharia/IntroToProg-Python-Mod07/blob/main/images/7.png)

## Figure 7. Output displayed in Terminal window after running the python script.

Lastly, the binary file age.dat was located and opened in the text editor to verify that it worked. The text editor could not render the data in a text format because the data is a serialized python object.

**Summary:**

Python is a simple yet powerful language programming language that runs on Windows, Linus/Unix, and Mac OS. I used PyCharm to create a python script that asks the user to input their current age and based on that, it displays the birth year of the user.

The script was run both in PyCharm and Terminal. Finally, the code was verified by locating the binary file age.dat and opening it in a text editor.
