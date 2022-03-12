import glob, os

current_dir = '/home/paula/Escritorio/obj' # Path where data is

filename = 'pool_swimmer_004_A_' # Name to find and later, rename file

files_list = [] # Vector to store numbers to change
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*")):
      if pathAndFilename.find(filename) != -1:
        # For each file, if its name is the selected one, obtain its number and store it
        separated = pathAndFilename.split("/")
        file_name = separated[5].split("_")
        num_filename = file_name[4].split(".")[0]
        files_list.append(num_filename)

files_list.sort() # Sort vector to know the order to rename files
order = '0082' # First number of images list
for i in files_list:
  if i != order: # If the file number is not the order one, change it
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*")):
      if pathAndFilename.find(filename + str(i)) != -1: 
        separated = pathAndFilename.split("/") # Obtain its number and rename
        os.rename(pathAndFilename, (current_dir + '/' + filename + order + '.txt'))
  # Next file
  order_int = int(order) + 1
  order = str(order_int)
  if len(order) < 4:
    if len(order) == 3:
      order = '0' + order
    elif len(order) == 2:
      order = '00' + order
    elif len(order) == 1:
      order = '000' + order