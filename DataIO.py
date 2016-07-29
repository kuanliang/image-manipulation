import cv2
import numpy as np
import os

    
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

    