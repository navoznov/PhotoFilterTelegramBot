from PIL import Image, ImageEnhance

class BlackAndWhiteFilter:
    def __init__(self):
        pass

    def apply(self, original_file_path, converted_file_path):
        image = Image.open(original_file_path)
        converted_image = image.convert('L')
        converted_image.save(converted_file_path, format='PNG')