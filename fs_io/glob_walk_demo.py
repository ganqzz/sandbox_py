# glob.glob and os.walk demo

import glob
import os

DATA = "../data"

print('--- glob.glob ---')

files = glob.glob(DATA + "/**/*", recursive=True)
print(files)

print('\n--- os.walk ---')

for folder_name, sub_folders, file_names in os.walk(DATA):
    print(f'The current folder: "{folder_name}"')
    print('Sub folders:', sub_folders)
    print('Files inside:', file_names)
    print()
