document.addEventListener("DOMContentLoaded", () => {
    const contentDiv = document.getElementsByClassName("content")[0];
    let postCounter = 0;

    window.addEventListener("scroll", () => {
        if (window.scrollY + window.innerHeight >= document.body.offsetHeight - 2) {
            // Get the basic post layout (from index.html)
            var post = document.querySelector('article.post');
            if (post) {
                // Create a deep clone of the existing article element
                var clonedArticle = post.cloneNode(true);

                // Append a unique timestamp to the image URL
                var postImage = clonedArticle.querySelector('.post__media');
                if (postImage) {
                    // postImage.src = postImage.src + '?t=' + Date.now();
                    postImage.src = "https://source.unsplash.com/random/512x512/?t=" + Date.now()
                }
                var description = clonedArticle.querySelector('#desc-text')
                if (description) {
                    getQuote(description)
                }

                // Append the cloned article to the postsDiv
                contentDiv.appendChild(clonedArticle);

                postCounter++;

                // Update alt attribute with a unique identifier
                postImage.alt = 'This is post #' + postCounter;
            } else {
                console.log("[Error] No posts found");
            }
        }
    });
});

const heart = document.getElementsByClassName("s1")[0]

heart.addEventListener("mouseup", () => {
    if (heart.style.fill == "red")
        heart.style.fill = "white"
    else {
        heart.style.fill = "red"
    }
})

function getQuote(desc) {
    let quote = ""
    fetch("https://api.quotable.io/random")
        .then(response => response.json())
        .then(data => {
            desc.innerText = data.content
        })
    return 0
}