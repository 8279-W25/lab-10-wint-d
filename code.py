import time
from adafruit_circuitplayground import cp

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
def convert_to_morse(text):
    texts = text.strip().split()
    morse_text = []

    for text in texts:
        morse_char = []
        for char in text:
            if char in morse_code:
                morse_char.append(morse_code[char])
        if morse_char:
            morse_text.append(" ".join(morse_char))
    return "//".join(morse_text)

def morse_leds(bit, morse_time, brightness_level):
    cp.pixels.brightness = brightness_level
    if bit == '.':
        cp.pixels.fill((66, 245, 194))
        cp.play_tone(440, morse_time)
        time.sleep(morse_time)
        cp.pixels.fill((0, 0, 0))
        time.sleep(morse_time)
        
    elif bit == '-':
        cp.pixels.fill((66, 245, 194))
        cp.play_tone(440, morse_time * 3)
        time.sleep(morse_time * 3)
        cp.pixels.fill((0, 0, 0))
        time.sleep(morse_time)
    elif bit == ' ':
        time.sleep(morse_time)
    elif bit == '//':
        time.sleep(morse_time * 7)

while True:
    try:
        time_length = float(input("Enter time duration (between 0 and 1.0): "))
        brightness = float(input("Enter brightness (between 0 and 1.0): "))
        user_text = input("Enter sentence: ").lower()
        result = convert_to_morse(user_text)
        print("Morse code result:", result)

        for bit in result:
            morse_leds(bit, time_length, brightness)
            
    except ValueError:
        print("Invalid input. Please try again.")
            
    except ValueError:
        print("Invalid input. Please try again.")
