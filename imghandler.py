import PIL
from PIL import Image

#PIL is a necessary module for this function to work, PILLOW might work as well if PIL is unavailable
#PIL can be included in source (if downloaded externally) and be used that way with newer versions of python that dont support PIL


def resize_img():
    basewidth = 260   #adjust basewidth value to increase/decrease the new length/width of the image
    img = Image.open('/home/tol2/Downloads/media.gif')   #File to resize, use full path #Opens image in given path
    wpercent = (basewidth / float(img.size[0])) 
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('/home/tol2/Downloads/media.gif')   #Optionally, you can save the resized image under a new name to keep the original image
