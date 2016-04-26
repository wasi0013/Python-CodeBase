class Hello():
    def __init__(self,text="Hello_world"):
        self.text= text
    def fireWorks(self):
        text= input("Type?\n-->")
        return text
def main():
    fly=Hello()
    egg=fly.fireWorks()
    print(egg)
    pause_exits =input("Press any key to quit")
        
if __name__ == "__main__": main()
