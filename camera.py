import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

def open_camera(index):
    cap = cv2.VideoCapture(index)
    return cap

def getAvailableCameras():
    # Return a string list
    available_cam= []
    i = 0
    available_dev = QtMultimedia.QCamera.availableDevices()
    # print("len=", len(available_dev))
    while i < len(available_dev):
        available_cam.append(QtMultimedia.QCamera.deviceDescription(QtMultimedia.QCamera.availableDevices()[i]))
        i += 1
    return available_cam, i


def split_frame(img):
    size = img.shape
    height = size[0]
    width  = size[1]

    mid = int(width/2)
    left_img = img[0:height, 0:mid]
    right_img= img[0:height, mid:width]

    return left_img, right_img


# if __name__ == "__main__":
#     print(getAvailableCameras())
