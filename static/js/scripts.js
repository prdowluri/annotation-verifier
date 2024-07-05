// JavaScript for image navigation
let currentImageIndex = 0;

function showImage(index) {
    const images = document.querySelectorAll('.img-fluid');
    images.forEach(img => img.classList.remove('active'));
    const currentImage = document.querySelectorAll('.img-fluid')[index - 1];
    if (currentImage) {
        currentImage.classList.add('active');
    }
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % totalImages;
    showImage(currentImageIndex + 1);
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + totalImages) % totalImages;
    showImage(currentImageIndex + 1);
}

// Show the first image initially
showImage(1);

// Add keyboard navigation
document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowRight') {
        nextImage();
    } else if (event.key === 'ArrowLeft') {
        prevImage();
    }
});

// Show arrows when images are displayed
document.addEventListener('DOMContentLoaded', function() {
    if (totalImages > 0) {
        document.querySelector('.nav-arrow.prev').style.display = 'block';
        document.querySelector('.nav-arrow.next').style.display = 'block';
    }
});
