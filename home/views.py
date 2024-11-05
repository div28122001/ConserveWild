from email.headerregistry import SingleAddressHeader
from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . models import * 
from django.contrib.auth.models import User,auth
from .models import  Room , Message
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.
# Create your views here.


def index(request):
    pdis={}
    ps=Post.objects.all()
    pdis["pkey"]=ps
    cdis={}
    cg=pscat.objects.all()
    cdis["ckey"]=cg
    pl=Package.objects.all()
    pdis["data"]=pl
    
   
    return render(request,"index.html",cdis|pdis)

def faq(request):
    return render(request,"faq.html")
def know(request):
    return render(request,"know.html")

def plan(request):
    
    return render(request,"plan.html")
def addpost(request): 
     
    pdis={}
    cg=pscat.objects.all()
    pdis["ckey"]=cg
    if request.method=="POST":
        usr=get_object_or_404(User,id=request.user.id)
        
        ct=request.POST["categ"]   
        pt=request.POST["ptitle"]
        ds=request.POST["desc"]
        ctg=ctg=get_object_or_404(pscat,id=ct)
        pst=Post(usr=usr,cat=ctg,pst_title=pt,pst_desc=ds)
        pst.save()
        if "bimg" in request.FILES:
            b_image=request.FILES["bimg"]
            pst.img=b_image
            pst.save()
        pst.save()
        return redirect("wild")
        
        
    return render(request,'add-post.html',pdis)


def likeview(request,pk):
    pst=get_object_or_404(Post,id=request.POST.get("post_id"))
    pst.likes.add(request.user)
    return redirect("wild")
def cmnt(request,pk):
  
    usr=get_object_or_404(User,id=request.user.id)
    if request.method=="POST":
        com=request.POST["cmt"]
        pest=request.POST["pst"]
        pst=get_object_or_404(Post,id=pest)
        rea=Reaction(pst=pst,Comment=com,user=usr)
        rea.save()
       
        cmt=Reaction.objects.filter(pst=pk) 
        return redirect("wild")
    pest=Post.objects.all()
    
    return render(request,"wildopedia.html",{"pkey" :pest,"cmt":cmt})
def price(request):
    pla=Package.objects.all()
    mem=auth.authenticate(plan=pla)
    if mem!=None:
        return redirect('index')
    return render(request,'pricing.html',{"data":pla})
def wild(request,pid):
    pdis={}
    ct=pscat.objects.get(id=pid)
    ps=Post.objects.filter(cat=ct)
    
    cmt=Reaction.objects.filter(pst=pid) 
    pdis["pkey"]=ps
    pdis["cmt"]=cmt
    return render(request,"wildopedia.html",pdis)

def wildopedia(request):  
    pst=Post.objects.all()  
    for i in pst:
        cmt=Reaction.objects.filter(pst=i.id) 

    return render(request,"wildopedia.html",{"pkey" :pst,"cmt":cmt})
def rules(request):
    return render(request,"rules.html")

def services(request):
    return render(request,"services.html")

def details(request):
    return render(request,"details.html")

def sponser(request):
    return render(request,"sponser.html")
def search(request):
    pdis={}
    if request.method=="POST":
        sr=request.POST["ser"]
        ps=Post.objects.filter( pst_title__icontains=sr)
        pdis["pkey"]=ps
    return render(request,"wildopedia.html",pdis)
def contact(request):
    if request.method=="POST":
        sub=request.POST["sub"]
        msg=request.POST["msg"]
        num=request.POST["num"]
        usr=get_object_or_404(User,id=request.user.id)
        cn=Contact(user=usr,sub=sub,message=msg,contactnum=num)
        cn.save()
    
    return render(request,"contact.html")
def like(request, id):
    new_like, created = Reaction.objects.get_or_create(user=request.user, pst_id=Posts.id)
    if not created:
        pass
    else:
        # oll korrekt
     pic = get_object_or_404(Reaction, id=id)
    user_likes_this = pic.like_set.filter(user=request.user) and True or False
    p = Post.objects.get()
    number_of_likes = p.like_set.all().count()

# Create your views here.
def chat(request):
    return render(request, 'chat.html')
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def addtocart(request):
    dic={}
    item=cart.objects.filter(user__id=request.user.id,status="False")
    dic["item"]=item
    if request.user.is_authenticated:
        if request.method=="POST":
            sid=request.POST["pid"]
            quant=request.POST["qty"]
            is_exist=cart.objects.filter(service__id=sid,user__id=request.user.id,status="False")
            if len(is_exist)>0:
                dic["msg"]="Item Already Exists In Your Cart."
            else:
                srv=get_object_or_404(Package,id=sid)
                usr=get_object_or_404(User,id=request.user.id)
                crt=cart(user=usr,service=srv,quantity=quant)
                crt.save()
                dic["msg"]="{} Added in your cart".format(srv.p_name)
                dic["cls"]="alert alert success"
    else:
        dic["status"]="Please Login First to Checkout"
    return render(request,'cart.html',dic)

def get_cart_data(request):
    item = cart.objects.filter(user__id=request.user.id, status=False)
    sale,quantity =0,0
    for i in item:
        sale+=float(i.service.p_price)*i.quantity
        quantity=i.quantity
    resp={"quan":quantity,"tot":sale}
    return JsonResponse(resp)

def remove_package(request):
    if "delete_cart" in request.GET:
        id=request.GET["delete_cart"]
        cartobj=get_object_or_404(cart,id=id)
        cartobj.delete()
    return HttpResponse(1)


def process_payment(request):
    prod=""
    amt=0
    inv="Meditationer Invoice"
    pid=""
    cartid=""
    items = cart.objects.filter(user_id__id=request.user.id,status=False)
    for i in items:
        prod+=str(i.service.p_name)+"/n"
        amt+=(i.service.p_price)/75
        inv+=str(i.id)
        pid+=str(i.service.id)+","
        cartid+=str(i.id)+","
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt),
        'item_name': prod,
        'invoice': inv,
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                            reverse('success_payment')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                            reverse('cancel_payment')),
    }
    usr=User.objects.get(username=request.user.username)
    ord=Order(cust_id=usr,cart_ids=cartid,product_ids=pid)
    ord.save()
    ord.invoice_id=str(ord.id)+inv
    ord.save()
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'order': ord,'form': form})
def success_payment(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"success_payment.html")

def cancel_payment(request):
    return render(request,"cancel_payment.html")
