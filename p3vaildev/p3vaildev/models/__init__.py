import os
from p3vaildev.p3vaildev.config.app_conf import settings


def load_data_files():
    data_files = os.listdir(settings.data_files_directory)
    for data_file_name in data_files:
        print(data_file_name)
