def read_file_content (filename):
    f = open(str(filename) + ".txt" + "r")
    filename= f.read()
    f.close()
    return filename

def count_words():
    text = read_file_content("./story.txt")
    #[assignment] Add your code here
    output = {}
    for word in text.split():
        if word not in output.keys():
            output[word] = 0
        output[word] +=1
    return output

