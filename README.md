# Kathmandu Road Dataset: Ratnapark to Tripureshwor

## Overview

This dataset comprises annotated images captured on the route from Ratnapark to Tripureshwor in Kathmandu, Nepal. It is designed for applications in object detection, traffic monitoring, autonomous driving, and smart city research.

## Dataset Information

- **Location:** Kathmandu, Nepal
- **Route Covered:** Ratnapark to Tripureshwor
- **Number of Images:** 156
- **Image Resolution:** 1920x1080 pixels
- **Annotations:** Bounding boxes and class labels

## Dataset Structure

```
Kathmandu_Road_Ratnapark_Tripureshwor/
├── img/
│   ├── frame_077.jpg
│   ├── frame_101.jpg
│   └── ...
├── labels/
│   ├── frame_001.txt
│   ├── frame__002.txt
│   └── ...
└── README.md
```

## Annotation Classes

The dataset annotations include the following object classes:

- Vehicles
- Pedestrians
- Traffic signs
- Traffic signals
- Animals
- Other vehicles
- Auto Rickshaw

Specifically annotated classes:

- vehicles
- pedestrians
- traffic\_signs
- traffic\_signal
- car
- motorcycle
- bus
- truck
- animal
- other\_vehicles
- auto\_rickshaw

## Quick Example

Example Python usage:

```python
import cv2

image = cv2.imread('img/frames_001.jpg')
# Annotation can be processed from the XML file
```

## License

This dataset is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Proper attribution is required.

## Citation

Please cite this dataset in your work as follows:

```
@misc{Maurya2025,
  author = {Nitesh Kumar Shah and Chandra Prakash Maurya and Navjot Singh and Kartikeya Gullapalli and Jahnavi Gadde},
  title = {Kathmandu Road Dataset: Ratnapark to Tripureshwor},
  year = {2025},
  url = {https://github.com/rbhdsks/Kathmandu_Road_Ratnapark_Tripureshwor}
}
```

## Contributors

- **Nitesh Kumar Shah**, Student, IIIT Allahabad ([iib2021002@iiita.ac.in](mailto\:iib2021002@iiita.ac.in))
- **Gadde Jahnavi**, Student, IIIT Allahabad ([iit2021190@iiita.ac.in](mailto\:iit2021190@iiita.ac.in))
- **Kartikeya Gullapalli**, Student, University of Texas, Austin
- **Chandra Prakash Maurya**, Research Scholar, IIIT Allahabad 
- **Prof. Dr. Navjot Singh**, Assistant Professor, IIIT Allahabad ([navjot@iiita.ac.in](mailto\:navjot@iiita.ac.in))

## License

This dataset is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Please cite appropriately.

---

Thank you for using our dataset. Contributions and suggestions are always welcome!

