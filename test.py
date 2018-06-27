import os
import sys
import mytest2
print("hello python")
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main():
    for i in range(len(sys.argv)):
        print(sys.argv[i])
    # print(sys.path)
    abspath = os.path.abspath(__file__)
    print(abspath) # /home/jiayongqiang/workspace/TestDemo/test.py
    dir1 = os.path.dirname(abspath)
    print(dir1) # /h/j/w/T
    # dir2 = os.path.dirname(dir1) # /h/j/w
    # print(dir2)
   #  print(BASEDIR)
    sys.path.insert(0,os.path.join(BASEDIR,"sdfa"))
   #  print(sys.path)


    pwd = os.path.dirname(os.path.realpath(__file__))

    t2_path = pwd+"../"
    sys.path.insert(0,t2_path)
    mytest2.my_print()
    print(__file__)
if __name__ == "__main__":
    main()
