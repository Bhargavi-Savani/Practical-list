from PIL import Image
image_1 = Image.open(
r'D:\Codes\Py creations\Bhargavi\result.png')
im_1 = image_1.convert('RGB')
im_1.save(r'D:\Codes\Py creations\Bhargavi\my_result.pdf', save_all=True)
print("PDF created", end=" ")
