"""
***************************************************************************
Filename:      lab3.py

Author:        Omurbek Kurmanbekov

Date:          2024.10.16

Description:   This module demonstrates the use of functions to:
               1) perform indentation
               2) center a string on the screen

***************************************************************************
"""

def indent(string, spaces):
    """
    ***************************************************************************

    Function: indent(string, spaces)

    Parameters:
        string - string to be printed
        spaces - number of spaces to be indented for printing

    Outputs:
        Prints the string with indentation specified by "spaces"

    Returns:
        None

    Author: Omurbek Kurmanbekov

    Date: 2024.10.16

    Description:
    This function prints a string with a specified number of white spaces indented.
    The first parameter is a string literal or variable.
    The second parameter is the number of white spaces to be indented.

    ***************************************************************************
    """
    print(' ' * spaces + string)

# Test cases
indent("Hello", 0)
indent("Hi", 5)

def center(string, screen_width):
    """
    ***************************************************************************

    Function: center(string, screen_width)

    Parameters:
        string - string to be centered
        screen_width - the width of the screen

    Outputs:
        Prints the string centered within the screen width

    Returns:
        The number of spaces used to center the string

    Author: Omurbek Kurmanbekov

    Date: 2024.10.16

    Description:
    This function prints a string centered based on the specified screen width
    by calculating the necessary indentation using the indent function.

    ***************************************************************************
    """
    # Calculate spaces for center alignment
    spaces = (screen_width - len(string)) // 2
    indent(string, spaces)
    return spaces

# Test case
spaces = center("my lucky number is 888", 80)
print(f"Indented by {spaces} white spaces")


def read_n_center_text():
    """
    ***************************************************************************

    Function: read_n_center_text()

    Inputs:
        Prompts the user for a text string and a screen width

    Outputs:
        Prints the centered text and displays the number of spaces it was indented by

    Returns:
        None

    Author: Omurbek Kurmanbekov

    Date: 2024.10.16

    Description:
    This function prompts the user for a text string and a screen width, then
    centers the text by calling the center function. It also prints how many
    white spaces were used for indentation.

    ***************************************************************************
    """
    # User input
    text = input("Type Text String: ")
    screen_width = int(input("Enter Screen Width: "))

    # Centering the text
    spaces = center(text, screen_width)
    print(f"Indented by {spaces} white spaces")


# Running the main function
if __name__ == "__main__":
    read_n_center_text()


# Record of Execution
"""
Hello
     Hi
                             my lucky number is 888
Indented by 29 white spaces 
Type Text String: Omurbek
Enter Screen Width: 400
                                                                                                                                                              
                                      Omurbek
Indented by 196 white spaces
"""