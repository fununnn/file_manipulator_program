import sys
class Filemanuplator:
    def reverseFile(input_path,output_path):
    file = open(input_path)
    contents = file.read().reverse()
    file.close()
    output_path = contents

    def validationFiles(input_path,output_path):
        if 