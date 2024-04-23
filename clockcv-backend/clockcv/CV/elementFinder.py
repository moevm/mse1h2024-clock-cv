import cv2
import numpy as np
from .NumberAnalizer import NumberAnalizer
from .arrowAnalizer import ArrowAnalizer

class elementFinder():
    def __init__(self,image,prototype):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.arrows = []
        self.number_finder = NumberAnalizer(prototype)
        self.arrow_finder = ArrowAnalizer()
        self.numbers = [None for _ in range(12)]
        self.circle = None
        self.contours = []
        self.hierarchy = np.array([])
        self.useless = []
    
    def find_circle(self):
        gray_blurred = cv2.bitwise_not(cv2.GaussianBlur(self.gray, (7,7), 0)) 
        edges = cv2.Canny(gray_blurred, 50, 150, apertureSize=3)
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=4, param1=100, param2=70, minRadius=20, maxRadius=10000)
        drawn_circles = [[]]
        drawn_circles[0].append(circles[0,0])
        if circles is not None:
            drawn_circles = circles[0, :]   
            drawn_circles = [np.array(item, dtype=int) for item in drawn_circles]
            self.circle = np.array(np.mean(drawn_circles, axis=0), dtype=int)
        else:
            print('Круги не найдены на изображении.')
        _, threshold = cv2.threshold(self.gray, 127, 255, 0)
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in contours:
            c = cv2.boundingRect(i)
            radius = round(c[2] / 2)
            centerX =c[0] + round(c[2] / 2)
            centerY = c[1] + round(c[3] / 2)
            if (np.abs(self.circle[0] - centerX) < 40 and np.abs(self.circle[1] - centerY) < 40 and np.abs(self.circle[2] - radius) < 40):
                self.circle = [centerX, centerY,radius]
                break
        self.gray = cv2.cvtColor(self.delete_circles(), cv2.COLOR_BGR2GRAY)
    
    def delete_circles(self):
        image = self.image.copy()
        for y in range(self.circle[1] - self.circle[2] - 20, self.circle[1] + self.circle[2] + 20):
            for x in range(self.circle[0] - self.circle[2] - 20, self.circle[0] + self.circle[2] + 20):
                if np.all([100, 0, 0] <= image[y, x]) and np.all(image[y, x] <= [255, 255, 150]):
                    image[y, x] = [255, 255, 255]
        return image
    
    def find_contours(self):
        ret, threshold = cv2.threshold(self.gray, 127, 255, 0)
        contours, self.hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            dot = cv2.boundingRect(c)
            self.contours.append(dot)
          
    def find_numbers(self):
        self.number_finder.find_numbers(self.contours,self.numbers,self.gray, self.hierarchy, self.useless)
   
    def find_arrows(self,time):
        return self.arrow_finder.start(self.gray,self.numbers,self.circle,time)

    def draw_error(self, coord):
        x, y, w, h = coord
        for j in range(y, y + h):
            for i in range(x, x + w):
                if np.all(self.image[j, i] < 150):
                    self.image[j, i] = (0, 0, 255)
                    
    def check_inside(self):
        count = 0
        for num in self.numbers:
            if num:
                if self.number_finder.calculate_distance(self.number_finder.find_center(num),(self.circle[0], self.circle[1]))<self.circle[2]:
                    count+=1
                else:
                    self.draw_error(num)
        return count
    
    def check_sectors(self,sectors):
        count = 0
        angle = self.number_finder.get_angle(self.numbers, self.circle)
        for i in range(len(angle)):
            if angle:
                if angle[i] > sectors[i][0] and angle[i] < sectors[i][1]:
                    count+=1
                else: 
                    self.draw_error(self.numbers[i])
        return count