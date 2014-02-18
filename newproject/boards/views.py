from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from boards import models

def index(request):
    latest_posts = models.Post.objects.order_by('date_time')[:25]
    context =  { 'latest_posts' : latest_posts }
    return render(request, 'boards/index.html', context)

def board(request, board_slug):
    board = get_object_or_404(models.Board, slug=board_slug)
    
    context = { 'board' : board }
    return render(request, 'boards/board.html', context)

def post(request, board_slug, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    context = { 'post' : post }
    return render(request, 'boards/post.html', context)

@login_required
def post_vote(request, board_slug, post_id, direction):
    post = get_object_or_404(models.Post, pk=post_id)
    try:
        past_vote = models.PostVote.objects.filter(user=request.user, post=post_id).get()
        if past_vote.vote_type == 'UP':
            if direction == 'down':
                past_vote.vote_type == 'DW'
                past_vote.save()
        else:
            if direction == 'up':
                past_vote.vote_type == 'UP'
                past_vote.save()
    except ObjectDoesNotExist:
        if direction == 'up':
            vote = models.PostVote(user=request.user, post=post, vote_type='UP')
            vote.save()
        else:
            vote = models.PostVote(user=request.user, post=post, vote_type='DW')
            vote.save()
    return redirect('boards:post', board_slug=board_slug, post_id=post_id)

@login_required
def comment_vote(request, board_slug, post_id, comment_id, direction):
    comment = get_object_or_404(models.Comment, pk=comment_id)
    try:
        past_vote = models.CommentVote.objects.filter(user=request.user, comment=comment_id).get()
        if past_vote.vote_type == 'UP':
            if direction == 'down':
                past_vote.vote_type == 'DW'
                past_vote.save()
        else:
            if direction == 'up':
                past_vote.vote_type == 'UP'
                past_vote.save()
    except ObjectDoesNotExist:
        if direction == 'up':
            vote = models.CommentVote(user=request.user, comment=comment, vote_type='UP')
            vote.save()
        else:
            vote = models.CommentVote(user=request.user, comment=comment, vote_type='DW')
            vote.save()
    return redirect('boards:post', board_slug=board_slug, post_id=post_id)

@login_required
def submit_post(request, board_slug):
    board = models.Board.objects.get(slug=board_slug)
    if board:
        post = models.Post(user=request.user, board=board, title=request.POST['title'], url=request.POST['url'], text=request.POST['body'])
        post.save()
        return redirect('boards:post', board_slug=board_slug, post_id=post.pk)
    else:
        return redirect('boards:board', board_slug=board_slug)

@login_required
def submit_comment(request, board_slug, post_id):
    post = models.Post.objects.get(pk=post_id)
    if post:
        comment = models.Comment(user=request.user, post=post, text=request.POST['body'])
        comment.save()
    return redirect('boards:post', board_slug=board_slug, post_id=post_id)
