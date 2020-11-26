#SPDX-FileCopyrightText: © 2011 nagadomi@nurs.or.jp
#SPDX-License-Identifier: The MIT License (MIT)

import cv2
import os

def detect(filename,itr,cascade_file="../lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(36, 36))
    for (x, y, w, h) in faces:
        cpy = image.copy()
        roi = cpy[y:y+h, x:x+w]
        cv2.waitKey(0)
        cv2.imwrite(f"output/{itr}.png", roi)
        itr += 1
    return itr


itr = 0
epi = 0
source_dir_path = os.path.join(os.getcwd(), "webtoon")
source_dir_list = os.listdir(source_dir_path)
output_path = os.path.join(os.getcwd(), "output")
if not os.path.exists(output_path):
    os.makedirs(output_path)
for i_source in source_dir_list:
    input_dir_path = os.path.join(os.getcwd(), "webtoon", f"{i_source}")
    input_dir_list = os.listdir(input_dir_path)
    for i_input in input_dir_list:
        filename = os.path.join(input_dir_path,i_input)
        itr = detect(filename, itr)
    epi += 1
    print(f"episode{epi} complete - iter={itr}")

print("==========detection complete==========")

