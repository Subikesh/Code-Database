// Getting the basic editor set
var editor = ace.edit("editor");

// Elements for changing theme, language and font-size
var theme = document.getElementById("theme-select");
var lang = document.getElementById("lang-select");
var size = document.getElementById("size-select");

let editorLib = {
    init() {
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
    changeTheme(newTheme) {
        editor.setTheme("ace/theme/"+newTheme);
    },
    changeLang(newLang) {
        editor.session.setMode("ace/mode/"+newLang);
    },
    changeFontSize(newSize) {
        editor.setFontSize(newSize);
    }
};

editorLib.init();
editorLib.changeTheme(theme.value);
editorLib.changeLang(lang.value);

theme.addEventListener("change", function() {
    editorLib.changeTheme(this.value);
});
lang.addEventListener("change", function() {
    editorLib.changeLang(this.value);
});
size.addEventListener("change", function() {
    editorLib.changeFontSize(parseInt(this.value));
});
