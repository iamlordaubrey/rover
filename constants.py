import os

dir_path = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(dir_path, 'input.txt')

CARDINAL_POINTS = ['N', 'E', 'S', 'W']  # Maybe make this a set??
VALID_INSTRUCTIONS = ['L', 'R', 'M']
