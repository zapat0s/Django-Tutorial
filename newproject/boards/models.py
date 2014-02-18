from django.db import models
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User


class Board(models.Model):
    slug = models.SlugField()

    def __str__(self):
        return self.slug


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    board = models.ForeignKey(Board, related_name='posts')
    date_time = models.DateTimeField(auto_now=True)
    title = models.TextField()
    text = models.TextField()
    url = models.URLField()

    @property
    def count_votes(self):
        total = 0;
        for vote in self.votes.all():
            if vote.vote_type == 'UP':
                total += 1
            elif vote.vote_type == 'DW':
                total -= 1
        return total
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    date_time = models.DateTimeField(auto_now=True)
    text = models.TextField()

    @property
    def count_votes(self):
        total = 0;
        for vote in self.votes.all():
            if vote.vote_type == 'UP':
                total += 1
            elif vote.vote_type == 'DW':
                total -= 1
        return total

    def __str__(self):
        return self.text

VOTE_TYPE = (
    ('UP', 'Upvote'),
    ('DW', 'Downvote'),
)

class PostVote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='votes')
    vote_type = models.CharField(max_length=2, choices=VOTE_TYPE)

    def __str__(self):
        return self.post.title

        

class CommentVote(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment, related_name='votes')
    vote_type = models.CharField(max_length=2, choices=VOTE_TYPE)

    def __str__(self):
        return self.post.title

