
# Steps to Create Your Own Automatic Number Plate Detection Algorithm

## Data gathering and preparation

Firstly gather any publicly available dataset that is already annotated or download about a 100 images and self annotate using **LabelImg** or any other tools.
Make sure the annotations are in the YOLO model format accepted only.
Checkout -> [Click Here](https://miro.medium.com/max/2708/1*QfjU_RoyECAdSMV9FXicDg.png)
I used my own dataset uploaded at [Click Here](https://app.roboflow.com/dataset/license-plate-dataset-yn2je)

Then create a **classes.txt** file.
It should contain all the class name of training data.
For our case, the file contains only **license-plate** written in it.

Move all images, annotations text files and classes.txt into a single folder and zip it and upload to google drive.

## Some Custom File Configurations

Go to this link [Click Here](https://github.com/AlexeyAB/darknet)

### Configure Makefile

Go to darknet/Makefile. Download it. Update the followings :-
-   Line 1 — From  `GPU=0`  to  `GPU=1`
-   Line 2 — From  `CUDNN=0`  to  `CUDNN=1`
-   Line 4 — From  `OPENCV=0`  to  `OPENCV=1`

### Configure train.cfg and test.cfg

##### Go to darknet/cfg/yolov3.cfg. Download it.

-   Batches = number of classes * 2000
-   Filters = (number of classes + 5) * 3

For our case, number of classes = 1
So
Batches = 2000 (Number of training epochs)
Filters = 18

 Update the followings :-
 
 -  Comment Line 3
 -  Comment Line 4
 -  Un-Comment Out Line 6 — From  `batch=1`  to  `batch=4`
 -  Un-Comment Out Line 7 — From  `subdivisions=1`  to  `subdivisions=16`
 -  Line 20 — From  `max_batches=500200`  to  `max_batches=2000`
 -  Lines 603, 689, and 776 — From  `filters=255`  to  `filters=18`
 -  Lines 610, 696, and 783 — From  `classes=80`  to  `classes=1`

Save and rename as yolov3-train.cfg

##### Make a copy of train.cfg and rename as yolov3-testing.cfg

-   Batches = number of classes * 2000
-   Filters = (number of classes + 5) * 3

For our case, number of classes = 1
So
Batches = 2000 (Number of training epochs)
Filters = 18

 Update the followings :-
 
 -  Un-Comment Line 3
 -  Un-Comment Line 4
 -  Comment Out Line 6
 -  Comment Out Line 7
 -  Line 20 — From  `max_batches=500200`  to  `max_batches=2000`
 -  Lines 603, 689, and 776 — From  `filters=255`  to  `filters=18`
 -  Lines 610, 696, and 783 — From  `classes=80`  to  `classes=1`
 
 Save both and upload to drive.
 
## Training

Upload the ANPR.ipynb file in google colab.
Go to google drive and create a new folder named "yolo-license-plates".
This will be the folder where for every 1000 epochs, weights will be stored such that the weights do not get deleted.
Change runtime type to GPU (Mandatory).
Mount your drive to it.
Run all cells and enjoy.