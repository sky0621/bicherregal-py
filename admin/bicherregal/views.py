from django.shortcuts import render
from django.http import HttpResponse

# TODO docstring

# Create your views here.
def index(request):
    return HttpResponse("トップページ（一覧へリダイレクト？）")

def list(request):
    return HttpResponse("本棚写真一覧")

def add(request):
    return HttpResponse("本棚写真追加")

def edit(request):
    return HttpResponse("本棚写真編集")

def delete(request):
    return HttpResponse("本棚写真削除")

def login(request):
    return HttpResponse("ログイン（※後回し）")

def logout(request):
    return HttpResponse("ログアウト（※後回し）")
