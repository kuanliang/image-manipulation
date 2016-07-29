import cv2
import numpy as np
import os
import re
from os import listdir
from os.path import isfile, join


def import_images(path):
    '''import images 
    
    Args:
        path: path to the images
    
    Notes:
        the path contain many images
    
    Return:
        a numpy array
    '''
    onlyFiles = [f for f in listdir(path) if isfile(join(path,f)) ]
    images = np.empty(len(onlyFiles), dtype=object)
    for n in range(0, len(onlyFiles)):
        images[n] = cv2.imread(join(path, onlyFiles[n]))
    
    onlyFilesSN = [re.sub('_+.+', '', SN) for SN in onlyFiles]
    return images, onlyFilesSN
    
def import_corner(path):
    '''import corner images to a dictionary
    
    Args:
        path: path to the corner images
    
    Notes:
        4 corners:
            RU.img (Right Up)
            RD.img (Right Down)
            LU.img (Left Up)
            LD.img (Left Down)
    
    Return: return a dictionary with key (RU, RD, LU, LD) and values are repective images
    '''
    
    cornerDict = dict()
    for cornerFile in os.listdir(path):
        fileExt = os.path.splitext(cornerFile)
        pathToImage = path + cornerFile
        if fileExt[1] == '.png':
            cornerDict[fileExt[0]] = cv2.imread(pathToImage)
    return cornerDict
    
    
        
    
    
def import_template(templateNum):
    '''import template img to a dictionary 
    
    Args:
        templateNum: the image number within the directory
    
    Notes:
        f
    
    Return:
        
    '''
    templateDict = dict()
    for directory in dirList:
        if directory.startswith('N66'):
            fileToOldfile = './parameters/' + directory + '/templates/' + str(templateNum) + '.png'
            # print fileToOldfile
            temp = cv2.imread(fileToOldfile)
            directory = directory.replace('N66_', '')
            print directory
            # plt.imshow(cv2.imread(fileToOldfile))
            templateDict[directory] = temp
    
    return templateDict

    