#creating a tuple
product = (10011,"laptop",35000,"Dell",10011,"Laptop",35000,"Dell");
print(product)
print(type(product));
#product[0]=2003;
print(product[0]);
for index,i in enumerate(product):
    print(index,i)

#accessing tuple
print(product)
print("start and end index:",product[0:4])
print("only start index:",product[1:])
print("only end index:",product[:6])
print("reverse order:",product[-1:])

#tuple unpacking
product = (10011,"laptop",36000,"Dell")
pro_id,name,price,brand = product;
print("product id:",pro_id)
print("Product name:",name)
print("Price:",price)
print("brand:",brand)

for i in product:
    print(i)

for index,i in enumerate(product):
    print(index,i)

print("laptop" in product)
print("mobile" in product)   

repeat_tuple = ("*") * 100
print(repeat_tuple)

product_id = (10011,10022,10033,10044,10055)
product_name=("Laptop","mobiles","TV","AC","table")
product_tuple = product_id + product_name
print(product_tuple)

repeat_tuple = ("*") * 100
print(repeat_tuple)