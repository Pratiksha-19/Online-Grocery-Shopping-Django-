from django.shortcuts import render
from django.core.files import File

# Create your views here.

def index(request):
	return render(request, "supermarket/top.html")

def disitems():
	with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/list.txt",'r') as f:
	
		lst=[]
		for line in f:
			x=line.split() 
		
			lst.append({"items" : x[0], "price" : x[1], "qty" : x[2]})
	context = {"name":lst}
	return context




def shoplist(request):

	context=disitems()	

	if request.method=='POST' and 'add' in request.POST:
		i= request.POST.get('item')
		q = request.POST.get('qty')
		item=str(i)
		qty=str(q)
		with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/cart.txt","a+") as f:
			x=item+"|"+qty+"|\n"
			f.write(x)
			f.close()

		with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/index.txt","a+") as fp:
			fp.write(item+"\n")
			f.close()


	if request.method=='POST' and 'delete' in request.POST:
		k = request.POST.get('item')
		key=str(k)
		item=[]
		#offset=[]
		value=""
		with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/index.txt","r") as fp:
			for line in fp:
				x=line.split("|")
				item.append(x[0])
			#offset.append(line[1])	

		if key not in item:
			value="not found"

		else:
			pos=item.index(key)
			with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/cart.txt","r") as f:
				data = f.readlines()
				x=data[pos]
				data[pos]="*"+x
			with open('C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/cart.txt', 'a') as file:
				file.writelines( data )

			with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/index.txt","r") as f:
				data = f.readlines()
				x=data[pos]
				data[pos]="*"+x
			with open('C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/index.txt', 'a') as file:
				file.writelines( data )
			value="deleted"



	return render(request, "supermarket/shoplist.html", context)


def cartitems(request):

	#it and qt are lists from cart file
	it=[]
	qt=[]

	with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/cart.txt",'r') as f:
		lst=[]
		for line in f:
			x=line.split('|') 
			t=x[0]
			if t[0]!='*':
				lst.append({"items" : x[0], "qty" : x[1]})
				
				it.append(x[0])
				qt.append(float(x[1]))
				#map(float, qt)

#i, q, p are lists for list file
	i=[]
	q=[]
	p=[]
	with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/list.txt",'r') as fp:
		for line in fp:
			y=line.split()
			i.append(y[0])
			p.append(float(y[1]))
			q.append(float(y[2]))
			#map(float, p)
			#map(float, q)

	#price for standard quantity is list to store the price of each item in the cart file
	price=[]
	#price1 is for the quantity mentioned by user
	price1=[]

	totp, gst, bill=0.0, 0.0, 0.0
	#totp is total price of all items, bill is gst+total price
	pos=-1
	for key in it:
		if key in i:
			pos=i.index(key)
			#Getting the price of items in cart
			price.append(p[pos])
		
	c=len(price)
	for i in range(0,c):
		var=price[i]*qt[i]
		price1.append(var)
		totp=totp+price1[i]
	

	gst=(totp*(5/100))
	bill=(totp+gst)

	lst1=[]
	lst1.append({"price":price1,"total":totp, "gst":gst, "bill":bill})

	context = {
			"name1":lst, "name2":lst1
	}
	return render(request, "supermarket/cartitems.html", context)


def proceed(request):
	return render(request, "supermarket/proceed.html")

def submit(request):
	c=0
	fname = request.POST.get('fname')
	lname = request.POST.get('lname')
	email = request.POST.get('email')
	pas = request.POST.get('pas')
	tele = request.POST.get('tele')
	date = request.POST.get('date')
	add1 = request.POST.get('add1')
	add2 = request.POST.get('add2')
	city = request.POST.get('city')
	zipp = request.POST.get('zipp')
	c=c+1
	d = {'count':c}
	t = str(c)+"|"+fname+"|"+lname+"|"+email+"|"+pas+"|"+str(tele)+"|"+date+"|"+add1+"|"+add2+"|"+city+"|"+str(zipp)+"| \n"
		
	with open("C:/Users/PRATIKSHA/Desktop/project/mysite/supermarket/templates/supermarket/details.txt",'a') as fl:
		fl.write(t)
		fl.close()
	return render(request, "supermarket/submit.html", {"data":d})