import shutil
import sys

with open('Новый документ.docx', encoding='UTF-8') as file:
    for byte in file.readlines():
        print(byte)

