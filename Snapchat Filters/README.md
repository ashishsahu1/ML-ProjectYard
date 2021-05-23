# Snapchat Filters using OpenCV

## Description

This repository contains python implmentation of various snapchat like face filters and masks. 

## Getting Started

### Dependencies

* Python
* The program makes use of Dlib-facial feature points
* OpenCV
* Tkinter
* Shape predictor 68 face landmark points Model


### Installing
* Git clone repository: 
```
git clone **
```
* Make sure to install the dependencies:
```
pip install dlib
```
* Any modifications needed to be made to files/folders
```
pip install opencv-python
```

### Executing program
* Before running the program, please navigate to the resources folder and merge/extract the following files:
   * shape_predictor_68_face_landmarks.7z.001
   * shape_predictor_68_face_landmarks.7z.002
   * shape_predictor_68_face_landmarks.7z.003

* To run different filters and masks, run using: 
   * For surgical mask filter
   ![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/35187768/97100752-0ca2ec80-1654-11eb-8f27-e49c541dfd72.gif)
```
python mask_dlib.py
```
   * For annabelle face mask
   ![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/35187768/97100658-f0528000-1652-11eb-9c32-bd20fbf03424.gif)
```
python annabelle.py
```
   * For Cat mask filter
   ![cat](https://user-images.githubusercontent.com/35187768/97100607-660a1c00-1652-11eb-82b2-990849a32098.gif)
```
python cat.py
```
   * For Clown Nose filter
   ![clown](https://user-images.githubusercontent.com/35187768/97100605-5be81d80-1652-11eb-84dc-4e3638cf39fa.gif)
```
python clown.py
```
   * For Moustache face filter
   ![moos](https://user-images.githubusercontent.com/35187768/97100608-6bfffd00-1652-11eb-9a65-5c46c9e58511.gif)
```
python moustache.py

```
## Acknowledgments

Inspiration, code snippets, etc.
* [Sergio's Youtube tutorial on simple dlib](https://www.youtube.com/watch?v=IJpTe-1cimE&t=1425s)
