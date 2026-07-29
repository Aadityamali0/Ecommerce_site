const mainImg = document.getElementById("MainImage");
const thumbnails = document.querySelectorAll(".small-img");

thumbnails.forEach(img => {
    img.addEventListener("click", function () {

        // Save the current main image
        const currentMain = mainImg.src;

        // Replace the main image with the clicked thumbnail
        mainImg.src = this.src;

        // Put the old main image into the clicked thumbnail
        this.src = currentMain;
    });
});