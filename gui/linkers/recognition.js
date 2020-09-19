let {
    PythonShell
} = require('python-shell')
var path = require("path")
var os = require("os");



function getResponse() {

    var inputElement = document.getElementById('input');
    vueapp.toggleOverlay();
    vueapp.setMessage("Reconociendo...");

    if (inputElement.files.length > 0) {
        var filename = inputElement.files[0].path;
        vueapp.setRoute(filename);
        var options = {
            mode: 'text',
            pythonPath: path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'Python', 'Python38-32', 'python.exe'),
            pythonOptions: ['-u'],
            scriptPath: path.join(__dirname, '/../logic/'),
            args: [filename]
        }

        PythonShell.run('recognition.py', options, (err, data) => {
            inputElement.value = "";
            vueapp.pushData(data);
            vueapp.setMessage(null);
            vueapp.startDownload();
        });
    } else {
        alert('seleccione un archivo')
    }





}