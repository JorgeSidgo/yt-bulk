var path = require("path")
var os = require("os");



function getDownload(route) {

    var inputElement = document.getElementById('input');
    vueapp.toggleOverlay();
    vueapp.setMessage("Descargando...");

    if (route != null) {

        var options = {
            mode: 'text',
            pythonPath: path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'Python', 'Python38-32', 'python.exe'),
            pythonOptions: ['-u'],
            scriptPath: path.join(__dirname, '/../logic/'),
            args: [route]
        }

        PythonShell.run('download.py', options, (err, data) => {
            inputElement.value = "";
            vueapp.pushData(data);
            vueapp.setMessage(null);
            vueapp.startConvertion();
        });
    } else {
        alert('seleccione un archivo')
    }





}