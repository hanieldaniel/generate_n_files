import os

current_dir = os.getcwd()
output_dir = 'output'
valid_int = False


while not valid_int:
    try:
        no_of_files = int(input('Enter the number of files needed: '))
        if no_of_files > 0:
            valid_int = True
        else:
            print("That's not a positive number. Try again")
    except ValueError:
        print("That's not an integer. Try again")


filename = str(input('Enter Filename Prefix: '))
# filename = slugify(filename)

ext = str(input('Enter File extension: '))
# ext = slugify(ext)


if not os.path.exists(os.path.join(current_dir, output_dir)):
    os.makedirs(os.path.join(current_dir, output_dir))

for x in range(no_of_files):
    file_name = os.path.join(current_dir, output_dir, filename + '_' + str(x+1) + '.' + ext)
    file = open(file_name, "w")
    file.close()

# f = open("demofile2.txt", "a")
