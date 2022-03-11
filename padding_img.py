from PIL import Image

bg_img_path = "./10_2_35.539835078916035_139.48305196881293_35.54145833_139.4746875_35.534375_139.4834375.png"
bg_img = Image.open(bg_img_path)
bg_img = bg_img.convert('RGB')
print(bg_img.split())

mode = 'RGBA'
size = (640, 640)
color = (0, 0, 0)
blank_img = Image.new(mode, size, color)
blank_img.save("./padded_img.png")

front_img_path = "./888.jpeg"
front_img = Image.open(front_img_path)
resize_size = (175, 128)
position = (166, 35)
front_img = front_img.resize(resize_size)
print(front_img.split())

# position = (300, 200)
bg_img.paste(front_img, position)
# bg_img.show()
bg_img.save('./test_888.png')

