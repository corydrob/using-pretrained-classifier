#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Cory Robinson 
# DATE CREATED: April 30, 2019
# caught flu, fell behind on course.
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from os import path

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #get filenames from directory.
    filename_list = listdir(image_dir)
    #create the results dictionary that we'll be returning:
    results_dic = {}
    #go through our filename list:
    for pet_image in filename_list:
        if pet_image.startswith('.'):
            continue
        elif pet_image not in results_dic:
            #get rid of caps
            lowered_pet_image = pet_image.lower()
            #remove file extension
            lowered_pet_image=path.splitext(lowered_pet_image)[0]
            #turn snake-case string into a list of words
            pet_image_chopped = lowered_pet_image.split('_')
            #create a string to store the pet name that will go in the dict
            pet_name = ""
            #save the words in the word-list that describe the animal while throwing out the numbers+file extension
            for word in pet_image_chopped:
                if word.isalpha():
                    pet_name+=word+" "
                    #discard the extra white space at the end of the pet name
              

            results_dic[pet_image]=[pet_name.strip()]
            #print(results_dic[pet_image],'|')
            
        else:
            print("warning: {} appears to be a duplicate filename. not added to dict.")
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
