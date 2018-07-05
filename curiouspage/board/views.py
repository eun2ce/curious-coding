# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board, Comment
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from .forms import CommentForm, BoardForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'board/index.html'  #index.html을 뿌려줄 것
    context_object_name = 'board_title'

    def get_queryset(self):
        search_word = self.request.GET.get('search_word', '')
        if search_word : # 검색 된 단어 있으면
            return Board.objects.filter(title__icontains=search_word)
        return Board.objects.order_by('-id')
    
class DetailView(generic.DetailView):
    model = Board
    template_name = 'board/detail.html'
    context_object_name = 'board_detail'
    # def get_queryset(self):
    #    return Board.objects.filter(id=self.kwargs['pk'])
def write_form(request):    #보여질 글쓰기 폼
    if request.method == 'POST':
        form = BoardForm(request.POST,request.FILES)
        if form.is_valid(): # 값이 들어오면 저장하고 인덱스로
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

    if request.method == 'POST':
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

def commnet_new(request, pk):   ##댓글 남기기
    board = get_object_or_404(Board,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)   #사용자가 하지않는 pk입력을
            comment.title = Board.objects.get(pk=pk)    #개발자가 넣어준다
            comment.save()
            return HttpResponseRedirect(reverse('board:detail',args=(board.id,)))
    else:
        form = CommentForm()
    return render (request,'board/post_form.html',{
        'form' : form,
    })

def comment_edit(request,board_pk,pk):  ##댓글 수정
    comment =get_object_or_404(Comment,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.title = Board.objects.get(pk=board_pk)
            comment.save()
            return HttpResponseRedirect(reverse('board:detail',args=(board_pk,)))
    else:
        form = CommentForm(instance=comment)
    return render (request,'board/post_form.html',{
            'form' : form,
    })
        
