from PIL import Image

def get_center_pixel_color(image_path):

    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    block_size = 10
    block_positions = []

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):

            center_x = x + block_size // 2
            center_y = y + block_size // 2

            if center_x < width and center_y < height:
                color = pixels[center_x, center_y]
                r, g = color[:2]
                block_positions.append((g*10,r*10))

    return block_positions

def reposition_blocks(image_path, new_image_path):

    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()
    block_size = 10

    new_img = Image.new('RGB', (width, height))
    new_pixels = new_img.load()

    counter = 0
    position = get_center_pixel_color(image_path)

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):

            print((position[counter]))

            area_de_recorte = (x, y,x+block_size,y+block_size)
            imagem_recortada = img.crop(area_de_recorte)
            new_img.paste(imagem_recortada, position[counter])

            counter+=1

    new_img.save(new_image_path)

if __name__ == '__main__':

    image_path = "shredded.png"
    new_image_path = "shreddednew.png"

    reposition_blocks(image_path,new_image_path)
