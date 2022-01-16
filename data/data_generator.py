import sys
import random
from datetime import datetime


def create_title_row(cols):
    row = ','
    col = 0
    names = []
    while col < cols:
        names.append(f'col{col}')
        col += 1
    row += ','.join(names) + '\n'
    return row


def create_data_row(cols):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S+00:00')
    row = f'{date},'
    col = 0
    nums = []
    while col < cols:
        nums.append(str(random.uniform(0.1, 1)))
        col += 1
    row += ','.join(nums) + '\n'
    return row


def run(file_name, cols, rows):
    with open(file_name, 'w') as f:
        f.write(create_title_row(cols))
        row = 0
        while row < rows:
            f.write(create_data_row(cols))
            row += 1


if __name__ == "__main__":
    _, name, cols_count, rows_count = sys.argv
    run(name, int(cols_count), int(rows_count))
