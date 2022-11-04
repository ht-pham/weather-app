/* Color Pallete: https://coolors.co/palette/8ecae6-219ebc-023047-ffb703-fb8500 */
function changeBackground(){
    if (new Date().getHours() < 18){
        document.body.style.backgroundColor = "#8ecae6";
        document.getElementsByTagName("h1").style.color = "#ffb703";
        document.getElementsByTagName("p").style.color = "black";
    }
}
/* 
const form = document.querySelector("#search");
const CITY_REQUIRED = "Please enter a city";

function hasValue(input, message) {
	if (input.value.trim() === "") {
        const msg = input.parentNode.querySelector("small");
	    msg.innerText = message;
		return false;
	}
	return true;
}
form.addEventListener("submit", function (event) {
	// stop form submission
	event.preventDefault();

	// validate the form
	let nameValid = hasValue(form.elements["city"], CITY_REQUIRED);
	
	/* // if valid, submit the form.
	if (nameValid) {
		alert(CITY_REQUIRED);
	} 
});
*/