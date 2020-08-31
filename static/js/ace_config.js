// Getting the basic editor set
var editor = ace.edit("editor");

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
    }
};

editorLib.init();