from pdf2image import convert_from_path
import easyocr
import numpy as np

# here we initialize reader object to use english laguage

reader = easyocr.Reader(['en'])


def easyocr(pdf):
    images = convert_from_path(pdf)
    for i in range(0, len(images)):
        bounds = reader.readtext(np.array(images[i]), min_size=0, slope_ths=0.2, ycenter_ths=0.7, height_ths=0.6,
                                 width_ths=0.8, decoder='beamsearch', beamWidth=10)
    bounds += bounds
    text = ''
    for i in range(len(bounds)):
        text = text + bounds[i][1] + '\n'
    print(text)
  
    return text

