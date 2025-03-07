#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py

# PROGRAMMER: Tasneem Mosameh
# DATE CREATED: 3/6/2025
# REVISED DATE: 3/7/2025
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels.

# Imports classifier function for using CNN to classify images
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.
    Parameters: 
     images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
     results_dic - Results Dictionary with 'key' as image filename and 'value'
                   as a List. Where the list contains the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int) where 1 = match between pet image
                           and classifier labels, 0 = no match
     model - CNN model architecture ('resnet', 'alexnet', 'vgg')
    Returns: None
    """
    for key in results_dic:
        # Classify the image using the classifier function (inputs: path + filename and model)
        model_label = classifier(images_dir + key, model)

        # Process the classifier label to match the required format
        model_label = model_label.lower().strip()

        # Define truth as pet image label
        truth = results_dic[key][0]

        # Compare pet image label to classifier label
        if truth in model_label:
            # If labels match, add classifier label and 1 (match) to the results dictionary
            results_dic[key].extend([model_label, 1])
        else:
            # If labels do not match, add classifier label and 0 (no match) to the results dictionary
            results_dic[key].extend([model_label, 0])#DONE :)
