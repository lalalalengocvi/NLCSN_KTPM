from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory, widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.

class Register(SuccessMessageMixin, generic.CreateView):
    form_class = UserCreationForm
    success_message = "Đăng kí thành công, bây giờ bạn có thể đăng nhập."
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

# def start(request):
#     return render(request, 'intro.html')

@login_required
def profile(req):
    UserEditForm = modelform_factory(
        get_user_model(), fields=('first_name', 'last_name', 'username'))
    form = UserEditForm(instance=req.user)
    if req.method == "POST":
        form = UserEditForm(instance=req.user, data=req.POST)
        if form.is_valid():
            form.save()
    return render(req, 'registration/profile.html', {'form': form})



# @login_required(login_url='adminlogin')
# def admin_dashboard_view(request):
#     # for cards on dashboard
#     customercount=models.Customer.objects.all().count()
#     productcount=models.Product.objects.all().count()
#     ordercount=models.Orders.objects.all().count()

#     # for recent order tables
#     orders=models.Orders.objects.all()
#     ordered_products=[]
#     ordered_bys=[]
#     for order in orders:
#         ordered_product=models.Product.objects.all().filter(id=order.product.id)
#         ordered_by=models.Customer.objects.all().filter(id = order.customer.id)
#         ordered_products.append(ordered_product)
#         ordered_bys.append(ordered_by)

#     mydict={
#     'customercount':customercount,
#     'productcount':productcount,
#     'ordercount':ordercount,
#     'data':zip(ordered_products,ordered_bys,orders),
#     }
#     return render(request,'ecom/admin_dashboard.html',context=mydict)


# # admin view customer table
# @login_required(login_url='adminlogin')
# def view_customer_view(request):
#     customers=models.Customer.objects.all()
#     return render(request,'ecom/view_customer.html',{'customers':customers})

# # admin delete customer
# @login_required(login_url='adminlogin')
# def delete_customer_view(request,pk):
#     customer=models.Customer.objects.get(id=pk)
#     user=models.User.objects.get(id=customer.user_id)
#     user.delete()
#     customer.delete()
#     return redirect('view-customer')


# @login_required(login_url='adminlogin')
# def update_customer_view(request,pk):
#     customer=models.Customer.objects.get(id=pk)
#     user=models.User.objects.get(id=customer.user_id)
#     userForm=forms.CustomerUserForm(instance=user)
#     customerForm=forms.CustomerForm(request.FILES,instance=customer)
#     mydict={'userForm':userForm,'customerForm':customerForm}
#     if request.method=='POST':
#         userForm=forms.CustomerUserForm(request.POST,instance=user)
#         customerForm=forms.CustomerForm(request.POST,instance=customer)
#         if userForm.is_valid() and customerForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             customerForm.save()
#             return redirect('view-customer')
#     return render(request,'ecom/admin_update_customer.html',context=mydict)

# # admin view the product
# @login_required(login_url='adminlogin')
# def admin_products_view(request):
#     products=models.Product.objects.all()
#     return render(request,'ecom/admin_products.html',{'products':products})


# # admin add product by clicking on floating button
# @login_required(login_url='adminlogin')
# def admin_add_product_view(request):
#     productForm=forms.ProductForm()
#     if request.method=='POST':
#         productForm=forms.ProductForm(request.POST, request.FILES)
#         if productForm.is_valid():
#             productForm.save()
#         return HttpResponseRedirect('admin-products')
#     return render(request,'ecom/admin_add_products.html',{'productForm':productForm})


# @login_required(login_url='adminlogin')
# def delete_product_view(request,pk):
#     product=models.Product.objects.get(id=pk)
#     product.delete()
#     return redirect('admin-products')


# @login_required(login_url='adminlogin')
# def update_product_view(request,pk):
#     product=models.Product.objects.get(id=pk)
#     productForm=forms.ProductForm(instance=product)
#     if request.method=='POST':
#         productForm=forms.ProductForm(request.POST,request.FILES,instance=product)
#         if productForm.is_valid():
#             productForm.save()
#             return redirect('admin-products')
#     return render(request,'ecom/admin_update_product.html',{'productForm':productForm})


# @login_required(login_url='adminlogin')
# def admin_view_booking_view(request):
#     orders=models.Orders.objects.all()
#     ordered_products=[]
#     ordered_bys=[]
#     for order in orders:
#         ordered_product=models.Product.objects.all().filter(id=order.product.id)
#         ordered_by=models.Customer.objects.all().filter(id = order.customer.id)
#         ordered_products.append(ordered_product)
#         ordered_bys.append(ordered_by)
#     return render(request,'ecom/admin_view_booking.html',{'data':zip(ordered_products,ordered_bys,orders)})


# @login_required(login_url='adminlogin')
# def delete_order_view(request,pk):
#     order=models.Orders.objects.get(id=pk)
#     order.delete()
#     return redirect('admin-view-booking')

# # for changing status of order (pending,delivered...)
# @login_required(login_url='adminlogin')
# def update_order_view(request,pk):
#     order=models.Orders.objects.get(id=pk)
#     orderForm=forms.OrderForm(instance=order)
#     if request.method=='POST':
#         orderForm=forms.OrderForm(request.POST,instance=order)
#         if orderForm.is_valid():
#             orderForm.save()
#             return redirect('admin-view-booking')
#     return render(request,'ecom/update_order.html',{'orderForm':orderForm})

