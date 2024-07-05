# Annotation Verifier

This application allows users to upload a zip file containing images, labels, and a `classes.txt` file. It then visualizes the bounding box annotations on the images and displays them for verification.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Pros and Cons](#pros-and-cons)
- [Contributing](#contributing)

## Features

- Upload a zip file containing images, labels, and classes.
- Visualize bounding box annotations on images.
- Navigate through annotated images.
- Display annotations with corresponding class names.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/prdowluri/annotation-verifier.git
    cd annotation-verifier
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

Visit the project's website : [Annotation-Verifier]([https://huggingface.co/spaces/prudhvirajdowluri/annotation-verifier])

1. Upload a zip file containing:
    - An `images` folder with the images.
    - A `labels` folder with the corresponding label files.
    - A `classes.txt` file with the class names.

2. Click the "Submit" button to visualize the annotated images.

3. Use the navigation arrows or keyboard arrow keys to navigate through the images.

## Folder Structure

The expected structure of the zip file is as follows:

```
zip_file.zip
│
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
├── labels/
│   ├── image1.txt
│   ├── image2.txt
│   └── ...
│
└── classes.txt
```

## Pros and Cons

### Pros

- **Ease of Use**: Simple and intuitive interface for uploading and visualizing annotated images.
- **Visual Feedback**: Provides a visual representation of annotations for easy verification.
- **Keyboard Navigation**: Allows navigation through images using keyboard arrow keys for better user experience.

### Cons

- **Limited Annotation Types**: Currently supports only bounding box annotations.
- **No Annotation Editing**: Does not provide functionality to edit annotations directly in the interface.
- **File Structure Dependency**: Requires a specific folder structure in the zip file.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and includes relevant tests.
"# annotation-verifier" 
