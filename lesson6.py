from PIL import Image, ImageFilter, ImageEnhance

orange_cat = Image.open(r"orange_cat.jpg")
flipped_orange_cat = orange_cat.transpose(Image.FLIP_TOP_BOTTOM)
#flipped_orange_cat.show()
rotated_cat = orange_cat.rotate(45)
#rotated_cat.show()
