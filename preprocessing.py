import xml.etree.ElementTree as ET
import os
from glob import glob

def convert_bbox_to_yolo(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_file, output_path):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    classes = {"Vehicle_Bus": 0, "TrafficSign_Else": 1, "Vehicle_Unknown": 2}

    out_file = open(output_path, 'w')

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes[cls]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
        bb = convert_bbox_to_yolo((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    out_file.close()

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for xml_file in glob(os.path.join(input_dir, '*.xml')):
        base_name = os.path.splitext(os.path.basename(xml_file))[0]
        txt_file = os.path.join(output_dir, base_name + '.txt')
        convert_annotation(xml_file, txt_file)

# 처리할 디렉토리 목록
directories = ['train', 'test', 'val']

for directory in directories:
    input_dir = os.path.join('C:/Users/mong3/Desktop/code/graduate/data', directory, 'labels')
    output_dir = os.path.join('C:/Users/mong3/Desktop/code/graduate/data', directory, 'labels_yolo')
    process_directory(input_dir, output_dir)

print("변환 완료!")