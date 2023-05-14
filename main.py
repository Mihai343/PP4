import subprocess


class Handler:

    def __init__(self, successor=None):
        self.successor = successor

    def handle_file(self, filename):
        if self.successor:
            return self.successor.handle_file(filename)
        else:
            print("Nu am putut determina tipul fișierului.")


class KotlinHandler(Handler):
    def handle_file(self, filename):
        if filename.endswith(".kt"):
            subprocess.run(["kotlin", filename])
        else:
            super().handle_file(filename)


class PythonHandler(Handler):
    def handle_file(self, filename):
        if filename.endswith(".py"):
            subprocess.run(["python", filename])
        else:
            super().handle_file(filename)


class BashHandler(Handler):
    def handle_file(self, filename):
        if filename.endswith(".sh"):
            subprocess.run(["bash", filename])
        else:
            super().handle_file(filename)


class JavaHandler(Handler):
    def handle_file(self, filename):
        if filename.endswith(".java"):
            subprocess.run(["javac", filename])
            subprocess.run(["java", filename.split(".")[0]])
        else:
            super().handle_file(filename)


handler = Handler(JavaHandler(BashHandler(PythonHandler(KotlinHandler()))))
handler.handle_file("python.py")
