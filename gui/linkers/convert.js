var path = require("path")
var os = require("os");



function getConvertion() {

    vueapp.toggleOverlay();
    vueapp.setMessage("Convirtiendo...");
    var options = {
        mode: 'text',
        pythonPath: path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'Python', 'Python38-32', 'python.exe'),
        pythonOptions: ['-u'],
        scriptPath: path.join(__dirname, '/../logic/'),
    }

    PythonShell.run('convert.py', options, (err, data) => {
        vueapp.pushData(data);
        vueapp.setMessage(null);
    });






}