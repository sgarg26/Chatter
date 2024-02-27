document.addEventListener("DOMContentLoaded", () => {
    const postsDiv = document.getElementById("postsDiv");
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
                    postImage.src = postImage.src + '?t=' + Date.now();
                }

                // Append the cloned article to the postsDiv
                postsDiv.appendChild(clonedArticle);

                postCounter++;

                // Update alt attribute with a unique identifier
                postImage.alt = 'This is post #' + postCounter;
            } else {
                console.log("[Error] No posts found");
            }
        }
    });
});