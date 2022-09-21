from constants import CARDINAL_POINTS, VALID_INSTRUCTIONS


def validate_config_input(config_input: list) -> bool:
    if len(config_input) != 2:
        return False

    try:
        config_x_int = int(config_input[0])
        config_y_int = int(config_input[1])
    except (ValueError, SyntaxError):
        return False

    if config_x_int < 0 or config_y_int < 0:
        return False

    return True


def validate_landing(landing: list, config_input: list) -> bool:
    if len(landing) != 3:
        return False

    try:
        landing_x_int = int(landing[0])
        landing_y_int = int(landing[1])
    except (ValueError, SyntaxError):
        return False

    if (landing_x_int < 0
            or landing_y_int < 0
            or landing_x_int > int(config_input[0])
            or landing_y_int > int(config_input[1])):
        return False

    if landing[2] not in CARDINAL_POINTS:
        return False

    if not type(landing[2]) == str:
        return False

    return True


def validate_instructions(instructions: list) -> bool:
    return set(instructions).issubset(VALID_INSTRUCTIONS)


def validate_new_rover_entry(user_input) -> bool:
    try:
        if int(user_input) in (0, 1):
            return True
    except ValueError:
        pass
    return False
