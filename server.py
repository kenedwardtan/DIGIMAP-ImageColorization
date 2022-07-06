from io import BytesIO
from flask import Flask, request, render_template
from PIL import Image
import base64
import matplotlib.pyplot as plt
from colorizers import *

def colorize(path="", use_gpu=False):
    # load siggraph17 model
    colorizer_siggraph17 = siggraph17(pretrained=True).eval()
        
    # store and process input image
    img = load_img(path)
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

    # save image 
    img_L = Image.fromarray((out_img_siggraph17*255).astype(np.uint8))
    img_B = BytesIO()
    img_L.save(img_B, "png")
    img_B.seek(0)
    img_F = base64.b64encode(img_B.read()).decode()

    # return image
    return img_F