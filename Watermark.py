from PIL import Image
from save_instrument import save_edited_image
from save_instrument import add_to_edited_table

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

def find_size(w, h, wWM, hWM):
    if w > h:
        heightWM_new = int(h / 2)
        widthWM_new = int((heightWM_new * wWM) / hWM)
    else:
        widthWM_new = int(w / 2)
        heightWM_new = int((widthWM_new * hWM) / wWM)
    return widthWM_new, heightWM_new
