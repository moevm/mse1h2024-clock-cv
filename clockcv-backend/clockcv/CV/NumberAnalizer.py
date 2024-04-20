import cv2
import numpy as np

class NumberAnalizer():
    def __init__(self, prototype):
        self.prototype = prototype 
        self.numbers =  [[] for _ in range(10)]
        
    def find_numbers(self, contours, numbers, image, hierarchy):
        threshold = 0.7
        for j in range(len(contours)):
            c = contours[j]
            h = hierarchy[0][j]
            if c[2] <=55 and c[3] <=55 and h[3]==0 and c[2] >=5 and c[3] >=5:
                temp_image = image[c[1] : c[1]+c[3], c[0]:c[0]+c[2]]
                temp_image = self.resize_image(temp_image)
                list_of_matches =  [[] for _ in range(10)]
                for i in range(len(self.prototype)):
                    for p in self.prototype[i]:
                        result = cv2.matchTemplate(temp_image, p, cv2.TM_CCOEFF_NORMED)
                        max_res = np.max(result)
                        if max_res > threshold:
                            list_of_matches[i].append(max_res)
                found_number = self.find_max_match_index(list_of_matches)
                if found_number!= None:
                    self.numbers[found_number].append(c)
        self.find_two_digit_number(numbers)
        for i in range (len(self.numbers)):
            if len(self.numbers[i]) > 0:
                numbers[i-1] = self.numbers[i].pop(0)
        
    def resize_image(self,image):
        image = cv2.resize(image, (15, 21))
        image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value= (255, 255, 255))
        return image

    def find_max_match_index(self, arr):
        max_number = float('-inf')
        current_max = float('-inf')
        max_index = None
        for i in range(len(arr)):
            if len(arr[i])!=0:
                current_max = max(arr[i])
            if current_max > max_number:
                max_number = current_max
                max_index = i
        return max_index
    
    def calculate_distance(self, center1, center2):
        distance = ((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2) ** 0.5
        return distance
    
    def find_center(self, coord):
        x, y, w, h = coord
        center = (x + w // 2, y + h // 2)
        return center
    
    def find_two_digit_number(self, numbers):
        remove_list = []
        for i in range(len(self.numbers)):
            for k in range(i, len(self.numbers)):
                start = 0 
                for j in range(len(self.numbers[i])):
                    if i == k: 
                        start = j
                    for l in range(start, len(self.numbers[k])):
                        coord_1 = self.numbers[i][j]
                        coord_2 = self.numbers[k][l]
                        if coord_1 != coord_2:
                            dist = self.calculate_distance(self.find_center(coord_1), self.find_center(coord_2))
                            avg_diagonal = (((coord_1[2] + coord_2[2]) / 2)**2 + ((coord_1[3] + coord_2[3]) / 2)**2) ** 0.5
                            if dist < avg_diagonal:
                                new_param = self.find_new_pair_parameters(coord_1,coord_2)
                                remove_list.append((i,coord_1))
                                remove_list.append((k,coord_2))
                                index = 0
                                if i==1:
                                    index = int(str(i)+str(k)) - 1
                                elif k==1:
                                    index = int(str(k)+str(i)) - 1
                                if index > 8 and index < 12 :
                                    numbers[index] = new_param
        for r in remove_list:
            self.numbers[r[0]].remove(r[1])

    def find_new_pair_parameters(self, coord_1, coord_2):
        new_x = min (coord_1[0], coord_2[0])
        new_y = min (coord_1[1], coord_2[1])
        new_w = max (coord_1[0] + coord_1[2], coord_2[0] + coord_2[2]) - new_x
        new_h = max (coord_1[1] + coord_1[3], coord_2[1] + coord_2[3]) - new_y
        return (new_x, new_y, new_w, new_h)
    
    def get_angle(self, numbers, circle):
        A = np.array([circle[0], circle[1] - circle[2]])
        B = np.array([circle[0], circle[1]])
        angle = [None for _ in range(12)]
        for i in range(len(numbers)):
            if numbers[i]:
                C = np.array(self.find_center(numbers[i]))
                BA = A - B
                BC = C - B
                angle_rad = np.arctan2(BC[1], BC[0]) - np.arctan2(BA[1], BA[0])
                angle_deg = np.degrees(angle_rad)
                if angle_deg < 15:
                    angle_deg += 360
                angle[i] = angle_deg
        return angle   