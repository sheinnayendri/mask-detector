# Artificial Intelligence Final Project: Mask Detector Application
Departemen Informatika, ITS 2020

## Ilustrasi Aplikasi yang dibuat:
![image](https://user-images.githubusercontent.com/48936125/85216077-ccccaf80-b3aa-11ea-874b-6a79e5ed4dd0.png)

## Implementation:
- File ```mask-detector.py``` merupakan implementasi penggunaan model untuk detect wajah dan recognize mask.
- File ```deploy.prototxt.txt``` dan ```res10_300x300_ssd_iter_140000.caffemodel``` merupakan model untuk detect wajah.
- File ```model_mask2.h5``` merupakan model untuk recognize mask (dapat diakses [di sini](https://drive.google.com/file/d/1IRurap0hGgbVWC-bt-G4ll0smpuCcaTJ/view?usp=sharing))
- Model recognize mask (```model_mask2.h5```) didapatkan dari training pada file ```train_mask_model.ipynb```, di mana menggunakan sample image sebanyak 828 (70% untuk training dan 30% untuk validation). Training images dapat diakses [di sini](https://drive.google.com/drive/folders/1qAy0VYYTMYKKV-_ty6A0kU3yi1K2CNHT?usp=sharing).

## Convert to application (.exe):
- Install auto-py-to-exe.
- Pada saat akan melakukan convert, sertakan juga ketiga model (```deploy.prototxt.txt```, ```res10_300x300_ssd_iter_140000.caffemodel```, dan ```model_mask2.h5```) sebagai file tambahan.
- Sertakan pula icon ```logo_mask.ico```.

## Aplikasi Mask Detector:
Aplikasi exe dapat didownload [di sini](https://drive.google.com/file/d/1QVqfY5-uJSdaAgioexwPnyv9dp30ipIS/view?usp=sharing).

## Link Youtube berisi demonstrasi dan penjelasan source code project:
https://youtu.be/gBpB-4EcNro
