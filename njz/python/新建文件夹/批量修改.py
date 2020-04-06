import os
import scandir
def gbk_trans_utf8(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        content = f.read()
    with open(file_path, 'w', encoding='gbk') as f:
        f.write(content)

path = "E:\\Personal\\Documents\\GitHub\\MyEclipse 8.5\\clf\\src\\com"
fns = [os.path.join(root, fn) for root, dirs, files in scandir.walk(path) for fn in files]
for f in fns:
 gbk_trans_utf8(f)