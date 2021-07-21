# PDF Image Extration

This project has been developed for extracting images from a PDF file using Opencv and Wand. The script first first converts the  PDF into an image and then extracts the images and tabels from the PDF using opencv contours by calculating the lenght of the contours and finding the region of intrest of contours that are greater than 2000 in area. 

Since this method depends on opencv. It does not need any prior training. But needs to be tuned as per the PDF format that you will be working on. 

## Prerequistes
* numpy==1.21.0 
* opencv-python-headless==4.2.0.34. 
* Wand==0.6.6.  


## Project tree


 * [cropped_images](./tree-md)
   * [sample-1-1.jpg](./dir1/file1.ext) 
   * [sample-2-1.jpg](./dir1/file2.ext)
   * [sample-3-1.jpg](./dir1/file3.ext)
   * [sample-4-1.jpg](./dir1/file4.ext)
   * [sample-5-1.jpg](./dir1/file5.ext)
   * [sample-5-2.jpg](./dir1/file6.ext)
 * [sample](./dir2)
 * [README.md](./README.md)
 * [function.py](./file_in_root.py)
 * [main.py](./main.py)
 * [requirements.txt](./file_in_root)
 * [sample.pdf](./file_in_root)



## Output

To run the script clone he repository and run ( python main.py --pdf 'path to the pdf file' )

From the screen shot you can notice the input and the outputs on the right. The script identifies the images and you can see a green box with represents the region of interest. And after it identifies the region of interest and crops the image with an increase in 100 units in all directions of the the region of interest. 

The name of the cropped image (sample-1-1.jpg) sample representing the name of the PDF and the next digit represents the page number in that pdf and then the next digit represents the image number in that page. 

<img width="743" alt="Screenshot 2021-07-21 at 8 51 59 AM" src="https://user-images.githubusercontent.com/22589402/126425906-4182d485-ce61-4b9a-b745-1cd3a1d19338.png">

