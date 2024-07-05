from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import cv2
import numpy as np
from PIL import Image
from zipfile import ZipFile
import tempfile
import io
import base64

app = Flask(__name__)

def load_classes(classes_file):
    """Load class names from a text file."""
    with open(classes_file, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    return classes

def load_annotation(annotation_file):
    """Load annotations from a text file."""
    with open(annotation_file, 'r') as f:
        annotations = [line.strip().split() for line in f.readlines()]
    return annotations

def visualize_annotations(image_folder, label_folder, classes_file):
    """Visualize bounding box annotations on images."""
    classes = load_classes(classes_file)
    dark_green = (0, 255, 0)
    # class_colors = {cls: tuple(np.random.randint(100, 255, 3).tolist()) for cls in classes}
    class_colors = {cls: dark_green for cls in classes}

    annotated_images = []

    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        label_path = os.path.join(label_folder, os.path.splitext(image_name)[0] + '.txt')

        if not os.path.exists(label_path):
            continue

        image = cv2.imread(image_path)
        if image is None:
            continue

        annotations = load_annotation(label_path)
        for annotation in annotations:
            class_id = int(annotation[0])
            class_name = classes[class_id]
            x_center, y_center, width, height = map(float, annotation[1:])
            x_center, y_center, width, height = int(x_center * image.shape[1]), int(y_center * image.shape[0]), int(width * image.shape[1]), int(height * image.shape[0])
            x1, y1 = x_center - width // 2, y_center - height // 2
            x2, y2 = x_center + width // 2, y_center + height // 2

            cv2.rectangle(image, (x1, y1), (x2, y2), class_colors[class_name], 2)
            cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, class_colors[class_name], 2)

        annotated_image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        buffered = io.BytesIO()
        annotated_image_pil.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        annotated_images.append(img_str)

    return annotated_images

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('zip_file')
        if uploaded_file:
            with tempfile.TemporaryDirectory() as tmp_dir:
                zip_path = os.path.join(tmp_dir, "uploaded.zip")
                uploaded_file.save(zip_path)

                with ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(tmp_dir)

                folder_path = tmp_dir
                image_folder = os.path.join(folder_path, 'images')
                label_folder = os.path.join(folder_path, 'labels')
                classes_file = os.path.join(folder_path, 'classes.txt')

                if not os.path.exists(image_folder) or not os.path.exists(label_folder) or not os.path.exists(classes_file):
                    return render_template('index.html', error="The zip file must contain 'images', 'labels', and 'classes.txt'.")

                annotated_images = visualize_annotations(image_folder, label_folder, classes_file)
                return render_template('index.html', annotated_images=annotated_images)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
