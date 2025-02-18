import sys

def check_args():
    if len(sys.argv) != 2:
        print("Error: invalid arguments")
        sys.exit(1)

def building(string):
    """
    Analyzes a given text and prints various character statistics.

    Parameters:
        string (str): The input text to analyze.

    Output:
        Prints the following statistics:
        - Total number of characters
        - Number of uppercase letters
        - Number of lowercase letters
        - Number of digits
        - Number of punctuation marks
        - Number of spaces
    """
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    print(f"The text contains {len(string)} characters:")
    print(f"{sum(1 for char in string if char.isupper())} uppercase letters")
    print(f"{sum(1 for char in string if char.islower())} lowercase letters")
    print(f"{sum(1 for char in string if char.isdigit())} digits")
    print(f"{sum(1 for char in string if char in punctuation_chars)} punctuation marks")
    print(f"{string.count(' ')} spaces")




def main():
    check_args()
    string = str(sys.argv[1])
    # print functio doc 
    print(building.__doc__)
    
    

if __name__ == "__main__":
    main()
