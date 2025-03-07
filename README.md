# Dog Breed Classifier

This project is part of **Udacity's AI Programming with Python and TensorFlow Nanodegree**. It utilizes a **pre-trained deep learning model** to classify images, identifying dog breeds and distinguishing between dogs and non-dogs.

## Features
- Uses **VGG, ResNet, or AlexNet** for classification.
- Processes images and extracts labels automatically.
- Supports **command-line arguments** for flexibility (`--dir`, `--arch`, `--dogfile`).
- Measures execution time for performance analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Acceptance
✅ This project has been approved by Udacity!


## Usage
Run the classifier with:
```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

## Project Structure
```
├── check_images.py   # Main script for classification
├── get_pet_labels.py # Extracts image labels
├── classifier.py     # Runs the deep learning model
├── adjust_results.py # Compares results
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
```

## License
This project is for educational purposes under Udacity's AI Nanodegree Program.


