import cv2
import numpy as np
import sys
import math
'''
из финдера будет подгружаться инфа о контурах,        сделано
очистить изображение от цифер                         сделано
найти контур стрелок, затем нужно пройтись по контуру стрелок по всему и найти точку, 
которая ближе всех к центру окружности, закрасить ее белым кругом, снова найти контуры стрелок раздельно,           сделано
затем начать анализ
'''
class ArrowAnalizer():
    def __init__(self):
        self.arrows = []
        self.clean_image = None
        self.found_time = None
        self.arrow_contour = None
        self.center = [0,0]
            
    def clear_image(self,gray,numbers):
        self.clean_image = gray
        for num in numbers:
            fill = np.full((num[3], num[2]), 255)
            self.clean_image[num[1]: num[1] + num[3], num[0] : num[0] + num[2]] = fill
    
    def start(self,gray,numbers,circle,circle_contour):
        self.clear_image(gray,numbers)
        self.print_center(circle)
        self.find_arrows()
        self.find_time(circle,circle_contour)
    
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
                if np.abs(i - circle[1]) + np.abs(j - circle[0]) < minimum:
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
        cv2.imshow('cldt', self.clean_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def find_time(self,circle,circle_contour):
        '''
        1. определить краевые точки
        
        
        
        2. определить, какая стрелка часовая какая минутная
        
        какая краевая точка ближе к контуру круга, та минутная
        
        3. анализ времени
        
        
        '''
        
        