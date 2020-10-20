
def write_file(file_name, content):  # file_name:文件的名字；content：要写入的内容 
    """
        写入文件
    """
    with open(file_name, "w") as f: # with open:打开一个文件；"w"：写入；以写入"w"的方式打开with open文件名 file_name ，并把它赋值给 f
        f.write(content)   # 去写入我们传进来的内容content

def read_file(file_path): # file_path文件路径
    result = ""
    with open(file_path, "r") as f: # r 只读
        result = f.readline()

    return result

if __name__ == "__main__":
    # write_file("./user_token.txt", "1231435466577879")
    # token = read_file("./user_token.txt")
    # print(token)

    # write_file("./article_id.txt", "79")
    iid = read_file("./article_id.txt")
    print(iid)