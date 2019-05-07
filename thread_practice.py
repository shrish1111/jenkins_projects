import time
import threading

def calc_square(num):
    print("calculate square of numbers")
    for n in num:
        time.sleep(0.2)
        print("square is: ",'\n',n*n)


def calc_cube(num):
    print("calculate cube of numbers")
    for n in num:
        time.sleep(0.2)
        print('cube is: ',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in :",time.time()-t)
