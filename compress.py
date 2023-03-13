import cv2 as cv
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFilter
import ffmpy
import random

#СТАБЛ Версия 
#Правильная центровка



for file in os.scandir('out'):
    fileim=file.name
    # Загрузка изображения
    if file.is_file() and file.path.split('.')[-1].lower() == 'mp4':
        print ('n')
    else:
        magein = Image.open('C:/users/and/out/'+fileim)
        bg = Image.new("RGB", imagein.size, (255,255,255))
        bg.paste(imagein,imagein)
  
        bg.save("c:/users/and/compress/"+fileim+".jpg")


    
    os.scandir('out').close()


cv.waitKey(0)
cv.destroyAllWindows()