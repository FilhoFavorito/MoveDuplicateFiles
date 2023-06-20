import filecmp
import os
import shutil
from pyuac import main_requires_admin

@main_requires_admin
def main():
    directory = "C:/Users/Sonias/coisa/recuperado/"
    base_file = "C:/Users/Sonias/coisa/recuperado/_1.doc"

    new_dir = "duplicates"
    path = os.path.join(directory,new_dir)
    if os.path.isdir(path) == False:
        os.mkdir(path)

    for current_file in os.listdir(directory)[1::]:
        if filecmp.cmp(base_file,f"{directory}/{current_file}", shallow=False) and f"{directory}/{current_file}" != base_file :
            shutil.move(f"{directory}/{current_file}", f"{path}/{current_file}")

if __name__ == "__main__":
    main()
