from elementFinder import elementFinder,np,cv2,sys

'''
всего 14 контуров должно быть(2 стрелки и 12 чисел)
1 - ничего кроме круга нет
2 - есть какие-то числа или стрелки, но не все
3 - есть почти все числа, но они все вне круга
4 - есть почти все числа, большая часть чисел расположена внутри круга
5 - все числа есть внутри круга, но не все из них расположены в своих секторах - есть все числа
6 - все числа в своих секторах(1 - 2 могут быть рядом), но стрелок нет или есть какие-то лишние отметки на времени(обведено время в круг)
7 - стрелки есть, но они показывают совершенно неправильное время (> 2 секторов погрешность)
8 - время почти верное, но погрешность двух стрелок в сумме от 1 до 2 секторов
9 - время почти верное, но погрешность стрелок в сумме от 0.5 до 1 сектора
10 - время верное, погрешность до 0.5 сектора

1. Посчитать сколько чисел есть(2-3 балла)
2. Определить, все ли числа находятся внутри круга(4 балла) 
3. Посчитать сколько чисел в нужных секторах(5 баллов)
4. Похожи ли стрелки в общих чертах на стрелки( 6-7 баллов)
5. Время, которое показывают стрелки(8-10баллов)
'''
class CVSolver():
    def __init__(self,finder):
        self.finder = finder
        self.result = 0
        self.current_time = (21,44)
        self.angles = [(15,45),(45,75),(75,105),(105,135),(135,165),(165,195),(195,225),(225,255),(255,285),(285,315),(315,345),(345,375)] # углы границы для расположения чисел циферблата
        
    def start(self):
        self.finder.find_circle()
        self.finder.find_contours()
        self.draw_sections()
        self.draw_circle()
        # self.draw_contours()
        self.find_result()
        self.draw_number()
        cv2.imshow('cldt', self.finder.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #нахождение чисел на картинке    
    def first_test(self):
        self.finder.find_numbers()
        # if len(self.finder.numbers) > 0:
        #     if len(self.finder.numbers) != 12:
        #         self.result = 2
        #     else:
        #         self.result = 3
        # else:
        #     self.result = 1
        
    #нахождение чисел внутри круга, добавляет 1 к result
    def second_test(self):
        pass
    
    #определение местоположения чисел внутри круга(сектора)
    def third_test(self):
        pass
   
    #определение погрешности  времени показания стрелок
    def fourth_test(self):
        pass
    
    def find_result(self):
        self.first_test()
        # if self.result > 1:
        #     self.second_test()
            
        # else: 
        #     return
    
    def draw_sections(self):
        lines = []
        for a in self.angles:
            lines.append([self.finder.circle[0] + self.finder.circle[2] * np.sin(np.deg2rad(a[0])),  self.finder.circle[1] -  self.finder.circle[2] * np.cos(np.deg2rad(a[0]))])
        lines = [[int(np.around(dot)) for dot in line] for line in lines]
        for line in lines:
            cv2.line(self.finder.image,(self.finder.circle[0],self.finder.circle[1]),(line[0],line[1]),(0,0,255),1)
    
    def draw_contours(self):
        for dot in self.finder.contours:
            # if
            cv2.rectangle(self.finder.image,(dot[0],dot[1]),(dot[0]+dot[2],dot[1]+dot[3]),(0,255,0),2)
    
    def draw_number(self):
        for dot in self.finder.numbers:
            if dot:
                cv2.rectangle(self.finder.image,(dot[0],dot[1]),(dot[0]+dot[2],dot[1]+dot[3]),(255,0,0),2)
            
    def draw_circle(self):
        cv2.circle(self.finder.image,(self.finder.circle[0],self.finder.circle[1]), self.finder.circle[2],(0,255,0),3)