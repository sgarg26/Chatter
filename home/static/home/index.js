document.addEventListener("DOMContentLoaded", () => {
    const postsDiv = document.getElementById("postsDiv");
    
    // postCounter is defined globally in index.html
    // add infinite scrolling
    window.addEventListener("scroll", () => {
        if (window.scrollY + window.innerHeight >= document.body.offsetHeight - 2) {
            // Get the basic post layout (from index.html)
            var post = document.querySelector('article.post');
            if (post) {
                // Create a deep clone of the existing article element
                var clonedArticle = post.cloneNode(true);
                
                // update postIDs
                let postID = (postCounter - 1) + 2;
                clonedArticle.dataset.postId = postID;
                let comments = (clonedArticle.querySelector(`.comment`)) // remember we can't use IDs because they have to be unique
                let likeIcon = (clonedArticle.querySelector(`.likeIcon`)) // remember we can't use IDs because they have to be unique
                comments.dataset.postId = postID;
                likeIcon.dataset.postId = postID;

                // Append a unique timestamp to the image URL
                var postImage = clonedArticle.querySelector('.post__media');
                if (postImage) {
                    postImage.src = postImage.src + '?t=' + Date.now();
                }

                // since querySelector copies the first post, we need to ensure we don't copy the like color
                var likeButton = clonedArticle.querySelector('.likeButton')
                var commentSection = clonedArticle.querySelector('.post__comments')
                var commentForm = commentSection.querySelector('.commentForm')

                if (likeButton.querySelector('path').classList.contains("s2")) {
                    likeButton.querySelector('path').classList.remove("s2")
                    likeButton.querySelector('path').classList.add("s1")
                }
 
                // add event listeners for commenting and liking
                likeButton.addEventListener("click", (event) => {
                    likeButton = event.target;
                    likePost(likeButton);
                })

                commentForm.addEventListener("submit", (event) => {
                    event.preventDefault();
                    postComment(event);
                    return false; // to prevent page from reloading
                })

                postsDiv.appendChild(clonedArticle);
                postCounter++;
                // Update alt attribute with a unique identifier
                postImage.alt = 'This is post #' + postCounter;
            } else {
                console.log("[Error] No posts found");
            }
        }
    });

    // initialize like buttons
    const likeBtns = document.querySelectorAll('.post__button');
    const commentFrms = document.querySelectorAll('.commentForm')
    likeBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            likePost(e.target)
        });
    });
    commentFrms.forEach(form => {
        form.addEventListener("submit", (event) => {
            event.preventDefault();
            postComment(event);
            return false;
        })
    })

});

/**
 * Uses the custom dataset-id attribute I added to identify which post was clicked,
 * and then assigns it a CSS class to set the color and update number of likes
 * @param {*} likeButton 
 */
function likePost(likeButton) {
    postID = likeButton.dataset.postId;
    var commentElement = document.querySelector(`.comment[data-post-id="${postID}"]`);
    
    // parse num likes
    var currentLikes = commentElement.querySelector('a')
    currentLikes = currentLikes.textContent.replace(/\D/g, '');
    
    if (likeButton.classList.contains("s1")) {
        console.log("liked!");
        likeButton.classList.add("s2");
        likeButton.classList.remove("s1");
        currentLikes++;
        commentElement.querySelector('a').textContent = currentLikes + ' others';
        
    } else {
        console.log("unliked!");
        likeButton.classList.add("s1");
        likeButton.classList.remove("s2");
        currentLikes--;
        commentElement.querySelector('a').textContent = currentLikes + ' others';
    }
}

function postComment(event) {
    // get the user input
    var commentText = document.querySelector('.post__comment-textfield').value;
    var postId = document.querySelector('.post__comments').dataset.postId;

    // append the comment
    var newComment = document.createElement('li');
    newComment.classList.add('post__comment-item');

    // for demonstration, instead of cloneNode() I'm just cheaply pasting the HTML
    newComment.innerHTML = `
        <div class="post__comment-avatar">
            <img src="${DEFAULT_USER_IMG_LINK}" alt="User Picture" />
        </div>
        <div class="post__comment-content">
            <p class="post__comment-text">${commentText}</p>
            <span class="post__comment-user">
                <a href="#">cs395_fan</a>
            </span>
        </div>
    `;

    // Get the comments list and append the new comment
    var commentsList = document.querySelector('.post__comments-list');
    commentsList.appendChild(newComment);

    // Clear the input field after posting the comment
    document.querySelector('.post__comment-textfield').value = '';
}
