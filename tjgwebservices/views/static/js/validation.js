function registerValidation(){

					var pwInput = document.getElementById("psw");
					var confirmInput = document.getElementById("pswconfirm");
					var letter = document.getElementById("letter");
					var capital = document.getElementById("capital");
					var number = document.getElementById("number");
					var length = document.getElementById("length");
					var matchpw = document.getElementById("match");
					var registerButton = document.getElementById("register");

					confirmInput.onfocus = function() {
					  document.getElementById("message").style.display = "block";
					}

					confirmInput.onblur = function() {
					  document.getElementById("message").style.display = "none";
					}

					confirmInput.onkeyup = function() {
					  // Validate lowercase letters
					  var lowerCaseLetters = /[a-z]/g;
					  if(confirmInput.value.match(lowerCaseLetters)) { 
						letter.classList.remove("invalid");
						letter.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						letter.classList.remove("valid");
						letter.classList.add("invalid");
						registerButton.disabled = true;
					}

					  // Validate capital letters
					  var upperCaseLetters = /[A-Z]/g;
					  if(confirmInput.value.match(upperCaseLetters)) { 
						capital.classList.remove("invalid");
						capital.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						capital.classList.remove("valid");
						capital.classList.add("invalid");
						registerButton.disabled = true;
					  }

					  // Validate numbers
					  var numbers = /[0-9]/g;
					  if(confirmInput.value.match(numbers)) { 
						number.classList.remove("invalid");
						number.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						number.classList.remove("valid");
						number.classList.add("invalid");
						registerButton.disabled = true;
					  }

					  // Validate length
					  if(confirmInput.value.length >= 8) {
						length.classList.remove("invalid");
						length.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						length.classList.remove("valid");
						length.classList.add("invalid");
						registerButton.disabled = true;
					  }
					  
					  // Validate match
					  if(confirmInput.value === pwInput.value) {
						matchpw.classList.remove("invalid");
						matchpw.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						matchpw.classList.remove("valid");
						matchpw.classList.add("invalid");
						registerButton.disabled = true;
					  }

					}


}
