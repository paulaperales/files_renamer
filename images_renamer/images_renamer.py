import glob, os

current_dir = '/home/paula/Escritorio/' # Path where images folder are

filename = 'barbados_scuba_005_A' # Name of images

init_number = '0001'

for pathAndFilename in glob.iglob(os.path.join(current_dir + filename, "*.jpg")):
    # For each image, if its name is not the correct one, rename it
    print(pathAndFilename, (current_dir + filename + '_' + init_number + '.jpg'))
    #os.rename(pathAndFilename, (current_dir + filename + init_number + '.jpg'))
    number_int = int(init_number) + 1
    init_number = str(number_int)
    if len(init_number) < 4:
        if len(init_number) == 3:
            init_number = '0' + init_number
        elif len(init_number) == 2:
            init_number = '00' + init_number
        elif len(init_number) == 1:
            init_number = '000' + init_number


