# Maths PDF's

With the University of Melbourne still being mostly in online mode, maths assignments have to be written by hand, scanned, and sent in as PDF's. I however, do not own a scanner and am usually doing the assignments where there isn't instant access to one. I therefore have to take photos of each page, then convert each image from .HEIC to .JPEG, and then to .PDF. I don't have 15mins to spend every week converting files back and forth for a single assignment.

### Setup
Create a virtual environment:
`virtualenv venv`

Install Requirements:
`pip3 install -r requirements.txt`

Install imagemagick:
`brew install imagemagick`


#### Convert Images
If you have to convert .HEIC like I do:

Ensure you have imagemagick installed

Then run `./src/convert.sh` from the terminal

#### Compile
If you just need to compile images into a pdf:

Drop your .JPEG's in the imgs folder.

Then run `python3 src/main.py <assignment name>` from the terminal


