import cv2
import numpy as np


def homography_align(sourceImg, destImg, pointDict, plot=False):
    '''homography align source img with destination img
    
    Args:
        sourceImg: source image being adjusted (image2)
        destImg: destination image as a reference
        pointDict: a dictionary with keys ('LU', 'LD', 'RU', 'RD', 'LEFT', 'RIGHT', 'UP', 'DOWN')
                                and values (image)
        plt: plot the result for verification
        
    Notes:
        step1. pattern match according to each template
        step2. get the center coordinate of each matched template on the source and destination image
        step3. homography align two images
        step4. return aligned source image
    
    Return:
        return modified sourceImg
    
    
    '''
    cornerList = ['LU', 'LD', 'RU', 'RD', 'LEFT', 'RIGHT', 'UP', 'DOWN']
    # Four corners of the source and destination image
    ptsSource = np.array([surimg.pattern_match_coordinate(sourceImg, pointDict[corner], method='cv2.TM_CCOEFF_NORMED')\
                 for corner in cornerList])
    ptsDest = np.array([surimg.pattern_match_coordinate(destImg, pointDict[corner], method='cv2.TM_CCOEFF_NORMED')\
               for corner in cornerList])
    
    # Calculate Homography
    h, status = cv2.findHomography(ptsSource, ptsDest)
    
    # Warp source image to destination based on homography
    adjImg = cv2.warpPerspective(sourceImg, h, (destImg.shape[1], destImg.shape[0]))
    
    if plot == True:
        plt.subplot(131), plt.imshow(sourceImg)
        plt.subplot(132), plt.imshow(destImg)
        plt.subplot(133), plt.imshow(adjImg)
        plt.show()
    
    return adjImg