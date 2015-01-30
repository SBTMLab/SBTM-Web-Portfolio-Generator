 # -*- coding: utf-8 -*-
import os
from PIL import Image



def resize (img, origin, result ,width, height):
	size = (width, height)
	imgpath = origin + img 
	im = Image.open(imgpath)
	im.save(result+img)
	outfile = result + img[:img.rfind(".")] + "_"+ unicode(width)+"x"+unicode(height)+".png"
	im = im.resize(size)
	im.save(outfile, "PNG")
	return  img[:img.rfind(".")] + "_"+ unicode(width)+"x"+unicode(height)+".png"


