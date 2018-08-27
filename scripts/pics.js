// var images = [
//   "../images/bank.jpg",
//   "../images/georgiatech.jpg",
//   "../images/omni.jpg"
//
// ]
//
// var imageHead = document.getElementsByClassName("html_image")[0];
// var i = 0;
// // here, html_image is a list so grabbing the
//
// setInterval(function() {
//       // console.log(imageHead)
//       imageHead.style.backgroundImage = "url(" + images[i] + ")";
//       i = i + 1;
//       if (i == images.length) {
//       	i =  0;
//         // this restarts the loop
//       }
// }, 5000);

//new method for changing background pics
//it's a lot smoother
var bgImageArray = ["bank.jpg", "georgiatech.jpg", "omni.jpg"],
base = "../images/",
secs = 5;
bgImageArray.forEach(function(img){
    new Image().src = base + img;
    // caches images, avoiding white flash between background replacements
});

function backgroundSequence() {
	window.clearTimeout();
	var k = 0;
	for (i = 0; i < bgImageArray.length; i++) {
		setTimeout(function(){
			document.documentElement.style.background = "url(" + base + bgImageArray[k] + ") no-repeat center center fixed";
			document.documentElement.style.backgroundSize ="cover";
		if ((k + 1) === bgImageArray.length) { setTimeout(function() { backgroundSequence() }, (secs * 1000))} else { k++; }
		}, (secs * 1000) * i)
	}
}
backgroundSequence();
