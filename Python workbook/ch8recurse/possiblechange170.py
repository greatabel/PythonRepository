#http://www.dotnetperls.com/recursion-python
coins = []
amounts = [1, 5, 10, 25, 50]

def display(coins, amounts):
    # Display our goins sorted by amount.
    for amount in amounts:
    	count = coins.count(amount)
    	print(amount , ":", count)
    print("")

def change(coins, amounts, highest, sum, goal):
    # See if we are done.
    if sum == goal:
    	display(coins, amounts)
    	return 

    if sum > goal:
    	return

    for value in amounts:
    	if value >= highest:
    		copy = coins[:]
    		copy.append(value)
    		change(copy,amounts,value,sum+value,goal)

# 输入例子：10003
def main():

	# Begin.
	change(coins, amounts, 0, 0, 51)

if __name__ == "__main__":
    main()
