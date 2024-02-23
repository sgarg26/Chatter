window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= (0.9 * document.body.offsetHeight)) {
        const post = document.querySelector('.post__content img')
        console.log(post.src)        
    }
}

function myFunction() {
    alert("Hello from a static file!");
  }
  

document.addEventListener("DOMContentLoaded", () => {
    console.log("page loaded")
})