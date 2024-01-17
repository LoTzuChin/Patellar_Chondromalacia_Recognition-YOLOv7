from flask import Flask,render_template,request,url_for
import time
import cv2
import numpy as np
from PIL import Image
from yolo import YOLO, YOLO_ONNX



app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        yolo = YOLO()
        imagePath =request.form['imagePath']
    
        img = imagePath
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
        else:
            r_image = yolo.detect_image(image, crop = False, count= False)
            r_image.save("static/demo.jpg")
            r_image.show()

    return render_template('project.html')



if __name__ == '__main__':

    app.run()
