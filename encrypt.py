



from stegano import lsb

image = lsb.hide("original_image.png", "idinahui")
image.save("output_image.png")
