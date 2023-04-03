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
}

/**
Currently we have a problem with the ONS table macro where
we can't display two tables with the same headers on the same page.
This script is a temporary solution to the problem, where we update
the headers on the second table manually on page load.
*/
headers = ["Name", "Theme", "Expert group", "Languages", "Access", "Status"];


function updateTableHeaders() {
    const futureTable = document.querySelector("#future-table")
    const buttons = futureTable.querySelectorAll(".ons-table__sort-button");

    for (let i = 0; i < buttons.length; i++) {
        let sortIcon = `${headers[i]}<svg id="sort-sprite-name-${i}" class="ons-svg-icon" viewBox="0 0 12 19" xmlns="http://www.w3.org/2000/svg" focusable="false" fill="currentColor">
            <path class="ons-topTriangle" d="M6 0l6 7.2H0L6 0zm0 18.6l6-7.2H0l6 7.2zm0 3.6l6 7.2H0l6-7.2z"></path>
            <path class="ons-bottomTriangle" d="M6 18.6l6-7.2H0l6 7.2zm0 3.6l6 7.2H0l6-7.2z"></path>
        </svg>
        `;
        buttons[i].innerHTML = sortIcon;
    }
}

window.addEventListener("load", updateTableHeaders);
