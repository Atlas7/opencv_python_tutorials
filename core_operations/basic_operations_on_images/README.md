# Basic Operations on Images

See [OpenCV-Python Tutorials - Basic Operations on Images](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops) for the original tutorial.

# Demo Modify Image

Run the demo code `demo_modify_image.py`.

This covers:

- Accessing and Modifying pixel values
- Accessing Image Properties
- Image ROI (Region of Interest)
- Splitting and Merging Image Channels

Some screenshots:

Origina image:

![img_1](./screenshots/img_1)

Add a white pixel at row 100, column 150:

![img_2](./screenshots/img_2)

Add a red pixel at row 100, column 150:

![img_3](./screenshots/img_3)

Show the ball only:

![img_4](./screenshots/img_4)

Copy and paste the ball to somewhere else:

![img_5](./screenshots/img_5)

Image after split and merge:

![img_6](./screenshots/img_6)

Reduce the BGR red scale to 0:

![img_7](./screenshots/img_7)

# Demo Making Borders for Images (Padding)

Run the demo code `demo_add_border_to_image.py`.

Some snapshots:

Original image - no border:

![border_original.png](./screenshots/border_original.png)

Border Option - `cv2.BORDER_REPLICATE`:

![border_replicate.png](./screenshots/border_replicate.png)

Border Option - `cv2.BORDER_REFLECT`:

![border_reflect.png](./screenshots/border_reflect.png)

Border Option - `cv2.BORDER_REFLECT_101`:

![border_reflect_101.png](./screenshots/border_reflect_101.png)

Border Option - `cv2.BORDER_WRAP`:

![border_wrap.png](./screenshots/border_wrap.png)

Border Option - `cv2.BORDER_CONSTANT` (Blue):

![border_constant_blue.png](./screenshots/border_constant_blue.png)

# Conclusion

Some cool examples demonstrating basic operations around accessing and manipulating an image (matrix).
