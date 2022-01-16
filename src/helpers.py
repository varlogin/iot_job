import os

import settings as s


def exist_data_files():
    """Возвращает список доступных data файлов"""
    files = os.listdir(s.DATA_PATH)
    return [f for f in files if f.endswith('.csv')]
