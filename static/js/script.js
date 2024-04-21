// Show bootstrap toasts    ---------------------------------------------------------------------
$('.toast').toast('show');

// User login   ---------------------------------------------------------------------------------
// Password matching validation
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

// Solution submit form    ----------------------------------------------------------------------
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

// Sort the options in select tags --------------------------------------------
var sortOptions = function(options) {
    Array.prototype.sort.call(options, function(a, b) {
        if (a.text <= b.text)   return -1
        else                    return 1
    });
};
var selector = document.getElementById("id_tag");
if (selector != null) {
    sortOptions(selector.options);
}

// Adding new tags for questions -----------------------------------------------
var tagInput = document.getElementById("tag-name");

var addNewTag = function() {
    let data = tagInput.value;
    console.log('Adding new tag...')
    $.ajax({
        url: "/add_tag",
        data: {
            'tag_name': data,
        },
        datatype: 'json',
        success: function(result) {
            tagInput.value = '';
            if (!result.present) {
                // Use the returned object to append to the select list
                let addedOption = new Option(result.text, result.value);
                optionList.add(addedOption);
                sortOptions(optionList);
            }
            else 
                $("#tag-insert-error").html(result.errorMessage);
        }
    });

};

// If Add button is clicked
$("#add-tag").on("click", addNewTag);

// If Enter is pressed inside the #tag-name input area
$("#tag-name").on("keypress", function(event) {
    if (event.key === "Enter" || event.keyCode === 13) 
    addNewTag();
});