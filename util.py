import albumentations as A
import cv2
import os.path
import random
from matplotlib import pyplot as plt



BOX_COLOR = (255, 0, 0) # Red
TEXT_COLOR = (255, 255, 255) # White


def visualize_bbox(img, bbox, class_name, color=BOX_COLOR, thickness=2):
    """Visualizes a single bounding box on the image"""
    x_min, y_min, w, h = bbox
    x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
   
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)
    
    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    cv2.putText(
        img,
        text=class_name,
        org=(x_min, y_min - int(0.3 * text_height)),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.35, 
        color=TEXT_COLOR, 
        lineType=cv2.LINE_AA,
    )
    return img


def visualize(image, bboxes, category_ids, category_id_to_name):
    img = image.copy()
    for bbox, category_id in zip(bboxes, category_ids):
        class_name = category_id_to_name[category_id]
        img = visualize_bbox(img, bbox, class_name)
    plt.figure(figsize=(12, 12))
    plt.axis('off')
    plt.imshow(img)


image = cv2.imread('test/A(0007)')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#bboxes = [[5.66, 138.95, 147.09, 164.88], [366.7, 80.84, 132.8, 181.84]]
bboxes = [
    [0.408203, 0.379167, 0.147656, 0.019444], 
    [0.643359, 0.372917, 0.042969, 0.018056],
    [0.693750, 0.379861, 0.050000, 0.018056],
    [0.351562, 0.268056, 0.037500, 0.030556],
    [0.386328, 0.282639, 0.047656, 0.023611],
    [0.429688, 0.282639, 0.042188, 0.023611],
    [0.619531, 0.269444, 0.040625, 0.025000],
    [0.647656, 0.247917, 0.028125, 0.037500],
    [0.681250, 0.254861, 0.029687, 0.026389],
    [0.704297, 0.272917, 0.030469, 0.031944],
    [0.848828, 0.239583, 0.028906, 0.040278],
    [0.027344, 0.372917, 0.054688, 0.015278],
    [0.313672, 0.373611, 0.036719, 0.013889],
    [0.187891, 0.365972, 0.038281, 0.015278],
    [0.529688, 0.361806, 0.059375, 0.015278],
    [0.863281, 0.376389, 0.059375, 0.011111],
    [0.933594, 0.368056, 0.056250, 0.013889]
    ]
category_ids = [0, 0, 0, 14, 14, 14, 14, 14, 14, 14, 14, 0, 0, 0, 0, 0, 0]
category_id_to_name = {0: '0', 14: '14'}

visualize(image, bboxes, category_ids, category_id_to_name)