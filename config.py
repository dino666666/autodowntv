import os

CURRENT_FILE_PATH = os.path.abspath(__file__)
PROJECT_DIR = os.path.split(CURRENT_FILE_PATH)[0]
LOG_PATH = os.path.join(PROJECT_DIR, "log")


if __name__ == '__main__':
    print(f"CURRENT_FILE_PATH: {CURRENT_FILE_PATH}")
    print(f"PROJECT_DIR: {PROJECT_DIR}")
    print(f"LOG_PATH: {LOG_PATH}")
