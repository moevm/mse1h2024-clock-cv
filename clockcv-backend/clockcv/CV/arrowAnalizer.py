import cv2
import numpy as np

class ArrowAnalizer():
    def __init__(self):
        self.arrows = []
        self.clean_image = None
        self.found_time = None
        self.arrow_contour = []
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
        if self.print_center(circle) == -1:
            return 100
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
            if hierarchy[0, i, -1] == 0 and contours1[i][2] > 10:
                self.arrow_contour.append(contours1[i])
            elif hierarchy[0,i,-1] != -1:
                fill = np.full((contours1[i][3], contours1[i][2]), 255)
                self.clean_image[contours1[i][1] : contours1[i][1]  + contours1[i][3],contours1[i][0] : contours1[i][0]  + contours1[i][2]] = fill
        minimum = 10000000
        if len(self.arrow_contour) == 2:
            return 1
        if len(self.arrow_contour) == 0: 
           return -1 
        print(self.arrow_contour)
        for c in self.arrow_contour:
            for i in range(c[1], c[1] + c[3]):
                for j in range(c[0], c[0] + c[2]):
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
            #print(dot)
            if hierarchy[0, i, -1] == 0 and dot[2] > 10:
                self.arrows.append(dot)
                #cv2.rectangle(self.clean_image,(dot[0],dot[1]),(dot[0]+dot[2],dot[1]+dot[3]),(0,255,0),2)
        #cv2.circle(self.clean_image,(self.center[1],self.center[0]), 10 ,(0,255,0), -1)
        if len(self.arrows) == 1:
            self.check_two_arrows()
    
    def create_little_arrow(self,i,j, num):
        if i > self.arrows[0][num]:
            j = int((i - self.arrows[0][num]) / 2)
            i = self.arrows[0][num] + j
        else:
            j = int(self.arrows[0][num + 2] / 2)
        return i,j
    
    def check_two_arrows(self):
        minimum = 1000000
        x,y,w,h = 0,0,0,0
        for i in ([self.arrows[0][1], self.arrows[0][1] + self.arrows[0][3]]):
            for j in ([self.arrows[0][0], self.arrows[0][0] + self.arrows[0][2]]):
                if abs(i - self.center[1]) + abs(j - self.center[0]) < minimum:
                    x,y = j,i
                    minimum = abs(i - self.center[1]) + abs(j - self.center[0])
        x,w = self.create_little_arrow(x, w, 0)
        y,h = self.create_little_arrow(y, h, 1)
        self.arrows.append((x,y,w,h))
        

                
    def find_edge_dots(self,circle):
        #print(self.arrows)
        if self.arrows[0][2] ** 2 + self.arrows[0][3] ** 2 > self.arrows[1][2] ** 2 + self.arrows[1][3] ** 2:
            self.arrows[0], self.arrows[1] = self.arrows[1], self.arrows[0]
        for ar in self.arrows:
            maxi = 0
            x,y = 0,0
            for i in range(ar[1],ar[1] + ar[3]):
                for j in range(ar[0],ar[0] + ar[2]):
                    if (circle[0] - j) ** 2 + (circle[1] - i) ** 2 > maxi and self.clean_image[i,j] <= 128:
                        maxi = (circle[0] - j) ** 2 + (circle[1] - i) ** 2
                        x,y =  j,i
            self.dots.append((x,y))
            cv2.circle(self.clean_image,(x,y), 10 ,(0,255,0), -1)
        #cv2.imshow('',self.clean_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

           
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
        #print(self.angles)
        minutes = np.floor(self.angles[1] / 360 * 60) % 60
        hours = np.floor(self.angles[0] / 360 * 12) % 12
        self.found_time = (hours,minutes)
        #print(self.found_time)
    
    def find_error_rate(self,time):
        if np.abs(self.arrows[0][2] ** 2 + self.arrows[0][3] ** 2 -( self.arrows[1][2] ** 2 + self.arrows[1][3] ** 2)) <=5:
            return -1
        minutes_theor = time[1] / 60 * 360
        hours_theor = (time[0] % 12) / 12 * 360 + time[1] /60 * 30
        #print(hours_theor,minutes_theor)
        self.error_rate = min(np.abs(minutes_theor - self.angles[1]) % 360 + np.abs(hours_theor - self.angles[0]) % 360,np.abs(minutes_theor - (self.angles[1] - 360)) % 360 + np.abs(hours_theor - self.angles[0]) % 360 )
        #print(self.error_rate)
        return self.error_rate
    