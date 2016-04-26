#!/usr/bin/
def main():
    try:
        buffersize = 500000
        string1=input("type name of the file to copy with extension\n-->")
        try:
            a,b= string1.split('.',1)
            string2= "copied_file." + b
        except ValueError as n:
            print("Oops!\n({}) ".format(n))
            
        
            
        fopen  = open(string1,"rb")
        fwrite = open(string2,"wb")
        buffer = fopen.read(buffersize)
        while len(buffer):
            fwrite.write(buffer)
            print(".", end = ' ')
            buffer = fopen.read(buffersize)
        print()
        print("file copied successfully")
    except IOError as e:
        print("\n({}) ".format(e))
        
    
if __name__=="__main__":main()
