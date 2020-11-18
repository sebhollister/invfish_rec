import cv2
import numpy as np
import tutorial_helpers as helpers
import model
import subprocess
from datetime import datetime
import sys
from pathlib import Path

def main():
    # Take in camera options
    args = sys.argv[1:]
    num_args = len(args)
    if num_args != 5:
        print("Did not input enough camera options")
        sys.exit()
    iso , cont, brt, sat, shutter = args

    #Set Raspistill image options
    dir = "/home/pi/"
    fileName= "img_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    cmd = "raspistill --ISO {} --contrast {} -- brightness {} --drc high -k --saturation {} --shutter {} -o ".format(
        iso, cont, brt, sat, shutter) + dir + fileName
    print(cmd)
    subprocess.call(cmd, shell=True) 

    #Print model data
    model_wrapper = model.ModelWrapper()
    input_shape = model_wrapper.GetInputShape()
    output_shape = model_wrapper.GetOutputShape()
    preprocessing_metadata = helpers.get_image_preprocessing_metadata(model_wrapper)


    #Open image and run recognition
    my_file = Path(fileName)
    if not my_file.is_file():
        print("File Not Found")
        sys.exit()

    sample_image = cv2.imread(fileName)

    input_data = helpers.prepare_image_for_model(sample_image, input_shape.columns,
                                                input_shape.rows, preprocessing_metadata=preprocessing_metadata)

    input_data = model.FloatVector(input_data)

    predictions = model_wrapper.Predict(input_data)

    prediction_index = int(np.argmax(predictions))

    c_file = open("categories.txt", "r")
    list_of_categories = [(line.strip()).split() for line in c_file]
    c_file.close()

    #Print Results
    print("Model input shape: [{0.rows}, {0.columns}, {0.channels}]".format(
        input_shape))
    print("Model output shape: [{0.rows}, {0.columns}, {0.channels}]".format(
        output_shape))

    print("Category index: {}".format(prediction_index))
    print("Confidence: {}".format(predictions[prediction_index]))
    print("This object ({}) is a {} with confidence of {}".format(
        fileName, 
        list_of_categories[prediction_index], 
        predictions[prediction_index]))

if __name__ == "__main__":
    main()