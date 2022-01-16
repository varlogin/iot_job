import os
import pandas as pd

import settings as s


def condition_columns(full_path: str) -> list:
    """Определение списка нужных столбцов (поиск каждого 10ого)"""
    data_title = pd.read_csv(full_path, nrows=0)
    return data_title.columns[::10]


def calculate_sums(file_name: str) -> dict:
    """Вычисление сумм"""
    full_path = os.path.join(s.DATA_PATH, file_name)
    data = pd.read_csv(full_path, usecols=condition_columns(full_path))
    return data.sum(numeric_only=True).to_dict()
