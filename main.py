#load libraries
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
plt.gray()
from ipywidgets import interact, fixed
external_viewer = sitk.ImageViewer()
slicer_app_location = "C:/Users/User/AppData/Local/NA-MIC/Slicer 5.0.3/Slicer.exe"
external_viewer.SetApplication(slicer_app_location)
%config Completer.use_jedi = False

#Part A

#read images
img_prostate = sitk.ReadImage("C:\\Users\\User\\Downloads\\case23_resampled.nii")
img_boundary = sitk.ReadImage("C:\\Users\\User\\Downloads\\case23_resampled_segmentation.nii")

#opening data in slicer
external_viewer.Execute(img_prostate)
external_viewer.Execute(img_boundary)