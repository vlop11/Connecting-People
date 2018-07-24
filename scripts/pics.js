var images = [
  "../images/bank.jpg",
  "../images/tech.jpg",
]

var imageHead = document.getElementsByClassName("html_image")[0];
var i = 0;

setInterval(function() {
      // console.log(imageHead)
      imageHead.style.backgroundImage = "url(" + images[i] + ")";
      i = i + 1;
      if (i == images.length) {
      	i =  0;
      }
}, 5000);
