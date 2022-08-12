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
get_target_loc():