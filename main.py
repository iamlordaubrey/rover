from typing import Tuple

from constants import CARDINAL_POINTS, INPUT_FILE
from errors import invalid_landing_error, invalid_instructions_error, invalid_config_error
from utils import CircularList
from validators import validate_landing, validate_instructions, validate_new_rover_entry, validate_config_input


def control_rovers(rovers: dict) -> dict:
    new_location = {}

    for rover, detail in rovers.items():
        landing: list = detail['landing']

        landing_x = int(landing[0])
        landing_y = int(landing[1])
        current_cardinal = landing.pop()

        instructions: list = detail['instructions']

        cardinality = CircularList(CARDINAL_POINTS)

        for instruction in instructions:
            # check instruction is either L/R/M
            if instruction == 'L':
                current_cardinal = cardinality.previous(current_cardinal)
            elif instruction == 'R':
                current_cardinal = cardinality.next(current_cardinal)
            elif instruction == 'M':
                if current_cardinal == 'N':
                    landing_y += 1
                elif current_cardinal == 'E':
                    landing_x += 1
                elif current_cardinal == 'S':
                    landing_y -= 1
                elif current_cardinal == 'W':
                    landing_x -= 1
                else:
                    print('Never gets here')
                    raise
            else:
                print('Never gets here')
                raise

        new_location[rover] = f'{landing_x} {landing_y} {current_cardinal}'

    return new_location


def read_lines_in_2s(file_path: str) -> Tuple[list, dict]:
    rovers_detail = {}
    current_rover = 1

    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            config_input = input_file.readline().strip().split(':')[1].split()
            if not validate_config_input(config_input):
                print(invalid_config_error + f'\nCheck input file: {INPUT_FILE}\n')
                raise ValueError

            for rover_landing in input_file:
                rover_instructions = next(input_file)
                landing = rover_landing.split(':')[1].strip().upper().split()

                if not validate_landing(landing, config_input):
                    print(invalid_landing_error + f'\nCheck input file: {INPUT_FILE}\n')
                    raise ValueError

                instructions_input: str = rover_instructions.split(':')[1].strip().upper()
                instructions: list = [instruction for _, instruction in enumerate(instructions_input)]

                if not validate_instructions(instructions):
                    print(invalid_instructions_error + f'\nCheck input file: {INPUT_FILE}\n')
                    raise ValueError

                rovers_detail[f'Rover{current_rover}'] = {
                    'landing': landing,
                    'instructions': instructions,
                }

                current_rover += 1
    except StopIteration:
        # handles an odd-number of rows situation (Landing without Instructions or vice versa)
        pass

    return config_input, rovers_detail


def sentry(config_input: None | list = None, rovers: None | dict = None):
    if config_input is None or rovers is None:
        config_input, rovers = read_lines_in_2s(INPUT_FILE)

    new_location: dict = control_rovers(rovers)
    for rover, location in new_location.items():
        print(f'{rover}:{location}')


def should_prompt() -> bool:
    add_rover = 'Add a rover?\n'
    add_rover += 'Enter 0 for No, or 1 for Yes: '
    add_rover_error = 'Value should either be 0 or 1\n'

    user_input = input(add_rover)
    is_valid_integer = validate_new_rover_entry(user_input)

    if not is_valid_integer:
        print(add_rover_error)
        return should_prompt()

    elif int(user_input) == 0:
        return False

    return True


def get_configuration() -> list:
    invalid_config = True
    config_input = []

    while invalid_config:
        config_input: list = input('Configuration input (Upper-right coordinates): ').strip().split()
        invalid_config: bool = not validate_config_input(config_input)
        print(invalid_config_error) if invalid_config else None

    return config_input


def get_rovers(config_input: list) -> dict:
    rovers_detail = {}
    current_rover = 1
    landing = []
    instructions = []
    prompt = True

    while prompt:
        invalid_landing = True
        while invalid_landing:
            landing: list = input('Rover landing coordinates and cardinal point: ').strip().upper().split()
            invalid_landing: bool = not validate_landing(landing, config_input)
            print(invalid_landing_error) if invalid_landing else None

        invalid_instructions = True
        while invalid_instructions:
            instructions_input: str = input('Spin and movement: ').strip().upper()
            instructions: list = [instruction for _, instruction in enumerate(instructions_input)]
            invalid_instructions: bool = not validate_instructions(instructions)
            print(invalid_instructions_error) if invalid_instructions else None

        rovers_detail[f'Rover{current_rover}'] = {
            'landing': landing,
            'instructions': instructions,
        }

        current_rover += 1
        prompt = should_prompt()

    return rovers_detail


if __name__ == '__main__':
    # configuration_input: list = get_configuration()
    # rovers_dict: dict = get_rovers(configuration_input)

    # sentry(configuration_input, rovers_dict)
    sentry()  # delete this line
