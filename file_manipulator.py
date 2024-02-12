import sys
class Filemaniplator:
    def __init__(self) :
        self.method = None
        self.input_path = None
        self.output_path = None
        self.number = 1
        self.contents = ""
        self.validationArgv()

    def validationArgv(self):
        if len(sys.argv) < 4:
            print("ERROR: Insufficient arguments. file_manipurator.py, method, input_path, output_path")
            sys.exit(1)
        self.method = sys.argv[1]
        self.input_path = sys.argv[2]
        self.output_path = sys.argv[3]

        if self.method not in ["reverse", "copy", "duplicate-contents", "replace-string"]:
            print("ERROR: Method is something wrong. method: 'reverse', 'copy', 'duplicate-contents', 'replace-string'")            
            sys.exit(1)

        if self.method == "duplicate-contents":
            self.number = int(sys.argv[4])

    def reverseFile(self):
        with open(self.input_path) as f:
            self.contents = f.read()

        reverse_contents = self.contents[::-1]
        
        with open(self.output_path,"w") as f:
            f.write(reverse_contents)
            
    def copyFile(self):
        with open(self.input_path) as f:
            self.contents = f.read()

        with open(self.output_path,"w") as f:
            f.write(self.contents)  

    def duplicateContents(self):
        with open(self.input_path) as f:
            self.contents = f.read()

        with open(self.output_path,"w") as f:
            f.write(self.contents * self.number)  

    def replaceString(self):
        with open(self.input_path) as f:
            self.contents = f.read()

        replace_contents = self.contents.replace("needle","newstring")

        with open(self.output_path,"w") as f:
            f.write(replace_contents)  

    def main(self):
        if self.method == "reverse" :
            return self.reverseFile() 
        elif self.method == "copy":
            return self.copyFile()
        elif self.method == "duplicate-contents" :
            return self.duplicateContents()
        elif self.method == "replace-string" :
            return self.replaceString() 

if __name__ == "__main__":
    file_namipurator = Filemaniplator()
    file_namipurator.main()