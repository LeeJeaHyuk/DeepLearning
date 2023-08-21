import os
from datetime import datetime

def file_make(filename):
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')

    file_path = os.path.join('.', filename, date)
    os.makedirs(file_path, exist_ok=True)

    return file_path






