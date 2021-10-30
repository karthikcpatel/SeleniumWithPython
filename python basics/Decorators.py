#Passing a function as an argument

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec()

@dec1
def who_is_kartik():
    print("Kartik is a good boy")

who_is_kartik()