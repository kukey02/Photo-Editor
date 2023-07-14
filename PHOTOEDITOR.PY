import numpy as np
import matplotlib.image as mi
import matplotlib.pyplot as plt
import cv2

# Read Images
img = mi.imread(r'C:\Users\MRUNALI\OneDrive\Pictures\testimg.jpg')
  
# Output Images
plt.imshow(img)
print(img.shape)


m = int(input("Enter: 1 for cropping the image ; 2 for rotating the image ; 3 for turning the image into a pencil skeetch; Press any other key for exiting! "))
while(m!=0):
  if m==1:
    print('\nYou selected 1\n')
    a,b=img.shape[:2]        #height and width
    d1=int(input("distance 1 "))  
    d2=int(input("distance 2 "))
    d3=int(input("distance 3 "))
    d4=int(input("distance 4 "))
    img=img[d4:a-d2, d1:b-d3]  #crop using pixels
    plt.imshow(img)

  elif m==2:
    a=int(input("90 Or 180: "))
    d=int(input("clockwise-1 and anticlockwise-2: "))
    if d==2:
      i=a/90
    else:
      i=-(a/90)
    plt.imshow(np.rot90(img,i))   #numpy rotation function

  elif m==3:
    grayscale=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(grayscale)
    blur=cv2.GaussianBlur(invert, (21,21), 0)
    invblur=cv2.bitwise_not(blur)
    sketch=cv2.divide(grayscale, invblur, scale=256.0)
    plt.imshow(sketch)

  else:
    m=0