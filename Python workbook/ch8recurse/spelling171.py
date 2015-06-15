#测试数据
simbols = ['Ai','Bi','Ci']

def Checking(s):
    # Display our goins sorted by amount.
    for item in simbols:
        if s == item or s == "" or s in simbols:
            return True
        elif s.startswith(item):
            
            s = s.replace(item, "")
            print('item=',item,'here',s)
            return Checking(s)
        else:
            return False




# 输入例子：10003
def main():

	# Begin.
    myinput = input("Enter a number:")
    # print(myinput)
    result = Checking(myinput)
    print("%s" %result)    

if __name__ == "__main__":
    main()
