import os
from wand.image import Image #pip install Wand
from wand.color import Color
import re
import cv2  #pip install "opencv-python-headless<4.3"

print("----Function file library importing complete -----")

def convert_pdf(filename, resolution=150):
    name=re.sub('.pdf','',filename)
    parent_dir= os.getcwd()
    path = os.path.join(parent_dir, name)
    print('Path',path)
    os.mkdir(path)
    output_path=path
    all_pages = Image(filename=filename, resolution=resolution)
    for i, page in enumerate(all_pages.sequence):
        with Image(page) as img:
            img.format = 'jpg'
            img.background_color = Color('white')
            img.alpha_channel = 'remove'
            image_filename = os.path.splitext(os.path.basename(filename))[0]
            print('1. file name',image_filename)
            image_filename = '{}-{}.jpg'.format(image_filename, i+1)
            print('2. file name',image_filename)
            image_filename = os.path.join(output_path, image_filename)
            print('3. file name',image_filename)
            img.save(filename=image_filename)
            print('file name',image_filename)
            print('end')
            
        print('end2')
    
    print('start')        
    for filename in os.listdir(path):
        im = path +'/'+filename
        print(filename)
        print('path of file name:::',im)
        img2 = cv2.imread(im)
        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        ROI_number = 1
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cntss = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cntss:
            area = cv2.contourArea(c)
            if area > 2000:
                x,y,w,h = cv2.boundingRect(c)
                f = filename[:-4]
                cr_name = f + '-' + str(ROI_number)+'.jpg'
                save_path = '/Volumes/AIML/Projects/pdf_image_extraction/pdf_image_extration/cropped_images/' + cr_name
                #cv2.rectangle(img2, (x , y), (x + w, y + h), (36,225,12), 4)
                try:
                    roi_crop = img2[y-100:y+h+100,x-100:x+w+100]
                    print('saved_path',save_path)

                    cv2.imwrite(save_path,roi_crop)
                    
                except:
                    roi_crop = img2[y:y+h,x:x+w]
                    cv2.imwrite(save_path,roi_crop)
                    
                ROI_number +=1


