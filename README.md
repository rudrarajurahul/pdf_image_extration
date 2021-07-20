# PDF Image Extration

This project has been developed for extracting images from a PDF file using Opencv and Wand. The script first first converts the  PDF into an image and then extracts the images and tabels from the PDF using opencv contours by calculating the lenght of the contours and finding the region of intrest of contours that are greater than 2000 in area. 

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

Git clone the repository and run python --pdf "path to the pdf"![Screenshot 2021-07-20 at 11 19 02 PM](https://user-images.githubusercontent.com/22589402/126371695-89626a82-1e71-4333-a777-f0684c344874.png)

![sample-6-1](https://user-images.githubusercontent.com/22589402/126371776-ac027b5c-63e6-40ba-b84d-da9aa54d227d.jpeg)

![sample-6-2](https://user-images.githubusercontent.com/22589402/126371854-3d59558d-647a-4d92-b8f1-8dfbdfcba28a.jpeg)

