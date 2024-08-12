                    #================================================================
                    #============== Lesson 4: Assignments | Regex =============+=====
                    #================================================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1. Python Regular Expressions Mastery ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Task 1: Name Verification

    # Problem Statement:
        # Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.


    # Use the following list as an argument to test your function.

        # Code Example:
            # names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

    # Expected Outcome:

            # Abraham Lincoln
            # Andrew P Garfield
            # Invalid name
            # Connor Milliken
            # Jordan Alexander Williams
            # Invalid name
            # Invalid name

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================
import re

print("\n"*10,"="*125, "\n", "\n","="*125)
txt = "Task 1: Name Verification"
x = txt.center(125)
print (x, "\n")


def validate_names(names):
    pattern = r"^[A-Z][a-zA-Z\s]+$"
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
validate_names(names)


print("\n"*2,"="*125, "\n", "\n","="*125)

                                    #======= END OF CODE =========


# Author Roger Block