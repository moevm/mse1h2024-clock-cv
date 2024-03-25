import cv2
import numpy as np
import sys
import math

class elementFinder():
    def __init__(self,image,prototype):
        self.image = image
        self.prototype = np.array(prototype)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.arrows = np.array([])
        self.numbers = []
        self.circle = None
        self.contours = []
        self.hierarchy = np.array([])
    
    def find_circle(self):
        gray_blurred = cv2.bitwise_not(cv2.GaussianBlur(self.gray, (7,7), 0)) 
        edges = cv2.Canny(gray_blurred, 50, 150, apertureSize=3)

        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=4, param1=30, param2=72, minRadius=20, maxRadius=10000)
        drawn_circles = [[]]
        drawn_circles[0].append(circles[0,0])

        if circles is not None:
            drawn_circles = circles[0, :]   
            drawn_circles = [np.array(item, dtype=int) for item in drawn_circles]
            self.circle = np.array(np.mean(drawn_circles, axis=0), dtype=int)
        else:
            print('Круги не найдены на изображении.')
    
    def find_contours(self):
        ret, threshold = cv2.threshold(self.gray, 127, 255, 0)
        
        contours, self.hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            
            dot = cv2.boundingRect(c)
            self.contours.append(dot)    
        for c in self.contours:
            radius = round(c[2] / 2)
            centerX =c[0] + round(c[2] / 2)
            centerY = c[1] + round(c[3] / 2)
            if (np.abs(self.circle[0] - centerX) < 20 and np.abs(self.circle[1] - centerY) < 20 and np.abs(self.circle[2] - radius) < 20):
                self.circle = [centerX, centerY,radius]
                break
    
    
        
    def find_numbers(self):
        for c in self.contours:
            #предполоагемый размер контура цифра, так как другие контуры это круг и стрелки, которые точно больше эттих размеров
            if c[2] <=30 and c[3] <=40:
                temp_image = self.gray[c[1] - 5 :c[1]+c[3] + 5, c[0] - 5:c[0]+c[2] + 5]
                for p in self.prototype:
                    result = cv2.matchTemplate(temp_image, p,cv2.TM_CCOEFF_NORMED)
                    threshold = 0.8
                    result = np.where(result >= threshold)
                    for pt in zip(*result[::-1]):
                        self.numbers.append(temp_image)
        print(len(self.numbers))
        print(self.contours)
        print(self.hierarchy)
          
    '''
     
    def find_arrows(self):
        pass
              
    def read_time(self):
        pass
    
    # 0 - нет чисел внутри
    # 1 - есть не все внутри
    # 2 - есть все внутри
    
    def check_inside(self):
        pass
    
    def check_sectors(self,sectors):
        pass
        
    '''
    