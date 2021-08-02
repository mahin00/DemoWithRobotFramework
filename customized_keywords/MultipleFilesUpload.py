from robot.libraries.BuiltIn import BuiltIn

class MultipleFilesUpload(object):
    _paths = None
    _locator = None

    def choose_files(self, locator, paths):
        self._locator = locator
        self._paths = paths
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        sl.find_element(locator).send_keys(paths)
