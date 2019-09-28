import cv2
import sys
import camera
import color_cast
import numpy as np
import matplotlib.pyplot as plt

if (sys.version[:1]=="3"): import _thread
else:import thread

def select_camera(last_index):
    number = 0
    hint = "Select a camera (0 to " + str(last_index) + "): "
    try:
        number = int(input(hint))
        # select = int(select)
    except Exception:
        print("It's not a number!")
        return select_camera(last_index)

    if number > last_index:
        print("Invalid number! Retry!")
        return select_camera(last_index)

    return number

if __name__ == "__main__":
    devices, n = camera.getAvailableCameras()
    print("请选择相机编号：")

    i = 0;
    while i < n:
        print("[",i,"]", devices[i])
        i += 1

    select = select_camera(i-1)
    print("You have select camera(%d)" %(select))

    cap = camera.open_camera(select)
    if cap.isOpened():
        width = cap.get(3)  # Frame Width
        height = cap.get(4)  # Frame Height
        print('Default width: ' + str(width) + ', height: ' + str(height))

        plt.axis([0, 100, 0, 300])
        plt.ion()
        xs = [0, 0]
        ys = [1, 1]
        i = 0

        while True:
            ret, frame = cap.read();
            # cv2.imshow("frame", frame)
            left_img, right_img = camera.split_frame(frame)
            #cv2.namedWindow("Left", cv2.WINDOW_AUTOSIZE)
            #cv2.namedWindow("Right", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("left", left_img)
            cv2.imshow("right", right_img)

            #print("\033[31mleft color_cast_factor :", color_cast.get_color_cast_factor(left_img))
            #print("\033[34mright_color_cast_factor:", color_cast.get_color_cast_factor(right_img))

            B_mean_left, G_mean_left, R_mean_left = color_cast.rgb_mean(left_img)
            #B_mean_right, G_mean_right, R_mean_right = color_cast.rgb_mean(right_img)
            #print("\033[31mLeft_image : RGB_Mean:", R_mean_left, G_mean_left, B_mean_left)
            #print("\033[34mRight_image: RGB_Mean:", R_mean_right, G_mean_right, B_mean_right)

            # drow the plot
            y = R_mean_left
            xs[0] = xs[1]
            ys[0] = ys[1]
            xs[1] = i
            ys[1] = y
            plt.plot(xs, ys, 'r-')
            plt.pause(0.000000000000001)
            i += 1
            if i > 95:
                plt.axis([i - 95, i+5, 0, 300])

            # key: 'ESC'
            key = cv2.waitKey(20)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
