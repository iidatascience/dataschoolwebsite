var token = (Math.floor(Math.random() * 9999)).toString();
var chatdiv = document.createElement("div");
chatdiv.setAttribute("class","chat");
var requestanchor = document.createElement("a");
requestanchor.setAttribute("href","#");
requestanchor.innerHTML = "Request Service";
var chatTitle = document.createElement("h1");
chatTitle.innerHTML = "II Data School - Currently Unavailable";
var button1 = document.createElement("button");
button1.innerHTML = "Close";
var spans = [];
spans[0] = document.createElement("span");
spans[0].innerHTML = "Online";
spans[1] = document.createElement("span");
spans[1].innerHTML = "Offline";
var form1 = document.createElement("form");
var textarea1 = document.createElement("textarea");
textarea1.setAttribute("name","messagetext");
textarea1.setAttribute("id","messagetext");
textarea1.setAttribute("disabled","disabled");
textarea1.setAttribute("placeholder","Currently Unavailable");
var button2 = document.createElement("button");
button2.innerHTML = "Send";
var div2 = document.createElement("div");
var textdiv = document.createElement("div");
textdiv.setAttribute("class","chattext");
var updatep = document.createElement("p");
updatep.setAttribute("id","updatemessage");
var textul = document.createElement("ul");
var textli1 = document.createElement("li");
textul.appendChild(textli1);
textdiv.appendChild(updatep);
textdiv.appendChild(textul);

chatdiv.appendChild(requestanchor);
chatdiv.appendChild(chatTitle);
chatdiv.appendChild(button1);
chatdiv.appendChild(spans[0]);
chatdiv.appendChild(spans[1]);
form1.appendChild(textarea1);
chatdiv.appendChild(form1);
chatdiv.appendChild(button2);
chatdiv.appendChild(div2);
asidebody=document.querySelector("main aside");
asidebody.appendChild(chatdiv);
asidebody.appendChild(textdiv);
		
var ring = document.querySelector("div.chat a");
var textarea = document.querySelector("div.chat textarea");
var send = document.querySelector("div.chat button:nth-of-type(2)");
var form = document.querySelector("div.chat form");
var textbox = document.querySelector("div.chattext > ul");

ring.addEventListener("click", 
	function(e){
		e.preventDefault(); 
		var formData = new FormData();
		formData.append("userchat","conversationstart");
		formData.append("conversationid",token);
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == XMLHttpRequest.DONE) {   
				if (xmlhttp.status == 200) {
					document.getElementById("updatemessage").innerHTML = xmlhttp.responseText;
					textarea.disabled = false;
					textarea.setAttribute("placeholder","Please enter your message here...");
				}
				else if (xmlhttp.status == 400) {
				}
				else {
				}
			}
		};
		xmlhttp.open("POST", "chat/newconversation");
		xmlhttp.send(formData);
		return false;
		}
,false);

send.addEventListener("click", 
	function(e){
		e.preventDefault(); 
		var formData = new FormData(form);
		formData.append("userchat","conversationcontinue");
		formData.append("conversationid",token);
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == XMLHttpRequest.DONE) {   
				if (xmlhttp.status == 200) {
					updateConversation(xmlhttp.responseText);
					textarea.value = "";
				}
				else if (xmlhttp.status == 400) {
				}
				else {
				}
			}
		};
		xmlhttp.open("POST", "chat/continueconversation");
		xmlhttp.send(formData);
		return false;
		}
,false);


function updateConversation(response) {
						var array1 = JSON.parse(response);
						if (array1.length> 0) {
							while( textbox.firstChild ){
							  textbox.removeChild( textbox.firstChild );
							}
							for (i = 0;i < array1.length; i++) {
								var tli = document.createElement("li");
								if (array1[i]["to"]=="0") {
									tli.setAttribute("class","sent");
								} else {
									tli.setAttribute("class","from");								
								}
								var messageText="<p><span>"+array1[i]["time"]+"</span>"+array1[i]["message"]+"</p>";
								tli.innerHTML = messageText;
								textbox.appendChild(tli);
							}
						}


}

function Request() {

this.poll = false;

this.activatePoll = function () {
    this.poll = true;
    this.runPoll();
};

this.disablePoll = function () {
    this.poll = false;
};

this.runPoll = function () {
    var self = this;
    var poll = setInterval(function () {
		var formData = new FormData();
		formData.append("userchat","conversationcontinue");
		formData.append("conversationid",token);
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == XMLHttpRequest.DONE) {
				if (xmlhttp.status == 200) {
					updateConversation(xmlhttp.responseText);
				}
				else if (xmlhttp.status == 400) {
				}
				else {
				}
			}
		};
		xmlhttp.open("POST", "chat/checkconversation");
		xmlhttp.send(formData);
		return false;
    }, 360000);
};
}

r = new Request();
r.activatePoll();
