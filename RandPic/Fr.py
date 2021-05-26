import os

if __name__ == '__main__':
    filelist = os.listdir("C:/UnknowFile/HDfile/Wallpaper")
    with open('C:/UnknowFile/HDfile/RandPic/img.txt','w') as f:
        for file in filelist:
            f.write("https://cdn.jsdelivr.net/gh/HRiver2/HDfile@main/Wallpaper/"+file+'\n')
