#第一题
num1,num2 = eval(input('请输入身高体重，用逗号隔开'))
BMI = num2 / (num1**2)
if BMI < 18.5:
	print('BMI={:.1f}体重过轻'.format(BMI))
elif 18.5 < BMI <=24:
	print('BMI={:.1f}正常'.format(BMI))
elif 24 < BMI <=27:
	print('BMI={:.1f}过重'.format(BMI))
elif 27 < BMI <= 32:
	print('BMI={:.1f}非常肥胖'.format(BMI))
#第二题
num = eval(input())
s=0
for i in range(num+1):
	s += i
print('{}的前n项和是{}'.format(num,s))
#第三题
pay = eval(input())
if 50 <= pay <= 100:
	cost = pay*0.9
	zk = 10
	print('购买价格是{}折扣为{}%最终结果为{}'.format(pay,zk,cost))
elif pay > 100:
	cost = pay*0.8
	zk = 20
	print('购买价格是{}折扣为{}%最终结果为{}'.format(pay,zk,cost))
