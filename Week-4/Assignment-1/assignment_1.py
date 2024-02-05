import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished.")


def main():
    j_list = []
    j1 = threading.Thread(target=do_job, args=(1,))
    j_list.append(j1)
    j2 = threading.Thread(target=do_job, args=(2,))
    j_list.append(j2)
    j3 = threading.Thread(target=do_job, args=(3,))
    j_list.append(j3)
    j4 = threading.Thread(target=do_job, args=(4,))
    j_list.append(j4)
    j5 = threading.Thread(target=do_job, args=(5,))
    j_list.append(j5)

    for ele in j_list:
        ele.start()

    for ele in j_list:
        ele.join()


main()
