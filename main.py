#load libraries
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
plt.gray()
from ipywidgets import interact, fixed
import utils
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
"""
#calculate physical extent #size*spacing mask

x_boundary= int((-94.40499877929688)+(333*0.6000000238418579))
y_boundary= int((-104.20700073242188)+(333*0.6000000238418579))
z_boundary= int((-49.85200119018555)+ (72*1.0))
print(x_boundary,y_boundary,z_boundary)

#get seed points from the prostate image
i1= int(40.454/105)
j1= int(10.329/95)
k1= int(-13.852/22)

i2= int(-16.107/105)
j2= int(-34.479/95)
k2= int(-13.852/22)

i3= int(29.435/105) 
j3= int(-35.948/95)
k3= int(-13.852/22)

i4= int(-21.984/105)  
j4= int(18.409/95)
k4= int(-13.852/22)

seed1 = (i1, j1,k1)
seed2 = (i2, j2,k2)
seed3 = (i3, j3,k3)
seed4 = (i4, j4,k4)"""

#seed_pts were pulled up from hovering over the prostate in slicer
seed_pts = [(122,211,36),(195,97,36),(135,109,36),(129,117,36)]

#calling prostate_segmenter()
seg= utils.prostate_segmenter(img_prostate, seed_pts)
sitk.WriteImage(seg, 'C:\\Users\\User\\Documents\\masters-queens\\BMIF804\\Mini-project\\my_segmentation.nrrd')

# overlay the mask generated
img_overlay = sitk.LabelOverlay(img_prostate, seg)
plt.figure(figsize=(5,5))
plt.imshow(sitk.GetArrayFromImage(img_overlay[:,:,35]))
plt.axis('off')
plt.show()

#overlay the gold standard
img_segmentation = sitk.ReadImage("C:\\Users\\User\\Downloads\\case23_resampled_segmentation.nii")
img_overlay_gold = sitk.LabelOverlay(img_segmentation, seg)
plt.figure(figsize=(5,5))
plt.imshow(sitk.GetArrayFromImage(img_overlay_gold[:,:,35]))
plt.axis('off')
plt.show()