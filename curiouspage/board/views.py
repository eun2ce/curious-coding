# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board, Comment
from django.urls import reverse
from django.views import generic

from .forms import CommentForm, BoardForm
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'board/index.html'  #index.html을 뿌려줄 것
    context_object_name = 'board_title'
    def get_queryset(self):
        return Board.objects.order_by('-id')

class DetailView(generic.DetailView):
    model = Board
    template_name = 'board/detail.html'
    context_object_name = 'board_detail'
    # def get_queryset(self):
    #    return Board.objects.filter(id=self.kwargs['pk'])

def commnet_new(request, pk):
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

def write_form(request):    #보여질 글쓰기 폼
    return render(request,'board/write.html')

def do_write_board(request):
    br = Board(title = request.POST['title'],
               content = request.POST['content'],)
    br.save()


