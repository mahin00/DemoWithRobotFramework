from robot.libraries.BuiltIn import BuiltIn

class Helper(object):

    def convert_to_title_case(self, stringToConvert):
        return stringToConvert.title()

    def integer_is_within_range_of_buffer(self, integerInput, integerToCheckWith, buffer):
        return abs(int(integerInput) - int(integerToCheckWith)) <= int(buffer)
