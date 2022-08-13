#load libraries
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

#Part A
def prostate_segmenter(img_prostate, seed_pts):

    seg = sitk.ConfidenceConnected(img_prostate, seedList=seed_pts,
                                   numberOfIterations=1,
                                   multiplier=2.5,
                                   initialNeighborhoodRadius=2,
                                   replaceValue=1)


#PartB
def seg_eval_dice(img_segmentation, seg):

    DSC = sitk.LabelOverlapMeasuresImageFilter()    

    # Overlap measures
    DSC.Execute(img_segmentation, seg)
    print(DSC.GetDiceCoefficient())
    print(DSC.GetVolumeSimilarity())
    print(DSC.GetFalseNegativeError())
    print(DSC.GetFalsePositiveError())

#Part C

from ipywidgets import interact, fixed
slice_ind = 35
def slice_view(img_prostate,slice_ind):
    plt.imshow(sitk.GetArrayFromImage(img_prostate[:,:,slice_ind]), 
               cmap='gray', vmin=0, vmax=400)
    plt.axis('off')
    plt.colorbar()
    plt.show()

def get_target_loc(mask):
    label_shape_statistics_image_filter = sitk.LabelShapeStatisticsImageFilter()
    label_shape_statistics_image_filter.Execute(mask)

    centroid = label_shape_statistics_image_filter.GetCentroid(1)
    print(centroid)

#Part D

def pixel_extract(img_prostate, point, width):
    seg = sitk.ConfidenceConnected(img_prostate, seedList=point,
                                   numberOfIterations=1,
                                   multiplier=2.5,
                                   initialNeighborhoodRadius=width,
                                   replaceValue=1)

    #returning intensities of seg
