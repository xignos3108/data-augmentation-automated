"""
# This is utility for calculating bbox coordinate from YOLO label

# YOLO label format --> Normalized((x_center, y_center, width, height))
# x_center = ((bb_x2 + bb_x1) / 2) / width
# y_center = ((bb_y2 + bb_y2) / 2) / height
# width = (bb_x2 - bb_x1) / width
# height = (bb_y2 - bb_y1) / height

# All bbox coordinates should be over 0 and lower than 1


(0,0)                               (1280,0)
   ------------------------------------
   |                                  |
   |                                  |
   | (bb_x1,bb_y1)  (bb_x2,bb_y1)     |
   |        ----------                |
   |       |         |                |
   |       ----------                 |
   | (bb_x1,bb_y2)  (bb_x2,bb_y2)     |
   |                                  |
   ------------------------------------
(0,960)                             (1280,60)

"""

width = 1280
height = 960

bb_x_center = 0.024609 # (bb_x2 + bb_x1) / 2*1280
bb_y_center = 0.373611 # (bb_y2 + bb_y1) / 2*960
bb_width = 0.049219 # (bb_x2 - bb_x1) / 1280
bb_height = 0.019444 # (bb_y2 - bb_y1) / 960


bb_x1 = ((bb_x_center*2*width)-(bb_width*width))/2
print("bb_x1:", bb_x1)
bb_y1 = ((bb_y_center*2*height)-(bb_height*height))/2
print("bb_y1:", bb_y1)
bb_x2 = ((bb_x_center*2*width)+(bb_width*width))/2
print("bb_x2", bb_x2)
bb_y2 = ((bb_y_center*2*height)+(bb_height*height))/2
print("bb_y2", bb_y2)