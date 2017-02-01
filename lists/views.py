from django.shortcuts import render,redirect
from lists.models import Item,List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm,ExistingListItemForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

# 用户信息


def userinfo(request):
    return render(request, 'registration/userinfo.html')


# 注册函数
def register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            # return HttpResponseRedirect('/')
            return HttpResponseRedirect(reverse('home'))

            # return redirect(to='home')
        # else:
        #     return  HttpResponseRedirect('/lists/accounts/register',form.errors)

    context['form'] = form
    return render(request, 'registration/register.html', context)


# 登陆函数




def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # if request.method == "POST":
    #     return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html',{'form': ItemForm()}
    )

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    # items = Item.objects.filter(list=list_)
    if request.method == 'POST':

        form = ExistingListItemForm(for_list=list_,data=request.POST)
        if form.is_valid():
            form.save()
            # Item.objects.create(text = request.POST['text'],list=list_)

            return redirect(list_)
    return render(request, 'list.html',{'list':list_, 'form':form}
    )


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

    # return redirect('lists:view_list' ,list_.id)


