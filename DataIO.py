import cv2
import numpy as np


def import_template(path):
    '''
    '''
    
    
def import_corner(path):
    '''
    '''
    
    
    
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

    