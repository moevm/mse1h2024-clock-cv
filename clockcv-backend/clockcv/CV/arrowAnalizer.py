import cv2
import numpy as np
import sys
import math
'''
из финдера будет подгружаться инфа о контурах,        сделано
очистить изображение от цифер                         сделано
найти контур стрелок, затем нужно пройтись по контуру стрелок по всему и найти точку, 
которая ближе всех к центру окружности, закрасить ее белым кругом, снова найти контуры стрелок раздельно,           сделано
'''
class ArrowAnalizer():
    def __init__(self):
        self.arrows = []
        self.clean_image = None
        self.found_time = None
        self.arrow_contour = None
        self.error_rate = 0
        self.center = [0,0]
        self.dots = []
        self.angles = []
            
    def clear_image(self,gray,numbers):
        self.clean_image = gray
        for num in numbers:
            fill = np.full((num[3], num[2]), 255)
            self.clean_image[num[1]: num[1] + num[3], num[0] : num[0] + num[2]] = fill
    
    def start(self,gray,numbers,circle,time):
        self.clear_image(gray,numbers)
        self.print_center(circle)
        self.find_arrows()
        self.find_edge_dots(circle)
        self.find_angles(circle)
        self.find_time()
        return self.find_error_rate(time)
    
    def print_center(self,circle):
        self.center = circle[:2]
        _, threshold = cv2.threshold(self.clean_image, 127, 255, 0)
        contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours1 = []
        for c in contours:
            dot = cv2.boundingRect(c)
            contours1.append(dot)  
        for i in range(len(contours1)):
            if hierarchy[0, i, -1] == 2:
                self.arrow_contour = contours1[i]
        minimum = 10000000
        for i in range(self.arrow_contour[1], self.arrow_contour[1] + self.arrow_contour[3]):
            for j in range(self.arrow_contour[0], self.arrow_contour[0] + self.arrow_contour[2]):
                if (i - circle[1]) ** 2 + (j - circle[0]) ** 2 < minimum:
                    minimum = (i - circle[1]) ** 2 + (j - circle[0]) ** 2
                    self.center = [i,j]
        fill = np.full((40, 40), 255)
        self.clean_image[self.center[0] - 20: self.center[0] + 20, self.center[1] - 20: self.center[1] + 20] = fill
        
        
    def find_arrows(self):
        _, threshold = cv2.threshold(self.clean_image, 127, 255, 0)
        contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i, c in enumerate(contours):
            dot = cv2.boundingRect(c)
            if hierarchy[0, i, -1] == 2:
                self.arrows.append(dot)
                cv2.rectangle(self.clean_image,(dot[0],dot[1]),(dot[0]+dot[2],dot[1]+dot[3]),(0,255,0),2)
                
        
        
    
    def find_edge_dots(self,circle):
        if self.arrows[0][2] ** 2 + self.arrows[0][3] ** 2 > self.arrows[1][2] ** 2 + self.arrows[1][3] ** 2:
            self.arrows[0], self.arrows[1] = self.arrows[1], self.arrows[0]


        for ar in self.arrows:
            maxi = 0
            x,y = 0,0
            for i in range(ar[1],ar[1] + ar[3]):
                for j in range(ar[0],ar[0] + ar[2]):
                    if (circle[0] - j) ** 2 + (circle[1] - i) ** 2 > maxi and self.clean_image[i,j] == 0:
                        maxi = (circle[0] - j) ** 2 + (circle[1] - i) ** 2
                        x,y =  j,i
            self.dots.append((x,y))
        
           
    def find_angles(self,circle):
        A = np.array([circle[0], circle[1] - circle[2]])
        B = np.array([circle[0], circle[1]])
        for dot in self.dots:
            C = np.array(dot)
            BA = A - B
            BC = C - B
            angle_rad = np.arctan2(BC[1], BC[0]) - np.arctan2(BA[1], BA[0])
            angle_deg = np.degrees(angle_rad)
            if angle_deg < 0:
                angle_deg += 360
            self.angles.append(angle_deg)
        cv2.line(self.clean_image,(circle[0] - circle[2],circle[1]), (circle[0] + circle[2],circle[1]),(0,0,255),1)
        cv2.line(self.clean_image,(circle[0], - circle[2]+circle[1]), (circle[0], circle[2] + circle[1]),(0,0,255),1)

        
    
    def find_time(self):
        minutes = np.floor(self.angles[1] / 360 * 60) % 60
        hours = np.floor(self.angles[0] / 360 * 12) % 12
        self.found_time = (hours,minutes)
    
    def find_error_rate(self,time):
        if np.abs(self.arrows[0][2] ** 2 + self.arrows[0][3] ** 2 -( self.arrows[1][2] ** 2 + self.arrows[1][3] ** 2)) <=5:
            return -1
        minutes_theor = time[1] / 60 * 360
        hours_theor = (time[0] % 12) / 12 * 360 + time[1] /60 * 30
        self.error_rate = np.abs(minutes_theor - self.angles[1]) + np.abs(hours_theor - self.angles[0])
        return self.error_rate

        
    
    def find_time(self):
        minutes = np.floor(self.angles[1] / 360 * 60) % 60
        hours = np.floor(self.angles[0] / 360 * 12) % 12
        self.found_time = (hours,minutes)
    
    def find_error_rate(self,time):
        if np.abs(self.arrows[0][2] ** 2 + self.arrows[0][3] ** 2 -( self.arrows[1][2] ** 2 + self.arrows[1][3] ** 2)) <=5:
            return -1
        minutes_theor = time[1] / 60 * 360
        hours_theor = (time[0] % 12) / 12 * 360 + time[1] /60 * 30
        self.error_rate = np.abs(minutes_theor - self.angles[1]) + np.abs(hours_theor - self.angles[0])
        return self.error_rate

        