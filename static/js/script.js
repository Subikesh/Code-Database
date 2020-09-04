// Password matching validation
$('.toast').toast('show');
var pwd = document.getElementById("pwd-input"), cnf = document.getElementById("cnf-pwd");

var  validatePassword = function() {
    if(pwd.value != cnf.value) {
        cnf.setCustomValidity("Passwords don't match");
    } else {
        cnf.setCustomValidity("");
    }
}
if (pwd && cnf) {
    pwd.onchange = validatePassword;
    cnf.onkeyup = validatePassword;
}

// Solution submit form
var titles = document.getElementsByClassName("form-title");
var links = document.getElementsByClassName("form-link");
var notes = document.getElementsByClassName("form-description");
var submits = document.getElementsByClassName("submit-solution");
var edits = document.getElementsByClassName("edit-solution");
// var cancels = document.getElementsByClassName("cancel-edit");

let display = (elem) => elem.classList.remove("d-none");
let erace = (elem) => elem.classList.add("d-none");

for (let i = 0; i < edits.length; i++) {
    edits[i].addEventListener("click", function(event) {
        erace(edits[i]);
        display(submits[i]);
        // display(cancels[i]);
        display(titles[i]);
        display(links[i]);
        display(notes[i]);
        notes[i].disabled = notes[i].readOnly = false;
        notes[i].classList.replace("form-control-plaintext","form-control")
        event.preventDefault()
    });
    // Reset button is not working as expected
    // cancels[i].addEventListener("click", function() {
    //     display(edits[i]);
    //     erace(submits[i]);
    //     erace(cancels[i]);
    //     erace(titles[i]);
    //     erace(links[i]);
    //     notes[i].disabled = notes[i].readOnly = true;
    //     notes[i].classList.replace("form-control", "form-control-plaintext");
    //     event.preventDefault();
    // });
}