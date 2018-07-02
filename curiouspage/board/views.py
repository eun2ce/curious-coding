# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, BoardTitle
from django.views import generic
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