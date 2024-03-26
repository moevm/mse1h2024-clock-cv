import os
from .solver import CVSolver,cv2,elementFinder,np

async def cv_image_recognise(file):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    width = image.shape[1]
    height = image.shape[0]
    if width!=1190 or height!=699:
        return (None, None, f"Изображение неправильных размеров, требуется {1190}x{699}, полученно{width}x{height}")

    prototype = [[] for _ in range(10)]
    for i in range(len(prototype)):
        file_list = os.listdir(f"storage/templates/{i}")
        for name in file_list:
            prototype[i].append(cv2.cvtColor(cv2.imread(f"storage/templates/{i}/{name}"), cv2.COLOR_BGR2GRAY))
    solver = CVSolver(elementFinder(image, prototype))
    return solver.start()