function changeImage(newSrc, highResSrc = null) {
    const mainImage = document.querySelector('#mainImageContainer img.zoom');
    const zoomLink = document.querySelector('#mainImageContainer a');

    if (mainImage && zoomLink) {
        mainImage.src = newSrc;
        zoomLink.href = highResSrc || newSrc;
    }
}


document.addEventListener('DOMContentLoaded', () => {
    const thumbnails = document.querySelectorAll('.Headband-Products a');
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', (event) => {
            event.preventDefault();
            const img = thumbnail.querySelector('img');
            if (img) {
                const highResSrc = img.getAttribute('data-highres');
                changeImage(img.src, highResSrc);
            }
        });
    });
});
