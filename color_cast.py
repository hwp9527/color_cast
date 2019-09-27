import sys
import cv2
import math

def get_color_cast_factor(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(img)
    h,w,_ = img.shape
    da = a_channel.sum()/(h*w)-128
    db = b_channel.sum()/(h*w)-128
    histA = [0]*256
    histB = [0]*256
    for i in range(h):
        for j in range(w):
            ta = a_channel[i][j]
            tb = b_channel[i][j]
            histA[ta] += 1
            histB[tb] += 1
    msqA = 0
    msqB = 0
    for y in range(256):
        msqA += float(abs(y-128-da))*histA[y]/(w*h)
        msqB += float(abs(y - 128 - db)) * histB[y] / (w * h)
    result = math.sqrt(da*da+db*db)/math.sqrt(msqA*msqA+msqB*msqB)
    #print("d/m = %s"%result)
    return result


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(a, "=", get_color_cast_factor(a))

