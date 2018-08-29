# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board,Category
from django.urls import reverse,reverse_lazy
from django.views import generic
from .forms import BoardForm, ConfirmPasswordForm, SignUpForm
from pytz import timezone

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
# from django.core.urlresolvers import reverse_lazy # generic view에서는 reverse_lazy를 사용한다.
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'board/index.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'board/adduser.html', {'form': form})
##


class IndexView(generic.ListView):
    template_name = 'board/index.html'  #index.html을 뿌려줄 것
    context_object_name = 'board_title'

    def get_queryset(self):
        search_word = self.request.GET.get('search_word', '')
        subject_type = self.request.GET.get('subject_type', '')
        if search_word : # 검색 된 단어 있으면
            return Board.objects.filter(title__icontains=search_word) or Board.objects.filter(content__icontains=search_word)
        if subject_type : # 클릭 된 키워드 있으면
            return Board.objects.filter(subject_type__icontains=subject_type)
        return Board.objects.order_by('-id')
# def detail
    
class DetailView(generic.DetailView):
    model = Board
    template_name = 'board/detail.html'
    context_object_name = 'board_detail'

    def get_object(self):
        board = super().get_object()
        board.count += 1
        board.save()
        return board
    # def get_context_data(self, **kwargs):
    #     confirm_pw = self.request.GET.get('confirm_pw')
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     if self.object.password == confirm_pw :
    #         self.object.delete()
    #         return HttpResponseRedirect(reverse('board:index'))
    
def writedel_confirm_pw(request,pk):
    board = get_object_or_404(Board,pk=pk)
    if request.method == 'POST' and request.POST['password'] == board.password:
        form = ConfirmPasswordForm(request.POST, instance = board)
        if form.is_valid():
            board = form.save(commit = False)
            board.delete()
            return HttpResponseRedirect(reverse('board:index'))
    else:
        form = ConfirmPasswordForm(instance=board)
    return render (request,'board/confirm_password.html',{
            'form' : form,
    })
        
def write_form(request):    #보여질 글쓰기 폼
    if request.method == 'POST':
        form = BoardForm(request.POST,request.FILES)
        if form.is_valid(): # 값이 들어오면 저장하고 인덱스로
            board = form.save(commit = False)
            # board = form.save(commit=False)   #사용자가 하지않는 pk입력을
            # board.title = Board.objects.get(pk=pk)    #개발자가 넣어준다
            form.save()
            return HttpResponseRedirect('/board')
           # return render(request,'board/index.html')
    else:       # 버튼 눌렀을 때 이동할 html
        form = BoardForm()
    return render (request,'board/write.html',{
        'form' : form,
    })

def do_write_board(request):
    br = Board(title = request.POST['title'],
               content = request.POST['content'],
               file = request.POST['file'],)
    br.save()
    return HttpResponseRedirect('board/index.html')

def write_eidt(request,pk):
    board = get_object_or_404(Board,pk=pk)
    if request.method == 'POST' and request.POST['password'] == board.password:
        form = BoardForm(request.POST,request.FILES, instance = board)
        if form.is_valid():
            board = form.save(commit = False)
            board.save()
            return HttpResponseRedirect(reverse('board:detail',args=(pk,)))
    else:
        form = BoardForm(instance=board)
    return render (request,'board/write.html',{
            'form' : form,
    })

def SuggestionView(request):
    return render (request,'board/Suggestion.html')
    
def InfoView(request):
    return render (request,'board/info.html')
# def commnet_new(request, pk):   ##댓글 남기기
#     board = get_object_or_404(Board,pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)   #사용자가 하지않는 pk입력을
#             comment.title = Board.objects.get(pk=pk)    #개발자가 넣어준다
#             comment.save()
#             return HttpResponseRedirect(reverse('board:detail',args=(board.id,)))
#     else:
#         form = CommentForm()
#     return render (request,'board/post_form.html',{
#         'form' : form,
#     })

# def comment_edit(request,board_pk,pk):  ##댓글 수정
#     comment =get_object_or_404(Comment,pk=pk)

#     if request.method == 'POST' and request.POST['password'] == comment.password:
#         form = CommentForm(request.POST, instance = comment)
#         if form.is_valid():
#             comment = form.save(commit = False)
#             comment.title = Board.objects.get(pk=board_pk)
#             comment.save()
#             return HttpResponseRedirect(reverse('board:detail',args=(board_pk,)))
#     else:
#         form = CommentForm(instance=comment)
#     return render (request,'board/post_form.html',{
#             'form' : form,
#     })

# def commentdel_confirm_pw(request,board_pk,pk):
#     comment = get_object_or_404(Comment,pk=pk)
#     if request.method == 'POST' and request.POST['password'] == comment.password:
#         form = ConfirmPasswordForm(request.POST, instance = comment)
#         if form.is_valid():
#             comment = form.save(commit = False)
#             comment.delete()
#             return HttpResponseRedirect(reverse('board:detail',args=(board_pk,)))
#     else:
#         form = ConfirmPasswordForm(instance=comment)
#     return render (request,'board/confirm_password.html',{
#             'form' : form,
#     })

# class CommentDelete(generic.DeleteView):
#     model = Comment
#     def get_success_url(self):
#         return reverse('board:detail',kwargs={'pk': self.object.title_id})
