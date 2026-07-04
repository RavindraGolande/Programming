import threading
import time

# 2+4+6+8 = 20
def SumEven(No):
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even : ", Sum)

# 1+3+5+7+9 = 25
def SumOdd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd : ", Sum)


def main():
    start_time = time.perf_counter()

    T1 = threading.Thread(target=SumEven, args=(10,))
    T2 = threading.Thread(target=SumOdd, args=(10,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4}")

if __name__ == "__main__":
    main()