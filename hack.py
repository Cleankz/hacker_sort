import random
import time
def MisterRobot( N, data):
    flag = True
    start_time = time.time()
    while flag:
        rand = random.randint(0,N-3)
        array = data[rand:rand+3]
        for i in range(2):
            if array == sorted(array):
                break
            else:
                array.append(array.pop(0))
        data[rand:rand+3] = array[:3]
        if data == sorted(data) and time.time() - start_time <= 1:
            return True
        elif data != sorted(data) and time.time() - start_time > 1:
            return False