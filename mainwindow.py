import cv2
import numpy as np
from PySide6.QtWidgets import QMainWindow,QFileDialog
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Qt,QTimer
from ui_mainwindow import Ui_MainWindow
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


from functions.filters.add_noise import salt_pepper_noise,gaussian_noise,uniform_noise
from functions.filters.noise_filters import average_filter,gaussian_filter,median_filter
from functions.filters.edge_detection_filters import sobel_edge_detection,roberts_edge_detection,prewitt_edge_detection,canny_edge_detection
from functions.hough_detection import hough_line, hough_circle
from functions.active_contour import active_contour
from functions.normalize_and_equalize_image import equalization,normalization
from functions.draw_colored_histogram import rgb_hist_cumulative
from functions.harris_detection import harris_corner_detection
from functions.thresholding import global_threshold, local_threshold
from functions.main_functions import ThresholdMethod
from functions.segmentation.agglomerative import agglomerative_clustering
from functions.segmentation.k_means import K_means_segmentation
from functions.segmentation.mean_shift import mean_shift_method
from functions.segmentation.region_growing import region_growing_method
from functions.face_recognition import detect_faces, get_reference_images, apply_pca, draw_roc_curve
from functions.hybrid_images import hybrid_image
from functions.sift import featureMatch

# Get the reference images and the their labels
references = get_reference_images()

# Get the weights, eigen vectors and eigen values of the vector
pca_params = apply_pca(references[2])

x_train, x_test, y_train, y_test = train_test_split(pca_params[0], references[1],test_size=0.2,random_state=42)

model = LogisticRegression(multi_class='multinomial', solver='lbfgs',max_iter=1000)
model.fit(x_train, y_train)

