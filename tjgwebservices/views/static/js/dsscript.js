(function() {


var Anchors1 = document.getElementsByTagName("nav")[0].getElementsByClassName("menu");

//var Anchors2 = document.getElementsByTagName("aside")[0].getElementsByTagName("a");

var arr1 = Array.prototype.slice.call( Anchors1, 0 );

//var arr2 = Array.prototype.slice.call( Anchors2, 0 );

//var arr = arr1.concat(arr2);

for (var i = 0; i < arr1.length ; i++) {
    arr1[i].addEventListener("click",
        function (event) {
            event.preventDefault();
            var split_url = this.href.split("#");
            var after_hash = split_url[1];
            //if (confirm(after_hash)) {
                addText(after_hash);
            //}
        },
        false);
}

startSlideshow();
registerValidation();
addText("home");


	

})();


function addText(text){
        var xhr= new XMLHttpRequest();
        xhr.open('GET', '/static/pages/datascience/'+text, true);
        xhr.onreadystatechange= function() {
                if (this.readyState!==4) return;
                if (this.status!==200) return;
                document.getElementById('pageElement').innerHTML= this.responseText;

        };
        xhr.send();
		
}
