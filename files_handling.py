

class file_extensions:

    def __init__(self, extension, file_name):
        self.extension = extension
        self.file_name = file_name

        if "python" in self.extension:
            exe = ".py"
        elif "javascript" in self.extension:
            exe = ".js"
        elif "php" in self.extension:
            exe = ".php"
        elif "html" in self.extension:
            exe = ".html"
        elif "css" in self.extension:
            exe = ".css"
        else:
            exe = ".txt"

        full_file = f"{self.file_name}{exe}"
        with open(full_file, "w") as fp:
            pass
