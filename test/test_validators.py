from unittest import TestCase

from validators import (
    validate_config_input, validate_landing,
    validate_instructions, validate_new_rover_entry)


class ValidatorsTest(TestCase):
    def test_validate_config_input(self):
        config_input = ['5', '5']
        is_valid = validate_config_input(config_input)
        self.assertTrue(is_valid)

        config_input = ['a', '2']
        is_valid = validate_config_input(config_input)
        self.assertFalse(is_valid)

        config_input = ['-2', '3']
        is_valid = validate_config_input(config_input)
        self.assertFalse(is_valid)

    def test_validate_landing(self):
        config_input = ['5', '5']

        landing = ['1', '2', 'N']
        is_valid = validate_landing(landing, config_input)
        self.assertTrue(is_valid)

        false_landings = [['6', '1', 'N'], ['5', '1', 'A'], ['5', '1', '2'], ['-2', '1', 'N'],
                          ['0', 'N', 'N'], ['A', '2', 'N'], ['1', '2', 'W', 'E'], ['1', '2', 3]]
        for landing in false_landings:
            is_valid = validate_landing(landing, config_input)
            self.assertFalse(is_valid)

    def test_validate_instructions(self):
        instructions = ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']
        is_valid = validate_instructions(instructions)
        self.assertTrue(is_valid)

        instructions = ['L', 'M', 'N', 'M', 'L', 'M', 'L', 'M', 'M']
        is_valid = validate_instructions(instructions)
        self.assertFalse(is_valid)

    def test_validate_new_rover_entry(self):
        user_input = '0'
        is_valid = validate_new_rover_entry(user_input)
        self.assertTrue(is_valid)

        user_input = 'a'
        is_valid = validate_new_rover_entry(user_input)
        self.assertFalse(is_valid)

        user_input = 'yes'
        is_valid = validate_new_rover_entry(user_input)
        self.assertFalse(is_valid)
