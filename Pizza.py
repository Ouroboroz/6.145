toppings = ['bacon','bacon','anchovies','pepperoni','mushroom','ham']
size = 'large'
if(size == 'large'):
	price = 18
elif(size == 'medium'):
	price = 16
else: 
	price = 14

price *= (1.1)**len(toppings)

if('bacon' in toppings or 'anchovies' in toppings):
	price += 5

print(price)