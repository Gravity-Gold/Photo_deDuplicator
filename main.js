document.addEventListener('DOMContentLoaded', function () {
    fetch('report.json')
        .then(response => response.json())
        .then(data => {
            const images = data.images;
            const dupImages = data.dupImages;

            // Display all images in the photo grid
            const photoGrid = document.getElementById('photo-grid');
            for (const key in images) {
                const imgDiv = document.createElement('div');
                imgDiv.classList.add('w3-quarter');
                const img = document.createElement('img');
                img.src = key;  // Assuming keys are paths to images
                img.alt = images[key];
                img.style.width = '100%';
                imgDiv.appendChild(img);
                photoGrid.appendChild(imgDiv);
            }

            // Display folder location
            const locationContainer = document.getElementById('image-container');
            const locationText = document.createElement('p');
            locationText.textContent = `Selected Folder: ${data.path}`; //  'path' holding folder location
            locationContainer.appendChild(locationText);

            // Display list of duplicates
            const duplicateSection = document.getElementById('duplicates-section');
            for (const key in dupImages) {
                const div = document.createElement('div');
                const duplicateText = document.createElement('p');
                duplicateText.textContent = `${key}: ${dupImages[key]}`;
                div.appendChild(duplicateText);
                duplicateSection.appendChild(div);
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});