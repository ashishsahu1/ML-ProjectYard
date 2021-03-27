## About

This is a computer vision model trained to **detect and predict** the **car plate number** of any image that is fed into this model.
The plates numbers must be only **English** alphabets and numbers only. It performs quite well in most of the cases.
First a object **localization regressor model** is trained.
Then using **google tesseract** we then predict the word written in those plates.

## Steps to RUN

 - Create a new environment and activate it.
 - Run the **requirements.txt** file to download all dependencies needed to run the program
 - Then run the 4 notebooks in this exact order only.
	 - Data_Augmentation_and_Pipelining.ipynb
	 - Number_Plate_Localization.ipynb
	 - Automatic_Number_Plate_Recognition.ipynb

## NOTE

Also for number plate recognition 3 pretrained model weights are also given.
You can use any of them according to your desire for number plate localization.
All of them are pretty good.