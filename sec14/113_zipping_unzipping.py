
# zip in File

f = open('fileone.txt', 'w+')
f.write("one file")
f.close()

f = open('filetwo.txt', 'w+')
f.write("two file")
f.close()


import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')

comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.clase()



# unzip - extracting 
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')

zip_obj.extractall('extract_content')





# shutil
import shutil
# dir_to_zip = "whole dir PATH"
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')






