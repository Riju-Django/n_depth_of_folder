import numpy as np
import cv2


def match(image_filename, template_filename):
    img = cv2.imread(image_filename,1)
    template = cv2.imread(template_filename,1)
    h , w, _ = template.shape

    methods= [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    for method in methods:
        
        img2 = img.copy()
        result = cv2.matchTemplate(img2, template , method )
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            
            location = min_loc
            
        else:
            location = max_loc
 
        bottom_right = (location[0] + w, location[1] +h)
        cv2.rectangle(img2, location , bottom_right, (0,255,0), 5)
        title = 'Match' + str(method);
        cv2.imshow(title,img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


match('1363I.JPG','1363I-M.JPG')
match('big-2.jpg','dhoni.jpg')
match('big-1.jpg','1374I-v2.jpg')



