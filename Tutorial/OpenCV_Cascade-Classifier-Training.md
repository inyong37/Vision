# [OpenCV Cascade Classifier Training](https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html)

:key: This tutorial will need to use `opencv_createsamples`, `opencv_annotation`, `opencv_traincascade`, and `opencv_visualisation`.

:key: `createsamples` and `traincascade` are disabled since OpenCV 4.0, therefore, tutorial needs to be conducted on 3.4 branch.

## Preparation of the training data

For training a boosted cascade of weak classifiers, it requires a set of positive samples (containing actual objects to detect) and a set of negative images (containing everything not to detect). The set of negative samples must be prepared manually, whereas set of positive samples is created using the opencv_createsamples application.

### Negative Samples

Negative samples are taken from arbitrary images, not containing objects you want to detect. These negative images, from which the samples are generated, should be listed in a special negative image file containing one image path per line (can be absolute or relative). Note that negative samples and sample images are also called background samples or background images, and are used interchangeably in this document.

Described images may be of different sizes. However, each image should be equal or larger than the desired training window size (which corresponds to the model dimensions, most of the times being the average size of your object), because these images are used to subsample a given negative image into several image samples having this training window size.

### Positive Samples

Positive samples are created by the opencv_createsamples application. They are used by the boosting process to define what the model should actually look for when trying to find your objects of interest. The application supports two ways of generating a positive sample dataset.

1. You can generate a bunch of positives from a single positive object image.
2. You can supply all the positives yourself and only use the tool to cut them out, resize them and put them in the opencv needed binary format.

:key: Many tutorials on the web even state that 100 real object images, can lead to a better model than 1000 artificially generated positives, by using the opencv_createsamples application.

The following procedure is used to create a sample object instance:
- The given source image is rotated randomly around all three axes. 
- Then pixels having the intensity from the [bg_color-bg_color_threshold; bg_color+bg_color_threshold] range are interpreted as transparent.
- White noise is added to the intensities of the foreground.
- If the `-inv` key is specified then foreground pixel intensities are inverted.
- If `-randinv` key is specified then algorithm randomly selects whether inversion should be applied to this sample.
- The obtained image is placed onto an arbitrary background from the background description file, resized to the desired size specified by `-w` and `-h` and stored to the vec-file, specified by the `-vec` command line option.

## Executing the actual model training

After the opencv_traincascade application has finished its work, the trained cascade will be saved in `cascade.xml` file in the `-data` folder. Other files in this folder are created for the case of interrupted training, so you may delete them after completion of training.

---

### Reference

- Cascade Classifier Training, https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html, 2023-01-25-Wed.
