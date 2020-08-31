// Getting the basic editor set
var editor = ace.edit("editor");

// Elements for changing language and font-size
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
    changeLang(newLang) {
        editor.session.setMode("ace/mode/"+newLang);
    },
    changeFontSize(newSize) {
        editor.setFontSize(newSize);
    }
};

editorLib.init();
editorLib.changeLang(lang.value)


lang.addEventListener("change", function() {
    editorLib.changeLang(this.value);
});
size.addEventListener("change", function() {
    editorLib.changeFontSize(parseInt(this.value));
});
