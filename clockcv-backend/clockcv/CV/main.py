from solver import CVSolver,cv2,elementFinder

if __name__ == '__main__':
    image = cv2.imread('./oprpo/images/prototype.png')
    prototype = []
    prototype.append(cv2.imread('./oprpo/images/temp1.png'))
    for i in range(len(prototype)):
        prototype[i] = cv2.cvtColor(prototype[i], cv2.COLOR_BGR2GRAY)
    solver = CVSolver(elementFinder(image,prototype))
    solver.start()