import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished.")


def main():
    j_list = []

    for i in range(1, 6):
        temp = threading.Thread(target=do_job, args=(i,))
        temp.start()
        j_list.append(temp)

    for ele in j_list:
        ele.join()


main()
