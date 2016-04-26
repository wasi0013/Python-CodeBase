from sys import stdin, stdout
import decimal

def main():
   numOfTimes = int(stdin.readline())
   for i in range(numOfTimes):
       
      d = decimal.toDecimal(int(stdin.readline()))
      print(d.sqrt())

if __name__ == '__main__':
   main()