y_prob = model.predict_proba(x_test)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Computer Vision Project")
        self.setWindowIcon(QPixmap("assets/eye.png"))

        self.homeImagePath = ""
        self.hybridInputImagePaths = []
        self.siftInputImagePaths = []

        self.noise_btn.clicked.connect(self.apply_noise)
        self.edge_btn.clicked.connect(self.apply_edge_detection)
        self.hough_btn.clicked.connect(self.apply_hough_transform)
        self.contour_btn.clicked.connect(self.apply_active_contour)
        self.histogram_btn.clicked.connect(self.apply_histogram)
        self.rgbhist_btn.clicked.connect(self.show_rgb_histograms)
        self.harris_btn.clicked.connect(self.apply_harris_operator)
        self.threshold_btn.clicked.connect(self.apply_threshold)
        self.segment_btn.clicked.connect(self.apply_segmentation)
        self.facedetect_btn.clicked.connect(self.apply_face_detection)
        self.homebrowse_btn.clicked.connect(self.home_browse_image)
        self.reset_btn.clicked.connect(self.reset_image)

        self.hybridbrowse_btn.clicked.connect(self.hybrid_browse_images)
        self.miximages_btn.clicked.connect(self.hybrid_mix_images)

        self.siftbrowse_btn.clicked.connect(self.sift_browse_images)
        self.matchfeatures_btn.clicked.connect(self.sift_match_features)

    def apply_noise(self):
        image = cv2.imread(self.homeImagePath)

        if self.saltandpepper_radio.isChecked():
            noisy_image = salt_pepper_noise(image)
        elif self.gaussian_radio.isChecked():
            noisy_image = gaussian_noise(image)
        elif self.uniform_radio.isChecked():
            noisy_image = uniform_noise(image)

        if self.average_radio.isChecked():
            output_image = average_filter(noisy_image)
        elif self.gaussianf_radio.isChecked():
            output_image = gaussian_filter(noisy_image)
        elif self.median_radio.isChecked():
            output_image = median_filter(noisy_image)

        cv2.imwrite("assets/home_image.png",output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
    
    def apply_edge_detection(self):
        image = cv2.imread(self.homeImagePath)
        if self.sobel_radio.isChecked():
            _,_,output_image = sobel_edge_detection(image)
        elif self.roberts_radio.isChecked():
            output_image = roberts_edge_detection(image)
        elif self.prewitt_radio.isChecked():
            output_image = prewitt_edge_detection(image)
        elif self.canny_radio.isChecked():
            output_image = canny_edge_detection(image)

        cv2.imwrite("assets/home_image.png",output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def apply_hough_transform(self):
        image = cv2.imread(self.homeImagePath)
        edge = canny_edge_detection(image)
        if self.line_radio.isChecked():
            output_image = hough_line(image, edge)
        elif self.circle_radio.isChecked():
            output_image = hough_circle(image, edge)
        elif self.ellipse_radio.isChecked():
            print("Ellipse Detection")

        cv2.imwrite("assets/home_image.png",output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def apply_active_contour(self):
        image = cv2.imread(self.homeImagePath)
        cv2.circle(image,self.center_spinbox,self.radius_spinbox,(255,0,0), 2)

        init = np.array([self.radius_spinbox, self.center_spinbox]).T
        snake = active_contour(gaussian_filter(image),init)
        cv2.polylines(image, snake, True, (0, 0, 255), 2)

        cv2.imwrite("assets/home_image.png", image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def apply_histogram(self):
        image = cv2.imread(self.homeImagePath)
        if self.normalize_radio.isChecked():
            output_image = normalization(image)
        elif self.equalize_radio.isChecked():
            output_image = equalization(image)

        cv2.imwrite("assets/home_image.png", output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def show_rgb_histograms(self):
        image = cv2.imread(self.homeImagePath)        
        rgb_hist_cumulative(image)


    def apply_harris_operator(self):
        image = cv2.imread(self.homeImagePath)        
        output_image = harris_corner_detection(image)

        cv2.imwrite("assets/home_image.png", output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def apply_threshold(self):
        image = cv2.imread(self.homeImagePath)        

        if self.threshold_combobox.currentIndex() == 0:  # Global
            if self.otsu_radio.isChecked():
                output_image = global_threshold(image,method=ThresholdMethod.OTSU)
            elif self.optimal_radio.isChecked():
                output_image = global_threshold(image,method=ThresholdMethod.OPTIMAL)
            elif self.spectral_radio.isChecked():
                output_image = global_threshold(image,method=ThresholdMethod.SPECTRAL)
        
        elif self.threshold_combobox.currentIndex() == 1:  # Local
            if self.otsu_radio.isChecked():
                output_image = local_threshold(image,method=ThresholdMethod.OTSU)
            elif self.optimal_radio.isChecked():
                output_image = local_threshold(image,method=ThresholdMethod.OPTIMAL)
            elif self.spectral_radio.isChecked():
                output_image = local_threshold(image,method=ThresholdMethod.SPECTRAL)

        cv2.imwrite("assets/home_image.png", output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def apply_segmentation(self):
        image = cv2.imread(self.homeImagePath)        

        if self.kmeans_radio.isChecked():
            output_image = K_means_segmentation(image)
        if self.regiongrowing_radio.isChecked():
            output_image = region_growing_method(image)
        if self.agglomerative_radio.isChecked():
            output_image = agglomerative_clustering(image)
        if self.meanshift_radio.isChecked():
            output_image = mean_shift_method(image)

        cv2.imwrite("assets/home_image.png", output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def apply_face_detection(self):
        image = cv2.imread(self.homeImagePath)        
        output_image = detect_faces(image, pca_params, model)
        
        cv2.imwrite("assets/home_image.png", output_image)
        self.homeimage_lbl.setPixmap(QPixmap("assets/home_image.png").scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def home_browse_image(self):
        fileName = QFileDialog.getOpenFileName(self,"Select Image",filter="Image File (*.png *.jpg *.jpeg)")
        self.homeImagePath = fileName[0]
        self.homeimage_lbl.setPixmap(QPixmap(self.homeImagePath).scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))

    def reset_image(self):
        self.homeimage_lbl.setPixmap(QPixmap(self.homeImagePath).scaled(self.homeimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))



    def hybrid_browse_images(self):
        filesNames = QFileDialog.getOpenFileNames(self,"Select Images",filter="Image File (*.png *.jpg *.jpeg)")
        self.hybridInputImagePaths = filesNames[0]

        self.hybridinputimage1_lbl.setPixmap(QPixmap(self.hybridInputImagePaths[0]))
        self.hybridinputimage2_lbl.setPixmap(QPixmap(self.hybridInputImagePaths[1]))


    def hybrid_mix_images(self):
        input_image1 = cv2.imread(self.hybridInputImagePaths[0])        
        input_image2 = cv2.imread(self.hybridInputImagePaths[1])

        output_image = hybrid_image(input_image1, input_image2)

        cv2.imwrite("assets/hybrid_image.png", output_image)
        self.hybridoutputimage_lbl.setPixmap(QPixmap("assets/hybrid_image.png").scaled(self.hybridoutputimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))



    def sift_browse_images(self):
        filesNames = QFileDialog.getOpenFileNames(self,"Select Images",filter="Image File (*.png *.jpg *.jpeg)")
        self.siftInputImagePaths = filesNames[0]

        self.siftinputimage1_lbl.setPixmap(QPixmap(self.siftInputImagePaths[0]))
        self.siftinputimage2_lbl.setPixmap(QPixmap(self.siftInputImagePaths[1]))


    def sift_match_features(self):

        input_image1 = cv2.imread(self.siftInputImagePaths[0])        
        input_image2 = cv2.imread(self.siftInputImagePaths[1])

        output_image = featureMatch(input_image1,input_image2)

        cv2.imwrite("assets/sift_image.png", output_image)
        self.siftoutputimage_lbl.setPixmap(QPixmap("assets/sift_image.png").scaled(self.siftoutputimage_lbl.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def start_webcam(self):
        # Create a video capture object
        self.camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        # Set the frame size to match the label size
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.VideoFeed.width())
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.VideoFeed.height())
    
        # Create a timer to update the video stream
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)  # 5 milliseconds

    def stop_webcam(self):
        self.camera.release()

    def update_frame(self):
        if self.camera.isOpened():
            # Read the frame
            stream, frame = self.camera.read()
            flipped_frame = cv2.flip(frame, 1)

            flipped_frame = detect_faces(flipped_frame, pca_params, model)

            # Convert the frame to RGB format
            flipped_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)

            # Create a QImage from the frame data
            img = QImage(flipped_frame, flipped_frame.shape[1], flipped_frame.shape[0], QImage.Format_RGB888)

            # Create a QPixmap from the QImage
            pix = QPixmap.fromImage(img)

            # Set the pixmap on the label to display the video stream
            self.VideoFeed.setPixmap(pix)

    def draw_roc_curve(self):
        draw_roc_curve(y_test, y_prob, 5)