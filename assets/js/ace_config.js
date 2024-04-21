// Getting the basic editor set
let editors = document.getElementsByClassName("editor");

// Elements for changing theme, language and font-size
var themes = document.getElementsByClassName("theme-select");
var langs = document.getElementsByClassName("lang-select");
var sizes = document.getElementsByClassName("size-select");
var codeInputs = document.getElementsByClassName("ace_control");

let editorLib = {
    init(editor) {
        // Theme
        editor.setTheme("ace/theme/monokai");
        // Set language
        editor.session.setMode("ace/mode/python");
        
        // Set options for code editor
        editor.setOptions({
            enableMultiselect: true,
            fontSize: '18px',
        });
    },
    changeTheme(editor, newTheme) {        
        editor.setTheme("ace/theme/"+newTheme);
    },
    changeLang(editor, newLang) {
        editor.session.setMode("ace/mode/"+newLang);
    },
    changeFontSize(editor, newSize) {
        editor.setFontSize(newSize);
    }
};

// Initial values
var editorObjects = []
for (let i = 0; i < editors.length; i++) {
    let theme = themes[i], lang = langs[i];
    editorObjects.push(ace.edit(editors[i]));
    editorLib.init(editorObjects[i]);
    editorLib.changeTheme(editorObjects[i], theme.value);
    editorLib.changeLang(editorObjects[i], lang.value);
}

// Change values on change selection.
for (let i = 0; i < editorObjects.length; i++) {
    let editor = editorObjects[i], theme = themes[i], lang = langs[i], fontsize = sizes[i];
    theme.addEventListener("change", function() {
        editorLib.changeTheme(editor, theme.value);
    });
    lang.addEventListener("change", function() {
        editorLib.changeLang(editor, lang.value);
    });
    fontsize.addEventListener("change", function() {
        editorLib.changeFontSize(editor, parseInt(fontsize.value));
    });
}

const copyCode = (editor, codeInput) => codeInput.value = editor.session.getValue();

// Making the submission on submit
for (let i = 0; i < editorObjects.length; i++) {
    let editor = editorObjects[i], codeInput = codeInputs[i];
    editor.addEventListener("load", () => copyCode(editor, codeInput));
    editor.addEventListener("change", () => copyCode(editor, codeInput));
}