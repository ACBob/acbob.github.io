window.onload = function () {
	var divs = document.getElementsByTagName("div");
	for(var i = 0; i < divs.length; i++){
		if(divs[i].innerHTML != document.getElementById("container").innerHTML && 
		divs[i].innerHTML != document.getElementById("buttons").innerHTML && divs[i].innerHTML != document.getElementById("header").innerHTML) {
			
		divs[i].innerHTML = "";
		}
}