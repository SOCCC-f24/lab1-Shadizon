#!/usr/bin/python3
"""
    temp_converter.py
    Andrew Gomez
    09/05/2024
    CSC138-EN
"""
# process
def c2f(c):
    return (9.0 / 5.0 * c) + 32
    #Converts the input from Celsius to Fahrenheit
def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = 100         # input
    print(main(cel))  # output
