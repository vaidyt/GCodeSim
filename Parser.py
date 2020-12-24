from CommandType import CommandType

# Parser class to parse the g-code string
# This class parses the given line of the g-code
# and identifies the appropriate command and its parameters
class Parser:

    def __init__(self, raw_gcode_str: str):
        s = str.split(raw_gcode_str, '\n')
        self.gcode = list(filter(None, s))
        self.gcode = list(filter(str.strip, self.gcode))

    @staticmethod
    def __get_coord(s: str) -> float:
        if s[0] == 'X' or s[0] == 'Y':
            # ToDo: Handle invalid numeric string here
            c = float(s[1:])
            return c
        else:
            print("Error: Invalid G-Code format")
            raise

    @staticmethod
    def __parse_toggle_command(gcode_line):
        c = None
        if gcode_line[0] == 'M01':
            # we have a laser toggle instruction
            c = CommandType.LaserToggle
        else:
            c = CommandType.Unknown

        return c, None, None

    @staticmethod
    def __parse_move_command(gcode_line):
        x = None
        y = None
        c = CommandType.Unknown

        if gcode_line[0] == 'G01':
            x = Parser.__get_coord(gcode_line[1])
            y = Parser.__get_coord(gcode_line[2])
            c = CommandType.Go

        return c, x, y

    def parse(self, i: int):
        s = str.split(self.gcode[i])
        n = len(s)
        if n == 1:
            # Possibly a 'Toggle' command
            return Parser.__parse_toggle_command(s)
        elif n == 3:
            # Possibly a 'Go' command
            return Parser.__parse_move_command(s)

        return CommandType.Unknown, None, None

    def number_of_lines(self) -> int:
        return len(self.gcode)
