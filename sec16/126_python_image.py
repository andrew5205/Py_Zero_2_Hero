
# Pillow - python image library - PIL
# pip install pillow

# pillow.readthedocs.io

# from PIL import Image
# Image.open('file path', mode = "r")



from PIL import Image
golden = Image.open('gld_exp.jpg')
# print(type(mac))            # <class 'PIL.JpegImagePlugin.JpegImageFile'>

# IDE to show image - .show()
# golden.show()

print(golden.size)                      # (225, 225)
print(golden.filename)                  # gld_exp.jpg
print(golden.format_description)        # JPEG (ISO 10918)


# Crooping image - return a rectangular region from this image. 
# The box is a  4-tuple defining left, upper, right lower pixel cordinate

# .crop()

pencil = Image.open('color_pencil.jpg')
pencil.show()
print(pencil.size)                      # (1000, 667)

# starting point (x, y) with (w, h)
# (x, y) = (0, 0) from top left
x = 0
y = 0

w = 1000 / 5
h = 667 / 10

pencil.crop((x, y, w, h)).show()
# p = pencil.crop((x, y, w, h))


# starting point (x, y) with (w, h)
# (x, y) = (0, 0) from top left
x = 0
y = 500

w = 1000 / 5
h = 667

pencil.crop((x, y, w, h)).show()
p = pencil.crop((x, y, w, h))


# *************************************   paste    ********************************************
# .paste(im=, box=())
# base_pic.paste(im = pic_gonna_paste_on, box = (x, y))
# wont affect original pic
pencil.paste(im = p, box = (0, 0))
pencil.show()


# *************************************   resize    ********************************************
print(pencil.size)              # (1000, 667)
pencil.resize((2000, 1800)).show()



# *************************************   rotate    ********************************************
# .rotate(degree)
golden.rotate(90).show()




# *******************************   color transparency    ***************************************
# RGBA - Red, Green, Blue, Alpha
# 255

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.jpg')

# .putalpha(0~255)
red.putalpha(200)
red.show()


blue.paste(im = red, box = (0,0), mask = red)
blue.show()



# *******************************************   save     ***************************************

blue.save("modified_img.png")
mod = Image.open('modified_img.png')
mod.show()



