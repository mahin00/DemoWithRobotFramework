import zipfile
from os import path

class UnzipFile(object):
    _file_path = None

    def unzip_file(self, _file_path):
        self._file_path = _file_path
        _zip_dest = path.splitext(_file_path)[0] # Assumes the filename ends with .zip
        with zipfile.ZipFile(_file_path, 'r') as archive:
            archive.extractall(_zip_dest)
        return _zip_dest