import os
from pixellib.instance import instance_segmentation

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def get_object_detection():
    segment_image = instance_segmentation()
    segment_image.load_model("/home/domochevsky/python/practice_bot/mask_rcnn_coco.h5")

    result = segment_image.segmentImage(
        image_path=f"/home/domochevsky/python/practice_bot/one.jpg",
        output_image_name=f"two.jpg",
        show_bboxes=True
    )
    return len(result[0]['scores'])

