// Password matching validation
$('.toast').toast('show')
var pwd = document.getElementById("pwd-input"), cnf = document.getElementById("cnf-pwd");

function validatePassword() {
    if(pwd.value != cnf.value) {
        cnf.setCustomValidity("Passwords don't match");
    } else {
        cnf.setCustomValidity("");
    }
}

pwd.onchange = validatePassword;
cnf.onkeyup = validatePassword;
