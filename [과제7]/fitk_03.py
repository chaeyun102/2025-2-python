def mergefiles(file1path, file2path, outputfilepath):
    with open(file1path, 'r', encoding='utf-8') as file1:
        file1content = file1.read()

    with open(file2path, 'r', encoding='utf-8') as file2:
        file2content = file2.read()

    mergedcontent = file1content + '\n' + file2content

    with open(outputfilepath, 'w', encoding='utf-8') as outputfile:
        outputfile.write(mergedcontent)

file1path = 'file1.txt'
file2path = 'file2.txt'
outputfilepath = 'output.txt'

mergefiles(file1path, file2path, outputfilepath)
