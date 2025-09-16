import os
import shutil


files = os.listdir()

def moving_txt():
  if 'txt' not in files:
    os.mkdir('txt')
  
  for file in files:
    if file.endswith('txt'):
      shutil.move(file, 'txt')


def moving_rar():
  if 'rar' not in files:
    os.mkdir('rar')
  
  for file in files:
    if file.endswith('rar'):
      shutil.move(file, 'rar')


def moving_bmp():
  if 'bmp' not in files:
    os.mkdir('bmp')
  
  for file in files:
    if file.endswith('bmp'):
      shutil.move(file, 'bmp')


moving_txt()
moving_rar()
moving_bmp()


