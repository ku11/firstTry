from PIL import Image
from save_instrument import save_edited_image
from save_instrument import add_to_edited_table

def emptyfunc():
def watermark_photo(input_image_path, watermark_image_path, output_name, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    widthWM, heightWM = watermark.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    width_new, height_new = find_size(width, height, widthWM, heightWM)
    transparent.paste(watermark.resize((width_new, height_new), Image.ANTIALIAS), position,
                      mask=watermark.resize((width_new, height_new), Image.ANTIALIAS))
    save_edited_image(transparent.convert('RGB'), output_name)
    add_to_edited_table(output_name)