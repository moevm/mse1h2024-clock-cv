import os
from .solver import CVSolver, cv2, elementFinder

def non_async_startup(filename,time):
    image = cv2.imread(filename)
    prototype = [[] for _ in range(10)]
    for i in range(len(prototype)):
        file_list = os.listdir(f"templates/{i}")
        for name in file_list:
            prototype[i].append(cv2.cvtColor(cv2.imread(f"templates/{i}/{name}"), cv2.COLOR_BGR2GRAY))
    solver = CVSolver(elementFinder(image, prototype),time)
    return solver.start()
    

def test_cv():
    assert non_async_startup('test_image/1.png', (9,30))[1] == 1
    assert non_async_startup('test_image/2.png', (9,30))[1] == 2
    assert non_async_startup('test_image/3.png', (9,30))[1] == 3
    assert non_async_startup('test_image/4.png', (9,30))[1] == 4
    assert non_async_startup('test_image/5.png', (9,30))[1] == 5
    assert non_async_startup('test_image/6.png', (9,30))[1] == 6
    assert non_async_startup('test_image/7.png', (9,30))[1] == 7
    assert non_async_startup('test_image/8.png', (9,30))[1] == 8
    assert non_async_startup('test_image/9.png', (9,30))[1] == 9
    assert non_async_startup('test_image/10.png', (9,30))[1] == 10
