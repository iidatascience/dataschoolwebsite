
isWeekend = function(date)
{
	var day = date.getDay();
	return day === 0 || day === 6;
};

isLeapYear = function(year)
{
	// solution lifted from date.js (MIT license): https://github.com/datejs/Datejs
	return ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0);
};

getDaysInMonth = function(year, month)
{
	return [31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month];
};

var d = new Date();
var currentDate = [d.getFullYear(),
					d.getMonth(),
					d.getDate(),
					d.getDay()];
					
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];



var today = months[d.getMonth()] + " " + currentDate[2] + "," + currentDate[0];
var firstDay = months[d.getMonth()] + " 1," + currentDate[0];
var daysMonth = getDaysInMonth(currentDate[0], currentDate[1]);
var dateobj = new Date(firstDay + ' 0:00:00');
document.getElementById("day").innerHTML = today;


var preva = document.createElement("a");
var preva_class = document.createAttribute("class");
preva_class.value = "prev";  
var preva_href = document.createAttribute("href");
preva_href.value = "index.html";  
preva.innerHTML = "prev";
preva.setAttributeNode(preva_class);
preva.setAttributeNode(preva_href);
var titlespan = document.createElement("span");
var titlespan_class = document.createAttribute("class");
titlespan.innerHTML = today;
titlespan_class.value = "title";  
titlespan.setAttributeNode(titlespan_class);
var nexta = document.createElement("a");
var nexta_class = document.createAttribute("class");
nexta_class.value = "next";  
var nexta_href = document.createAttribute("href");
nexta_href.value = "index.html";  
nexta.innerHTML = "next";
nexta.setAttributeNode(nexta_class);
nexta.setAttributeNode(nexta_href);
var caption = document.createElement("caption");
caption.innerHTML = today;

var newdivnode = document.createElement("div");
var newdivnode_class = document.createAttribute("class");
newdivnode_class.value = "calendarHeader";  
newdivnode.setAttributeNode(newdivnode_class);
newdivnode.appendChild(preva);
newdivnode.appendChild(titlespan);
newdivnode.appendChild(nexta);

var newdaysnode = document.createElement("div");
var newdaysnode_class = document.createAttribute("class");
newdaysnode_class.value = "calendarDays";  
newdaysnode.setAttributeNode(newdaysnode_class);

var daysul = document.createElement("ul");
var days_header = ["Mo","Tu","We","Th","Fr","Sa","Su"];
var days_li={}, daysli={};

var i, j;
for (i=0;i<7;i++) {
	days_li[i]=days_header[i];
	daysli[i]=document.createElement("li");
	daysli[i].innerHTML = days_header[i];
	daysul.appendChild(daysli[i]);
}
newdaysnode.appendChild(daysul);

var newcontentnode = document.createElement("div");
var newcontentnode_class = document.createAttribute("class");
newcontentnode_class.value = "calendarContent";  
newcontentnode.setAttributeNode(newcontentnode_class);

var currentday_class = document.createAttribute("class");
currentday_class.value = "today";  


var weeksul={}, dayli={};
for (i=0;i<6;i++) {
	weeksul[i]=document.createElement("ul");
}

var daytext, currentDay, offset, week;
var thisDay=1;

for (j=0;j<35;j++) {
	offset=dateobj.getDay() - 2;
	offsetday=j-offset;
	dayli[j]=document.createElement("li");
	if (offsetday<=daysMonth && offsetday>0){
		daytext=offsetday;
	} else {
		daytext="";
	}
	if (offsetday==currentDate[2]){
		dayli[j].setAttributeNode(currentday_class);
	}
	dayli[j].innerHTML = daytext;
	week=Math.floor(j/7);
	weeksul[week].appendChild(dayli[j]);
}
for (i=0;i<6;i++) {
	newcontentnode.appendChild(weeksul[i]);
}

var newtablenode = document.createElement("div");
var newtablenode_class = document.createAttribute("class");
newtablenode_class.value = "calendarTable";  
newtablenode.setAttributeNode(newtablenode_class);

newtablenode.appendChild(newdivnode);
newtablenode.appendChild(newdaysnode);
newtablenode.appendChild(newcontentnode);

var calendarElement = document.getElementById("calendarElement");
calendarElement.appendChild(newtablenode);

