from PIL import Image
import pytesseract
import os
import shutil
import uuid


class VerifyCode:

    @classmethod
    def get_text_from_image_file(cls, image_path):
        img_abspath = os.path.abspath(image_path)
        if os.path.exists(img_abspath):
            backup_path = os.path.dirname(img_abspath)
            copyto_path = os.path.join(backup_path, '{}.gif'.format(str(uuid.uuid1())))
            print(copyto_path)
            shutil.copy(img_abspath, copyto_path)

        img = Image.open(img_abspath)
        img = img.convert('RGB')

        text = pytesseract.image_to_string(img, lang='eng')
        return ''.join(x for x in text if x.isalpha())

    @classmethod
    def denoise_iamge(cls, image_path):
        pass
