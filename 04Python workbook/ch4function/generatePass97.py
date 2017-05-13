from CheckPassword96 import checkWhetherGoodPass
from  generateRandomPass94 import randomPasword

count = 0
while  True:
	tempPass = randomPasword()
	if checkWhetherGoodPass(tempPass):
		break;
	else:
		tempPass = randomPasword()
		count += 1
print("after ",count ,"times",tempPass)