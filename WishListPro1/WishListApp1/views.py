from django.shortcuts import render,redirect
from .forms import WishListFrom,WishListDelForm
from.models import WishData
from django.http.response import HttpResponse
import datetime as dt
time=dt.datetime.now()
def home(request):
    return render(request,'WishList_home.html')
def WishListview(request):
    if request.method=='POST':
        form=WishListFrom(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            wishDatetobuy = form.cleaned_data.get('wishDatetobuy', '')
            wishobj=request.POST.get('wishobj','')


            fb=WishData(name=name,
                        wishDatetobuy=wishDatetobuy,
                        time=time,
                        wishobj=wishobj)
            fb.save()
            return redirect('/insert/')
    else:
        data=WishData.objects.all()
        form=WishListFrom()
        return render(request,'WishList.html',{'form':form,'data':data})
def delete(request):
    if request.method=='POST':
        dform=WishListDelForm(request.POST)
        if dform.is_valid():
            name=request.POST.get('name','')
            Wishlistname=WishData.objects.filter(name=name)
            if not Wishlistname:
                return HttpResponse(' WishList is not available')
            else:
                Wishlistname.delete()
                return HttpResponse('WishList is SuccessfullyDelete')


    else:
        wdform=WishListDelForm()
        return render(request,'Wishlist_delete.html',{'wdform':wdform})

