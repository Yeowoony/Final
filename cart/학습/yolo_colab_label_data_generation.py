import os

current_path = os.path.abspath(os.curdir)
COLAB_DARKNET_ESCAPE_PATH = '/home/pi/cart/학습/'
COLAB_DARKNET_PATH = '/home/pi/cart/학습/'

YOLO_IMAGE_PATH = current_path + '/res_image'  #학습해야할 이미지 경로
YOLO_FORMAT_PATH = current_path + '/res_image'   #학습해야할 이미지 경로

class_count = 0
test_percentage = 0.2
paths = []

with open(COLAB_DARKNET_ESCAPE_PATH + 'classes.names', 'w') as names, \
     open(COLAB_DARKNET_ESCAPE_PATH + 'classes.txt', 'r') as txt:
    for line in txt:
        names.write(line)  
        class_count += 1
    print ("[classes.names] is created")

with open(COLAB_DARKNET_ESCAPE_PATH + 'custom_data.data', 'w') as data:
    data.write('classes = ' + str(class_count) + '\n')
    data.write('train = ' + COLAB_DARKNET_ESCAPE_PATH + 'train.txt' + '\n')
    data.write('valid = ' + COLAB_DARKNET_ESCAPE_PATH + 'test.txt' + '\n')
    data.write('names = ' + COLAB_DARKNET_ESCAPE_PATH + 'classes.names' + '\n')
    data.write('backup = backup')
    print ("[custom_data.data] is created")

os.chdir(YOLO_IMAGE_PATH)
for current_dir, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.jpg'):
            image_path = COLAB_DARKNET_PATH + 'res_image/' + f
            paths.append(image_path + '\n')


paths_test = paths[:int(len(paths) * test_percentage)]

paths = paths[int(len(paths) * test_percentage):]


with open(COLAB_DARKNET_ESCAPE_PATH + 'train.txt', 'w') as train_txt:
    for path in paths:
        train_txt.write(path)
    print ("[train.txt] is created")

with open(COLAB_DARKNET_ESCAPE_PATH + 'test.txt', 'w') as test_txt:
    for path in paths_test:
        test_txt.write(path)
    print ("[test.txt] is created")

