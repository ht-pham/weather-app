/* Color Pallete: https://coolors.co/palette/8ecae6-219ebc-023047-ffb703-fb8500 */
function changeBackground(){

    if (new Date().getHours() < 18){
        document.body.style.backgroundColor = "#8ecae6";
        document.getElementsByTagName("h1").style.color = "#ffb703";
        document.getElementsByTagName("p").style.color = "black";
    }
}