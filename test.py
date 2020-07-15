import time
from playsound import playsound




def sleep_test(time):
    print("Printed immediately.")
    time.sleep(time)
    playsound('test_cut_music.mp3')
    print("Song played after {} seconds.".format(time))

    

def test_module(i):
    print(i)


def main():

    func = test_module
    func("hello")
    sleep_test(10)
    # print(func("hello"))


if __name__== "__main__":
  main()