#activity2
s1 = {1 , 2 , 3}
s2 = { "b" , "c" , "a"}
s3 = list(zip(s1 , s2))
print(s3)

list1 = [ 10 , 30 , 40]
list2 = [ 100 , 600 , 800]
for x,y in zip(list1 , list2[::-1]):
    print(x , y)

stock = [ "reliance" , "infosys" , "tesla"]
prices = [ 1234 , 4567 , 7890]
new_dict = {stocks: prices for stocks , prices in zip(stock , prices)}
print("{}" . format(new_dict))