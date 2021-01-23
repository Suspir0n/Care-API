"""import base64
import os
from src.setting.config import folder_storage
from src.helpers.UtilHelper import UtilsHelper


class FileHelper:
    @staticmethod
    async def write_picture(photo=''):
        try:
            with open(photo, 'rb') as img_file:
                _base64_data = base64.b64encode(img_file.read())

            _directory = folder_storage
            dir_exitis = await os.path.isdir(_directory)

            if not dir_exitis:
                await os.mkdir(_directory)

            file_name = UtilsHelper.generate_unique_hash() + '.jpg'
            file_name_path =  _directory + '/' + file_name

            await os.write(file_name_path, _base64_data, 'base64')
            print('File saved in ', file_name_path)


"""