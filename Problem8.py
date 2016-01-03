import sys

def get_nums(x,i,k):
	return str(x)[i:k]

def product_of(slice):
	num = 1
	for x in slice:
		try: num *= int(x)
		except ValueError:
			set_trace()
	return num

def find_greatest_product(x,n):
	greatest_product = 0
	i = 0
	while i+n <= len(str(x)):
		if product_of(get_nums(x,i,i+n)) > greatest_product:
			greatest_product = product_of(get_nums(x,i,i+n))
		i += 1 
	return greatest_product

if __name__ == "__main__":
	x = open("num.txt").read().replace('\n', '')
	print find_greatest_product(x,int(sys.argv[1]))
