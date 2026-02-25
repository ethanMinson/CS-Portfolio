from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .contactForm import PortfolioAdd,PortfolioEdit
from .models import Hobbies
from .models import Portfolio

def index(request):
    return HttpResponse("Hello, world. You're at the base index.")

def home(request):
    home_text = "Hello there, my name is Ethan Minson. I am a Computer Science major at Weber State.\nI am in my senior year and graduating with my Bachelors in Computer Science in Spring 2026.\n I have spent my studies developing the skills to become a software developer.\n I like playing board games and watching movies.\n"
    context = {"home_text": home_text}
    return render(request, "PortfolioDatabase/home.html", context)

def hobbies(request):
    hobbies_list = Hobbies.objects.all()
    context = {"hobbies_list": hobbies_list}
    return render(request, "PortfolioDatabase/hobbies.html", context)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {"portfolio_list": portfolio_list}
    return render(request, "PortfolioDatabase/portfolio.html", context)

def hobbies_detailed(request):
    hobbies_list = Hobbies.objects.all()
    context = {"hobbies_list": hobbies_list}
    return render(request, "PortfolioDatabase/hobbies_detailed.html", context)

def portfolio_detailed(request):
    portfolio_list = Portfolio.objects.all()
    context = {"portfolio_list": portfolio_list}
    return render(request, "PortfolioDatabase/portfolio_detailed.html", context)
def portfolio_view(request, slug):
    project = Portfolio.objects.get(slug=slug)
    return render(request, "PortfolioDatabase/portfolio_detailed.html", {"project": project})
#make needed changes to the below views
@login_required(login_url="/login")
def portfolio_edit(request, slug):
    instance = Portfolio.objects.get(slug=slug)
    if request.method == "POST":
        form = PortfolioEdit(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("portfolio")
    else:
        form = PortfolioEdit(instance=instance)
    return render(request, "PortfolioDatabase/portfolio_edit.html", {"form": form})
@login_required(login_url="/login")
def portfolio_delete(request, slug):
    project = Portfolio.objects.get(slug=slug)

    if request.method == "POST":
        project.delete()
        if "next" in request.POST:
            return redirect(request.POST.get("next"))
        else:
            return redirect("/portfolio")
    return render(request, "PortfolioDatabase/portfolio_delete.html", {"project": project})

class AddPortfolio(FormView):
    template_name = "PortfolioDatabase/portfolio_add.html"
    form_class = PortfolioAdd
    success_url = "/portfolio"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "PortfolioDatabase/login.html", {"form":form})
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, "PortfolioDatabase/logout.html")
def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else:
        form = UserCreationForm()
    return render (request, "PortfolioDatabase/create-account.html", {"form": form})
