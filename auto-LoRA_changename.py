#擷取資料夾所有TXT 檔

def get_file_name(path):
    file_name = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.txt'):
                file_name.append(f)
    return file_name

#test
#get_file_name("C:\\Users\\vanla\\stable-diffusion-webui\\AI_project_5girls\\04_Olivia\\Olivia4-After\\100_OliviaB")

#read txt file
def read_txt(path):
    with open(path, 'r') as f:
        data = f.read()
    return data

#test
#read_txt("C:\\Users\\vanla\\stable-diffusion-webui\\AI_project_5girls\\04_Olivia\\Olivia4-After\\100_OliviaB\\00000-0-00078-666666.txt")


#Find & replace
def find_replace(txt_path, find, replace):
    with open(txt_path, 'r') as f:
        data = f.read()
    data = data.replace(find, replace)
    with open(txt_path, 'w') as f:
        f.write(data)

def Double_splash_path(path):
    return path.replace("\\", "\\\\")


#test
#find_replace("C:\\Users\\vanla\\stable-diffusion-webui\\AI_project_5girls\\04_Olivia\\Olivia4-After\\100_OliviaB\\00000-0-00078-666666.txt", "Olivia666", "Olivia777")

#Find & replace all
def find_replace_all(dir_path, find, replace):
    file_name = get_file_name(dir_path)
    for f in file_name:
        txt_path = os.path.join(dir_path, f)
        find_replace(txt_path, find, replace)



########
##main##
########

#資料夾位置
path=r'C:\Users\vanla\stable-diffusion-webui\AI_project_5girls\02_Lynn\Lynn666_After'
dir=Double_splash_path(path)

#Lora 的 training 資料夾中文本想改的名字
Original_name="a woman"
replace_name="Lynn666"

find_replace_all(dir, Original_name, replace_name)