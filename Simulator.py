import numpy as np
import CommandType as CT
import Parser
import LineSeg2D as LS


class Simulator:

    # Constructor to create a simulator object
    # raw_gcode_str is the gcode as a raw string
    # n_rows is the number of rows in the grid
    # n_clos is the number of columns in the grid
    def __init__(self, raw_gcode_str: str, n_rows: int, n_cols: int):
        self.raw_gcode_str = raw_gcode_str
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.parser = Parser.Parser(raw_gcode_str)
        self.x = 0
        self.y = 0
        self.laserHeadRadius = 0.5
        self.laser = False
        self.number_of_commands = self.parser.number_of_lines()
        self.grid = np.zeros((n_rows, n_cols), dtype=bool)
        self.command = CT.CommandType.Unknown

    # Turns on a given cell (if it is not already turned on)
    def __turn_on_cell(self, x_int: int, y_int: int):
        if not self.grid[y_int, x_int]:
            self.grid[y_int, x_int] = True

    # Updates the position of the laser head i.e. overwrites old x,y with the new x,y
    def __set_xy(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    # This method etches all the cells of the grid that are within
    # laser head radius distance from the laser path
    def __mark_laser(self, new_x: float, new_y: float):
        line = LS.LineSeg2D(self.x, self.y, new_x, new_y)

        for Y in range(self.n_rows):
            for X in range(self.n_cols):
                if line.distance_from_pt([X, Y]) <= self.laserHeadRadius:
                    self.__turn_on_cell(X, Y)

    # processes the laser command
    def __process_laser_command(self):
        if self.laser:
            self.__mark_laser(self.x, self.y)

        self.laser = not self.laser

    # processes the go command
    def __process_go_command(self, new_x: float, new_y: float):
        if self.laser:
            self.__mark_laser(new_x, new_y)

        self.__set_xy(new_x, new_y)

    # checks if the new_x and new_y are withing the bounds of the grid
    def __is_within_bounds(self, new_x: float, new_y: float) -> bool:
        return 0 <= new_x <= self.n_cols and 0 <= new_y <= self.n_rows

    # checks if the command is valid and/or X,Y coordinates are within bounds of the grid
    def __check_validity(self, new_x: float, new_y: float) -> bool:
        s = True
        if self.command == CT.CommandType.Unknown:
            print('Unknown command in G-Code; Currently, we only support G01 and M01 commands')
            s = False
        elif self.command == CT.CommandType.Go and not self.__is_within_bounds(new_x, new_y):
            print('Coordinate out of bounds; Please check the input coordinates in G-Code')
            s = False

        return s

    # Orchestrator method that handles the current command
    def __process(self, new_x: float, new_y: float):
        if not self.__check_validity(new_x, new_y):
            raise
        if self.command == CT.CommandType.LaserToggle:
            self.__process_laser_command()
        elif self.command == CT.CommandType.Go:
            self.__process_go_command(new_x, new_y)

    # Converts the bool grid to a raw string (for display purposes)
    def __get_string_grid(self) -> str:
        ch = np.chararray(self.grid.shape)
        ch[:] = '.'
        ch[self.grid] = 'X'

        s = ""
        for i in range(self.n_rows):
            this_str = ch[i, :].tostring().decode("utf-8")
            s += this_str + "\n"

        return s

    # Main simulation method that does the simulation
    # This method parses the lines in the g-code (one at a time)
    # and handles either the go or laser command appropriate
    # This method returns a string representation of the laser cutting
    def simulate(self) -> str:

        for i in range(self.number_of_commands):
            this_line = self.parser.parse(i)
            self.command = this_line[0]
            self.__process(this_line[1], this_line[2])

        return self.__get_string_grid()
