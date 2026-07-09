import subprocess

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
    "explorer": "explorer",
    "vscode": "code"
}

def open_application(app):
    app_name = app.lower()

    if app_name not in APPS:
        return False, f"I don't know how to open {app_name}."

    try:
        subprocess.Popen(APPS[app_name])
        return True, f"Opening {app_name}."
    except Exception as e:
        return False, f"ERROR: {e}"