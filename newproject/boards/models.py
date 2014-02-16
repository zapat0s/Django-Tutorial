from django.db import models
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User


class Board(models.Model):
    slug = models.SlugField()

    def __unicode__(self):
        return self.slug


class Post(models.Model):
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    date_time = models.DateTimeField(auto_now=True)
    title = models.TextField()
    text = models.TextField()
    url = models.URLField()
    
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __unicode__(self):
        return self.text

VOTE_TYPE = (
    ('UP', 'Upvote'),
    ('DW', 'Downvote'),
)

class PostVote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    vote_type = models.CharField(max_length=2, choices=VOTE_TYPE)

    def __unicode__(self):
        return self.post.title

        

class CommentVote(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    vote_type = models.CharField(max_length=2, choices=VOTE_TYPE)

    def __unicode__(self):
        return self.post.title

