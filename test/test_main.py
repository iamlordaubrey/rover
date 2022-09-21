import io
from unittest import TestCase, mock

from main import (
    sentry, get_configuration, get_rovers,
    should_prompt, read_lines_in_2s, control_rovers)


# End-To-End tests
class RoverEndToEndTest(TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_via_input_file(self, mock_stdout):
        sentry()
        self.assertIn('Rover1:1 3 N', mock_stdout.getvalue())
        self.assertIn('Rover2:5 1 E', mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_via_command_line(self, mock_stdout):
        config_input = ['5', '5']
        rovers_dict = {
            'Rover1': {
                'instructions': ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M'],
                'landing': ['1', '2', 'N']
            }
        }

        sentry(config_input, rovers_dict)
        self.assertIn('Rover1:1 3 N', mock_stdout.getvalue())


# Unit tests
class RoverUnitTest(TestCase):
    file_content = '''Plateau:5 5
        Rover1 Landing:1 2 N
        Rover1 Instructions:LMLMLMLMM
        Rover2 Landing:3 3 E
        Rover2 Instructions:MMRMMRMRRM
        '''

    def setUp(self):
        self.rover_response = {
            'Rover1': {
                'instructions': ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M'],
                'landing': ['1', '2', 'N']
            },
            'Rover2': {
                'instructions': ['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M'],
                'landing': ['3', '3', 'E']
            }
        }

    @mock.patch('main.input', create=True)
    def test_get_config(self, mocked_input):
        mocked_input.side_effect = ['5 5']
        config = get_configuration()
        self.assertEqual(config, ['5', '5'])

    @mock.patch('main.input', create=True)
    def test_get_rovers(self, mocked_input):
        mocked_input.side_effect = ['1 2 N', 'LMLMLMLMM', '0']
        rovers = get_rovers(['5', '5'])

        self.assertLessEqual(rovers.items(), self.rover_response.items())

    @mock.patch('main.input', create=True)
    def test_should_prompt(self, mocked_input):
        mocked_input.side_effect = ['0']
        response = should_prompt()
        self.assertFalse(response)

        mocked_input.side_effect = ['1']
        response = should_prompt()
        self.assertTrue(response)

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data=file_content)
    def test_read_lines_in_2s(self, mock_file):
        config_input, rover_detail = read_lines_in_2s('path/to/file')

        mock_file.assert_called_with('path/to/file', 'r', encoding='utf-8')
        self.assertEqual(config_input, ['5', '5'])
        self.assertEqual(rover_detail, self.rover_response)

    def test_control_rovers(self):
        control_location = {'Rover1': '1 3 N', 'Rover2': '5 1 E'}
        new_location = control_rovers(self.rover_response)
        self.assertEqual(new_location, control_location)
