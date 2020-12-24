import enum


# Enum class to represent different commands in the G-code
class CommandType(enum.Enum):
    Go = 0
    LaserToggle = 1
    Unknown = 2
