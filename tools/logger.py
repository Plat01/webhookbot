import logging
import os


class Logger(logging.Logger):

    def __init__(self, name: str = __name__, file: str = "alllogs.log"):
        super().__init__(name)

        self.setLevel(logging.DEBUG)

        # Get the value of PYTHONPATH environment variable
        __python_path = os.environ.get('PYTHONPATH')
        __python_path = __python_path.split(os.pathsep)

        # The first directory in PYTHONPATH is the project directory
        _project_dir = __python_path[0]

        _logs_dir = os.path.join(_project_dir, 'logs')

        # Create "logs" dir if it's not exists
        os.makedirs(_logs_dir, exist_ok=True)

        self.file_path = os.path.join(_logs_dir, file)

        # create a file handler
        _file_handler = logging.FileHandler(self.file_path)
        _file_handler.setLevel(logging.DEBUG)

        # create a formatter
        _formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        _file_handler.setFormatter(_formatter)

        # create a stream handler
        _stream_handler = logging.StreamHandler()
        _stream_handler.setLevel(logging.INFO)

        # add the handlers to the logger
        self.addHandler(_file_handler)
        self.addHandler(_stream_handler)


LOG = Logger(__name__)

if __name__ == '__main__':
    LOG.info("LOG is working")
  