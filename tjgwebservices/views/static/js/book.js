var flipspan = document.getElementsByClassName("click");
var articles = document.getElementsByClassName("articles");
var text1 = document.getElementById("text1");
var text2 = document.getElementById("text2");

var fs = flipspan.length;
var arts = articles.length;
var i,j=0;

for (i=0;i<fs;i++){
	flipspan[i].onclick = function(e){
	e = e || window.event;
	var targ = e.target || e.srcElement;
	if (targ.nodeType == 3) targ = targ.parentNode;
	  pn = targ.parentNode;
	  arr = pn.className.split(" ");
	  if (arr.indexOf("flip") == -1) {
		  var timer=setTimeout(function(){
		    pn.className += " " + "flip";

		  }, 10);

		  var timer2=setTimeout(function(){
					targ.style.display="none";

		  }, 350);

		setTimeout(() => {
		  pn.className = pn.className.replace(" flip","");
  		  targ.style.display="block";
		  j++;
		  if (j>=arts-1) j=0;
		  text1.innerHTML = articles[j].innerHTML;
		  text2.innerHTML = articles[j+1].innerHTML;
		  clearTimeout(timer);
		  clearTimeout(timer2);
		}, 400);
	   }
	};
}
