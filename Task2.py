import json

files=['./pos_0.png.json','./pos_10010.png.json','./pos_10492.png.json']

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('counseling3.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)