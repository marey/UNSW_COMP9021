# COMP9021 Term 3 2021


from argparse import ArgumentParser
from re import sub
from statistics import mean
from math import ceil
import os

from PIL import Image


parser = ArgumentParser()
parser.add_argument('--image_file', dest='image_filename', required=True)
parser.add_argument('--block_size', dest='block_size', required=False)
parser.add_argument('--character_ramp', dest='character_ramp', required=False)
args = parser.parse_args()
image_filename = args.image_filename
try:
    # Record the luminance of each pixel.
    image = Image.open(image_filename).convert('L')
except FileNotFoundError:
    print(f'File {image_filename} could not be found.')
except OSError:
    print(f'File {image_file} could not be processed as an image file.')
# Each ASCII character will be put at the centre of a box of size
# 2.5mm x 2.5mm. We want the ASCII picture to be of maximum size
# 80 * 2.5mm x 100 * 2.5mm = 200mm x 250mm.
min_block_size = max(ceil(image.width / 80), ceil(image.height / 100))
try:
    block_size = max(int(args.block_size), min_block_size)
except TypeError:
    block_size = min_block_size
width = image.width // block_size
height = image.height // block_size
# We will crop the image symetrically if needed.
x_offset = image.width % block_size // 2
y_offset = image.height % block_size // 2
# A string of ASCII characters to replace pixels,
# from darkest to brightest.
character_ramp = args.character_ramp or '@%#*+=-:. '
image_name = sub('\..*', '', image_filename)
ascii_image_name = sub('\..*', '', image_filename) + '_'\
                   + str(block_size) + '_as_block_size_'\
                   + '_'.join(str(ord(e)) for e in character_ramp)\
                   + '_as_character_ramp'
print(ascii_image_name)
tex_filename = ascii_image_name + '.tex'
pixels = tuple(image.getdata())
max_luminance = max(pixels)
min_luminance = min(pixels)
luminance_range = max_luminance - min_luminance
with open(ascii_image_name + '.tex', 'w') as tex_file:
    print('\\documentclass[10pt]{article}\n'
          '\\usepackage{fancyvrb}'
          # As we want to be able to output any ASCII character, we do
          # not choose an ASCII character for that surrounding
          # character; we (arbitrarily) choose the character obtained
          # on a Mac by pressing Option 0.
          '\\DefineShortVerb{\\º}\n'
          '\\usepackage{tikz}\n'
          '\\usepackage[margin=0cm]{geometry}\n'
          '\n'
          '\\begin{document}\n'
          '\n'
          '\\vspace*{\\fill}\n'
          '\\begin{center}\n'
          '\\begin{tikzpicture}[x=2.5mm, y=-2.5mm]', file=tex_file
         )
    for j in range(height):
        y = y_offset + j * block_size
        for i in range(width):
            x = x_offset + i * block_size
            c = character_ramp[min(len(character_ramp) - 1,
                                   int((mean(image.crop((x, y, x + block_size,
                                                         y + block_size
                                                        )
                                                       ).getdata()
                                            ) - min_luminance
                                       ) / luminance_range
                                         * len(character_ramp)
                                      )
                                  )
                              ]
            # Using {{ and }} to output { and }, respectively.
            print(f'\\node at ({i}, {j}) {{º{c}º}};', file=tex_file)
    print('\\end{tikzpicture}\n'
          '\\end{center}\n'
          '\\vspace*{\\fill}\n\n'
          '\\end{document}', file=tex_file
         )
os.system('lualatex ' + tex_filename)
for file in (ascii_image_name + ext for ext in ('.aux', '.log')):
    os.remove(file)
print(f'\nProduced {ascii_image_name + ".pdf"}, replacing blocks of '
      f'{block_size}x{block_size} pixels by one character.'
     )
