import time
from adafruit_circuitplayground import cp

# Morse code dictionary
morse_code = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.--',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}


# Function to covert user input to morse code
def convert_to_morse(text):
    # Delete leading and tailing whitespace with strip() and split each string by white space between words to make a list.
    texts = text.strip().split()
    # Covert string to morse code
    morse_text = []
    # For loop, to access in each text string.
    for text in texts:
        morse_char = []
        # For loop, to access in each character string in text string.
        for char in text:
            # Condition for checking each character is match the key character in morse dictionary.
            if char in morse_code:
                # If the character is matched, it will append the morse value of this character and store in morse_char list
                morse_char.append(morse_code[char])
        # After add the morse code into the morse list, this condition will check the morse_char list is not empty.
        if morse_char:
            # If the list is not an empty list, it will join all morse string with ' ' (whitespace) for 3 unit spaces and add it into morse_text list.
            morse_text.append(" ".join(morse_char))
    # return the morse_text result by join with '//' double slashes for 7 unit spaces from morse_text list to make a final morse string sentence
    return "//".join(morse_text)


# Function to turn on 10 LEDs and adjust the brightness
# the function receives 3 arguments; bit = character, morse_time = the morse duration time (0-1), brightness_level = led brightness (0-1)
def morse_leds(bit, morse_time, brightness_level, led_colors):
    # Set the brightness level to LEDs
    cp.pixels.brightness = brightness_level
    # if the character is '.'; 10 leds tuns on with teal color together play the sound with duration equal to morse_time.
    if bit == '.':
        cp.pixels.fill(led_colors)
        cp.play_tone(550, morse_time)
        time.sleep(morse_time)
        # after the morse_time, all leds turn off.
        cp.pixels.fill((0, 0, 0))
        time.sleep(morse_time)
    # if the character is '-'; 10 leds tuns on with teal color together play the sound with duration equal to morse_time * 3.
    elif bit == '-':
        cp.pixels.fill(led_colors)
        cp.play_tone(550, morse_time * 3)
        time.sleep(morse_time * 3)
        # after the morse_time * 3, all leds turn off.
        cp.pixels.fill((0, 0, 0))
        time.sleep(morse_time)
    # if the character is ' ' (space between each morse character); 10 leds still turn off and delay time equal to morse_time.
    elif bit == ' ':
        time.sleep(morse_time)
    # if the character is '//' (space between morse word); 10 leds still turn off and delay time equal to morse_time * 7.
    elif bit == '//':
        time.sleep(morse_time * 7)


# function to check valid value for time duration (between 0 and 1s)
def check_time():
    while True:
        try:
            time_length = float(input("Enter time duration (between 0.0 and 1.0): "))
            # this condition checks the time_length from user input is between 0 and 1. If it is not, It shows the error message and wait for user input a new value.
            if not (0 <= time_length <= 1.0):
                print("Time duration must be between 0.0 and 1.0.")
            else:
                return time_length
        except ValueError:
            print("Invalid input. Time duration must be number")


# function to check valid value for brightness level (between 0 and 1)
def check_brightness():
    while True:
        try:
            brightness_level = float(input("Enter brightness level (between 0.0 and 1.0): "))
            # this condition checks the brightness_level from user input is between 0 and 1. If it is not, It shows the error message and wait for user input a new value.
            if not (0 <= brightness_level <= 1.0):
                print("Brightness level must be between 0.0 and 1.0.")
            else:
                return brightness_level
        except ValueError:
            print("Invalid input. brightness level must be number")


# function to check valid color value for RGB (between 0 and 255)
def led_color():
    while True:
        try:
            red = int(input("Enter Red value (0 - 255): "))
            if not (0 <= red <= 255):
                print("Red value must be between 0 and 255.")
                continue

            green = int(input("Enter Green value (0 - 255): "))
            if not (0 <= green <= 255):
                print("Green value must be between 0 and 255.")
                continue

            blue = int(input("Enter Blue value (0 - 255): "))
            if not (0 <= blue <= 255):
                print("Blue value must be between 0 and 255.")
                continue
            return red, green, blue

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 255.")


def main():
    while True:
        try:
            # Receive user input for time duration (time_length) as a float value between 0 and 1.
            time_duration = check_time()
            # Receive user input for brightness level as a float value between 0 and 1.
            brightness = check_brightness()
            color = led_color()
            # Receive user string input as a lowercase.
            user_text = input("Enter sentence: ").lower()
            # call function to convert string to morse code
            result = convert_to_morse(user_text)
            print("Morse code result:", result)
            # for loop for play sound and turns on LEDs by each morse code character
            for bit in result:
                morse_leds(bit, time_duration, brightness, color)

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
