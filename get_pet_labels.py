#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
# PROGRAMMER:Tasneem Mosameh
# DATE CREATED: 3/6/2025
# REVISED DATE: 3/6/2025
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0: pet image label (string).

# Imports python modules
from os import listdir

# Define get_pet_labels function
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
    # Creates the list of files directory
    image_files = listdir(image_dir)

    # Creates empty dictionary
    results_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for i in range(0, len(image_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't a pet image file
       if image_files[i][0] != ".":
           
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = ""

           # Recall that each filename can be accessed by image_files[i]
           words = image_files[i].lower().split('_')  # Ensure correct indentation
           
           # Join only alphabetic words
           pet_label = " ".join(word for word in words if word.isalpha()) 
           
           # If filename doesn't already exist in dictionary, add it and its pet label 
           # Otherwise, print an error message because it indicates duplicate files
           if image_files[i] not in results_dic:
               results_dic[image_files[i]] = [pet_label]
           else:
               print("** Alert: Duplicate file found in directory:", image_files[i])

    return results_dic
