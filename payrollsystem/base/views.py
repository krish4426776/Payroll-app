from django.shortcuts import render , redirect
from base.models import CustomUser , Bill , Buyer ,Seller
from .forms import RegisterForm , BillForm , EditForm

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView 
from django.db.models import Sum

from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
@login_required(login_url=  'login')
def Home(request):
    user = CustomUser.objects.all()
    b = Bill.objects.all()
    fulfilled_bills = Bill.objects.filter(payment_status='fulfilled')
    total_earning = fulfilled_bills.aggregate(total=Sum('amount'))['total']

    
    context = {'user':user , 'bills':b , 'total':total_earning }
    return render(request , 'base/home.html' , context)


def CreateNewUser(request):
    if not request.user.is_superuser:
         return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    form = RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            user_type = form.cleaned_data['user_type']
            if user_type == 'seller':
                Seller.objects.create(user=user)
            elif user_type == 'buyer':
                Buyer.objects.create(user=user)
            
        return redirect('home')
    context = {'form':form}
    return render(request , 'base/registration.html' , context)
@login_required(login_url=  'login')
def AddBillForPayment(request):
    if request.user.user_type != 'seller':
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    form  = BillForm()
    if request.method=='POST':
        form = BillForm(request.POST)
        if form.is_valid():
           sell= form.save(commit=False)
           sell.seller = request.user.seller
           sell.save()
        return redirect('home')
    context = {'form':form}
    return render(request , 'base/add_bill.html' , context)

def DeleteUser(request , pk):
    if not request.user.is_superuser:
         return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    user = CustomUser.objects.get(id=pk)
    if request.method=='POST':
        user.delete()
        return redirect('home')
    context = {'obj':user}
    return render(request , 'base/delete.html' , context)

def Edituser(request , pk):
    if not request.user.is_superuser:
         return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    user = CustomUser.objects.get(id=pk)
    form = EditForm(instance=user)
    if request.method=='POST':
        form=EditForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')
    context={'form': form}
    return render (request , 'base/edit.html' , context )

def Payment(request):
    if request.user.user_type != 'buyer':
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    bill = Bill.objects.all()
   
            
    context = {'bills':bill}
    return render (request , 'base/payment.html' , context)

def pay(request , pk):
    if request.user.user_type != 'buyer':
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    bill = Bill.objects.get(id=pk)
    if request.method == 'POST':
            bill.payment_status = 'fulfilled'
            bill.save()
            return redirect('home')
    context = {'bills':bill}
    return render (request , 'base/paymentpage.html' , context )












