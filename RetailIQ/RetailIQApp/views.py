from django.shortcuts import render
from django.views import View

# Create your views here.

# class LoginPage(View):
#     def get(self,request):
#         return render(request,'Login.html')
#     def post(self,request):
#         username1=request.POST['username']
#         password1=request.POST['password']
#         print(username1)
#         prit(password1) 

#         login_obj=LoginTable.objects.get(username=username1,password=password1)
#         print("$$$$$$$$$$$$$$$$$$$",login_ibj)
#         request.session['userid']=login_obj.id
#         print(request.session['userid'])

#         if login_obj.udertype=="shop":
#             return HttpResponse(''')




# //////////////////////////////////////////// ADMIN /////////////////////////////////////
class BlockOrUnblockShops(View):
    def get(self,request):
        return render(request,'admin/BlockOrUnblockShops.html')

class ViewAndVerifyShops(View):
    def get(self,request):
        return render(request,'admin/ViewAndVerifyShops.html')

class ViewComplaintsAndReply(View):
    def get(self,request):
        return render(request,'admin/ViewComplaintsAndReply.html')
    
class ViewRatingAndFeedback(View):
    def get(self,request):
        return render(request,'admin/ViewRatingAndFeedback.html')   
  
    #///////////////////////////// SHOP //////////////////////////////////

class AddProducts(View):
    def get(self,request):
        return render(request,'shop/AddProducts.html')   

class AddStaff(View):
    def get(self,request):
        return render(request,'shop/AddStaff.html')   

class ManageDiscountaff(View):
    def get(self,request):
        return render(request,'shop/ManageDiscountaff.html') 

class ManageNotifications(View):
    def get(self,request):
        return render(request,'shop/ManageNotifications.html') 

class ManageOffers(View):
    def get(self,request):
        return render(request,'shop/ManageOffers.html') 

class ManageProducts(View):
    def get(self,request):
        return render(request,'shop/ManageProducts.html') 

class ManageStaff(View):
    def get(self,request):
        return render(request,'shop/ManageStaff.html') 

class Register(View):
    def get(self,request):
        return render(request,'shop/Register.html') 

class ViewCustomers(View):
    def get(self,request):
        return render(request,'shop/ViewCustomers.html') 

class ViewOrders(View):
    def get(self,request):
        return render(request,'shop/ViewOrders.html') 

class ViewSales(View):
    def get(self,request):
        return render(request,'shop/ViewSales.html') 

class ViewStockandUpdateStock(View):
    def get(self,request):
        return render(request,'shop/ViewStockandUpdateStock.html') 

#////////////////////////////// STAFF /////////////////////////////////////

class OrdersAndBill(View):
    def get(self,request):
        return render(request,'staff/OrdersAndBill.html') 
    
class ViewDiscount(View):
    def get(self,request):
        return render(request,'staff/ViewDiscount.html')
    
class ViewLowStock(View):
    def get(self,request):
        return render(request,'staff/ViewLowStock.html') 

class ViewNotification(View):
    def get(self,request):
        return render(request,'staff/ViewNotificationk.html') 

class ViewOffers(View):
    def get(self,request):
        return render(request,'staff/ViewOffers.html') 

class ViewOrders(View):
    def get(self,request):
        return render(request,'staff/ViewOrders.html') 

class ViewProducts(View):
    def get(self,request):
        return render(request,'staff/ViewProducts.html') 
    






  
  