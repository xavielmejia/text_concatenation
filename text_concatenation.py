import pyperclip


def convert_text(char_separator, items_list, char_start_end=''):
    """
    function to convert list to a text concatenated by a particular character

    Pameters: \n
    char_separator: character to separate items in the list
    list_items: list of items to concatenate
    char_start_end [optional]: character to place at start and end of the string
    """
    result = char_separator.join(items_list)
    pyperclip.copy( char_start_end + result + char_start_end )

    print('Text successfully copy to clipboard!')


def text_concat():#items_list, output):
    """
    Function to concatenate values from a column in a particular format.

    Example: copy a range of value (single column) from excel, csv or text, run the script, select an option and the result will be on the clipboard

    Pameters: \n
    list_items: list of items to concatenate
    output_text: output to obtain 

    Options: \n
    1 or SQL: to convert to SQL format, Ex. 'a','b','c' \n
    2 or BO: to convert to Business Objects format, Ex. a;b;c \n
    3 or COMMA: to place a comma between values, Ex. a,b,c
    """

    text = pyperclip.paste()
    output = input("Where are you going to use the resulting concatenation? \n1.- SQL \n2.- BO (Business Objects) \n3.- COMMA (simple comma in the middle):\n")
    items_list = text.split('\r\n')

    if '' in items_list:
        list_items.remove('')

    if isinstance(output, str) and output.upper() in ['1','SQL']:
        convert_text("','", items_list, "'")

    elif isinstance(output, str) and output.upper() in ['2','BO']:
        convert_text(";", items_list)

    elif isinstance(output, str) and output.upper() in ['3','COMMA']:
        convert_text(",", items_list)

    else:
        print('The value inserted is not valid, try SQL or BO')

        try_again = input('Do you want to try again? y/n: ')
        if try_again.upper() == 'Y':
            text_concat()
        else:
            print('Program exited')


if __name__ == '__main__':
    text_concat()