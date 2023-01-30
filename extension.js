const vscode = require("vscode");
const { exec } = require("child_process");

function activate(context) {
  let disposable = vscode.commands.registerCommand(
    "extension.runPython",
    function () {
      let editor = vscode.window.activeTextEditor;
      if (!editor) {
        console.log("Nofile");
        vscode.window.showErrorMessage("No file open to run!");
        return;
      }
      let filePath = editor.document.uri.fsPath;
      let command = `python main.py ${filePath}`;
      exec(command, (er, stdout, stderr) => {
        vscode.window.showInformationMessage(stdout);
      });
    }
  );

  context.subscriptions.push(disposable);
}
exports.activate = activate;
