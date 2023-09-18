from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):

    return HttpResponse('Hello from Homepage of Productapp')

def add_product(request):
    print("Method Name:",request.method)
    if request.method=="GET":
       print("In if GET section")
       return render(request,'product/store_product.html')
    else:
        print("In else POST section")
        return HttpResponse("In POST Section")