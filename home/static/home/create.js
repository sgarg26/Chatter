// When the page loads
document.addEventListener("DOMContentLoaded", () => {
    const createImageLink = document.getElementById("imageLink");
    const createImg = document.getElementById("createImg");

    // Whenever the user changes the input of the image link
    createImageLink.addEventListener("keyup", async (event) => {
        let imageUrl = event.target.value;
        // If the image doesn't exist, change it to a default "image doesn't exist" image
        // set image
        if (await checkImage(imageUrl)) {
            console.log("image")
            createImg.src = imageUrl;
        } else {
            console.log("no image")
            console.log(createImg.dataset.imgdne)
            createImg.src = createImg.dataset.imgdne;
        }
    })
})

// This is a function to check if an imageURL actually exists...
// You don't really need to add this except to be fancy
function checkImage(imageURL) {
    return fetch(imageURL)
        .then(response => {
            if (response.ok) {
                const contentType = response.headers.get('content-type');
                const isImage = contentType && contentType.startsWith('image/');

                return isImage;
            }

            return false;
        })
        .catch(error => {
            console.error('Error:', error);
            return false;
        });
}  