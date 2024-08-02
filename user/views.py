from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .pro import chatbotfun
from .models import Feedbacks
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please Login First!!")
            return redirect('sin')
    return inner

dec=[never_cache,signin_required]

# Create your views here.
@method_decorator(dec,name="dispatch")
class UserHomeView(TemplateView):
    template_name="userhome.html"

@method_decorator(dec,name="dispatch")
class ChatbotView(View):
    def get(self,request):
        return render(request,"chatbot.html")
    def post(self,request):
        question=request.POST.get('qstn')
        res=chatbotfun(question)
        print(res)
        return render(request,"chatbot.html",{"result":res,"question":question})


@method_decorator(dec,name="dispatch")
class FeedBackView(View):
    def get(self,request):
        data=Feedbacks.objects.all()
        return render(request,"feedback.html",{"data":data})
    def post(self,request):
        try:
            feed=request.POST.get('feed')
            user=request.user
            Feedbacks.objects.create(feedback=feed,user=user)
            messages.success(request,"Feedback added successfully!!")
            return redirect('uhome')
        except:
            messages.error(request,"Feedback adding is failed!!")
            return redirect('uhome')
        
        
@method_decorator(dec,name="dispatch")
class ContactView(TemplateView):
    template_name="contact.html"