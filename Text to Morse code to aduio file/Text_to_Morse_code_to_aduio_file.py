import os
from pydub import AudioSegment, generators

# Morse Code Dictionary
MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'       ',
                    "'":'.----.'}  
def text_to_morse(text):
    morse = ''
    for char in text:
        if char != ' ':
            morse += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse += ' '
    return morse

def morse_to_audio(morse, output_path):
    dot = generators.Sine(440).to_audio_segment(duration=50)
    dash = generators.Sine(440).to_audio_segment(duration=150)
    space = AudioSegment.silent(duration=50)
    audio = AudioSegment.empty()
    for char in morse:
        if char == '.':
            audio += dot + space
        elif char == '-':
            audio += dash + space
        else:
            audio += AudioSegment.silent(duration=150)
    audio.export(output_path, format="wav")

def convert_text_to_morse_audio():
    text = input("Enter the text to be converted to Morse code: ")
    output_path = input("Enter the path where you want to save the .wav file: ")
    morse = text_to_morse(text)
    morse_to_audio(morse, output_path)

# Example usage:
convert_text_to_morse_audio()
