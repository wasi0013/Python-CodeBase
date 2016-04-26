
import itertools
class Main:
    def __init__( self ):
        iterable = self.__standard( )
        self.__solution( iterable )
    def __solution( self, iterable ):
        number=0
        count,div=map(int,next(iterable).split())
        print(sum(1 for i in iterable if int(i)%div==0))

    def __standard( self ):
        from sys import stdin,stdout
        try:
            while True:
                yield stdin.readline()
        except :pass

if __name__ == "__main__":
    Main( )
