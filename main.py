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

#Part B
#cast img_segmentation type to solve int being unsigned 
seg = sitk.Cast(img_segmentation,sitk.sitkInt8)

utils.seg_eval_dice(img_segmentation, seg)   


#Part C
#checking the slice with largest area visually 
    
interact(utils.slice_view, img_prostate = fixed(img_prostate), slice_ind=(0,71))  

#slice 40 is the largest

utils.get_target_loc(img_segmentation[:,:,40])

#Part D

utils.pixel_extract(img_prostate, (6.664,-12.810,-13.852), 6)

#visualize intensities

plt.boxplot()