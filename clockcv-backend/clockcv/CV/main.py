import os
from solver import CVSolver,cv2,elementFinder

if __name__ == '__main__':
    image = cv2.imread('test_image/12_b.png')
    prototype = [[] for _ in range(10)]
    for i in range(len(prototype)):
        file_list = os.listdir("templates/"+ str(i))
        for name in file_list:
            prototype[i].append(cv2.cvtColor(cv2.imread("templates/" + str(i) + "/" + name), cv2.COLOR_BGR2GRAY))
    solver = CVSolver(elementFinder(image,prototype))
    solver.start()