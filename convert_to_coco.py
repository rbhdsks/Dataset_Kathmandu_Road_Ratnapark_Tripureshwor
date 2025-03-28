import os
import json
import cv2

def convert_to_coco(
    images_dir,       # path to your images, e.g. ".../img/"
    labels_dir,       # path to your YOLO-style labels, e.g. ".../labels/"
    classes_file,     # path to classes.txt
    output_json_path  # path to save the resulting COCO JSON
):
    # 1. Read the list of class names
    with open(classes_file, 'r') as f:
        class_names = [line.strip() for line in f if line.strip()]

    # 2. Prepare the COCO dictionary structure
    coco_output = {
        "info": {
            "description": "Custom Dataset",
            "version": "1.0",
            "year": 2023,
            "contributor": "",
            "date_created": ""
        },
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": []
    }

    # 3. Fill in the categories (one entry per class)
    for idx, name in enumerate(class_names):
        coco_output["categories"].append({
            "id": idx,
            "name": name,
            "supercategory": "none"
        })

    annotation_id = 1
    image_id = 1

    # 4. Loop over each image file in images_dir
    for filename in os.listdir(images_dir):
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
            continue

        # Full path to the image
        image_path = os.path.join(images_dir, filename)
        # Read the image to get its shape (for converting from normalized coords)
        img = cv2.imread(image_path)
        if img is None:
            print(f"Warning: could not read {image_path}, skipping.")
            continue
        height, width, _ = img.shape

        # 5. Add image entry to the COCO 'images' field
        coco_output["images"].append({
            "id": image_id,
            "file_name": filename,
            "height": height,
            "width": width
        })

        # 6. Look for a corresponding label file with the same base name
        base_name = os.path.splitext(filename)[0]
        label_file = os.path.join(labels_dir, base_name + '.txt')

        if os.path.exists(label_file):
            with open(label_file, 'r') as lf:
                lines = lf.readlines()
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    # typical YOLO: class_id, x_center, y_center, w, h
                    class_id = int(parts[0])
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    w = float(parts[3])
                    h = float(parts[4])

                    # Convert from normalized coords to absolute coords
                    # x_center, y_center, w, h are in [0, 1]
                    abs_x_center = x_center * width
                    abs_y_center = y_center * height
                    abs_w = w * width
                    abs_h = h * height

                    # Convert [x_center, y_center, w, h] to [x_min, y_min, w, h]
                    x_min = abs_x_center - abs_w / 2
                    y_min = abs_y_center - abs_h / 2

                    # 7. Append annotation
                    coco_output["annotations"].append({
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": class_id,
                        "bbox": [x_min, y_min, abs_w, abs_h],
                        "area": abs_w * abs_h,
                        "iscrowd": 0
                    })
                    annotation_id += 1

        # increment the image ID after processing
        image_id += 1

    # 8. Save COCO JSON
    with open(output_json_path, 'w') as out_file:
        json.dump(coco_output, out_file, indent=4)
    print(f"COCO annotations saved to: {output_json_path}")

if __name__ == "__main__":
    # Adjust these paths as needed:
    images_dir = "/Users/zsres/Desktop/Dataset_Kathmandu_Road_Ratnapark_Tripureshwor/img"
    labels_dir = "/Users/zsres/Desktop/Dataset_Kathmandu_Road_Ratnapark_Tripureshwor/labels"
    classes_file = "/Users/zsres/Desktop/Dataset_Kathmandu_Road_Ratnapark_Tripureshwor/labels/classes.txt"
    output_json_path = "/Users/zsres/Desktop/Dataset_Kathmandu_Road_Ratnapark_Tripureshwor/annotations_coco.json"

    convert_to_coco(images_dir, labels_dir, classes_file, output_json_path)
