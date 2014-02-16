from django.contrib import admin
from boards.models import Board, Post, Comment, PostVote, CommentVote

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostVote)
admin.site.register(CommentVote)

