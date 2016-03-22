import re
import sys

def remove_comments(text):
    return re.sub('\n\t*//.*', '', text)

if __name__ == '__main__':
    filepath = sys.argv[1]    
    filename = sys.argv[2]
    filepath2 = sys.argv[3]
    filepath3 = sys.argv[4]
    
    fullpath = filepath + filename
    
    code_w_comments = open(fullpath).read()
    code_wo_comments = remove_comments(code_w_comments)
    fh2 = open(filepath2+filename, "w")
    fh3 = open(filepath3+filename, "w")
    fh2.write(code_wo_comments)
    fh3.write(code_wo_comments)
    fh2.close()
    fh3.close()