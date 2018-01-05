import os

code_path = r'D:\projectFile\GraphicsViewEx01'
file_cnt, code_line_cnt, blank_line_cnt, comment_line_cnt = 0,0,0,0
for root,dirs,files in os.walk(code_path):
    for f in files:
        if f.endswith('.cpp'):
            file_cnt += 1
            with open(os.path.join(root,f),'r') as cur_f:
                for line in cur_f:
                    if line.strip().startswith('//'):
                        comment_line_cnt += 1
                    elif line.isspace():
                        blank_line_cnt += 1
                    else:
                        code_line_cnt += 1
print "file_cnt, code_line_cnt, blank_line_cnt, comment_line_cnt:"
print file_cnt,code_line_cnt,blank_line_cnt,comment_line_cnt