// Back to Top

//Get the button
var mybutton = document.getElementById("topBtn");
// document.querySelector.footer
var footer = document.footer

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
  console.log(mybutton.getBoundingClientRect().bottom)
}
