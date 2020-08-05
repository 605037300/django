from django.shortcuts import render,redirect,reverse,HttpResponse
from .models import *
from .forms import *
import hashlib,datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def tt(request):
    return HttpResponse(settings.CONFIRM_DAYS)
# Create your views here.
def index(request):
    if not request.session.get("is_login",None):
        return redirect('/app05/login/')
    return render(request,'app05/index.html')

def doHash(s,salt="mysite"):
    h=hashlib.sha256()
    s+=salt
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    if request.method=="POST":
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            msg="检查填写"
            name=loginform.cleaned_data.get('name')
            password=loginform.cleaned_data.get('password')
            try:
                userobj=User.objects.get(name=name)
            except User.DoesNotExist:
                msg="用户名不存在"
                return render(request,"app05/login.html",locals())
            if userobj.password==doHash(password):
                request.session['is_login']=True
                request.session['user_id']=userobj.id
                request.session['user_name']=userobj.name
                return redirect(reverse("app05:index"))
            else:
                msg="密码错误"
                return render(request,'app05/login.html',locals())

        return render(request,'app05/login.html',locals())




        # name=request.POST.get("name")
        # password=request.POST.get('password')
        # if name.strip() and password:
        #     try:
        #         userobj=User.objects.get(name=name) 
        #     except:
        #         return render(request,"app05/login.html",{"msg":"用戶名不存在"})
        #     if userobj.password==password:
        #         return render(request,"app05/index.html")
    loginform=LoginForm()
    return render(request,"app05/login.html",locals())

def make_code(userobj):
    now=datetime.datetime.now().strftime("%Y-%m-%D $H-%M-%S")
    print("xxxxxxxxxxxxxxxx",userobj,now)
    code=doHash(userobj.name,now)
    return code

def send_mail(toemail,codestring):
    subject,from_email="HEHE",'byjdh@qq.com'
    default_text="aa"
    context_html='''
                 <p><a href="http://{}/app05/confirm/?code={}">点击激活</a></p>
                 <p>有效期为:<h1>{}</h1></p>
    '''.format("localhost:8000",codestring,settings.CONFIRM_DAYS)
    mailmsg=EmailMultiAlternatives(subject,default_text,from_email,toemail)
    mailmsg.attach_alternative(context_html,'text/html')
    mailmsg.send()




def register(request):
    if request.session.get("is_login",None):
        return redirect("/app05/index")
    
    if request.method=="POST":
        registerform=RegisterForm(request.POST)
        if registerform.is_valid():
            name=registerform.cleaned_data.get("name")
            password1=registerform.cleaned_data.get("password1")
            password2=registerform.cleaned_data.get('password2')
            sex=registerform.cleaned_data.get("sex")
            email=registerform.cleaned_data.get("email")
            # print("----------",locals())
            if password1 !=password2:
                msg="两次密码不一致"
                return render(request,"app05/register.html",locals()) 
            elif User.objects.filter(name=name).first():
                msg="用户名不能重复"
                return render(request,"app05/register.html",locals()) 
            elif User.objects.filter(email=email).first():
                msg="邮箱不能重复"
                return render(request,"app05/register.html",locals()) 
            else:
                newobj=User.objects.create(name=name,password=doHash(password1),sex=sex,email=email)
                msg="成功"
                # 生成嘛并存入数据库
                code=make_code(newobj)
                # print("code-------",code)
                cons=ConfirmString.objects.create(code=code,user=newobj)
                print("--------------",cons)
                # 把嘛发送邮件
                to_email=["byjdh@qq.com",]
                send_mail(to_email,code)
                # 返回一个注册邮箱连接
                return render(request,"app05/confirm.html",locals())
        return render(request,"app05/register.html",locals())

    registerform=RegisterForm()
    return render(request,"app05/register.html",locals())

def logout(request):
    if request.session.get("is_login",None):
        request.session.flush()
      
    return redirect('/app05/login/')



def confirm(request):
    code=request.GET.get("code",None)
    codeobj=ConfirmString.objects.filter(code=code).first()
    if not codeobj:
        return render(request,'app05/confirm.html',{"msg":"无效激活码"})

    if datetime.datetime.now() >= codeobj.c_time+datetime.timedelta(days=settings.CONFIRM_DAYS):
        codeobj.user.delete()
        return render(request,"app05/confirm.html",{"msg":"激活码过期"})
    codeobj.user.has_confirmed=True
    codeobj.user.save()
    codeobj.delete()

    return render(request,"app05/confirm.html",{"msg":"激活成功"})