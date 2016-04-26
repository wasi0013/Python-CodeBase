def com(am, yrs, fr, g):
    for x in range(yrs):
        am += int(am*fr) - g
    return am
def sim(am, yrs, fr, g):
    cum = 0
    for x in range(yrs):
        cum += int(am*fr)
        am -= g
    return am + cum
def main():
    c = (sim, com)
    for x in range(int(input())):
        am = int(input())
        yrs = int(input())
        ams = []
        for x in range(int(input())):
            i,fr,g = input().split()
            ams.append(c[int(i)](am, yrs,float(fr), int(g)))
        print (max(ams))
    return 0
if __name__ == '__main__':main()
