#load libraries
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

def prostate_segmenter(img_prostate, seed_pts):

    seg = sitk.ConfidenceConnected(img_prostate, seedList=seed_pts,
                                   numberOfIterations=1,
                                   multiplier=2.5,
                                   initialNeighborhoodRadius=2,
                                   replaceValue=1)


    
    

