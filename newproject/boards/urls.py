from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'boards.views.index', name='index'),
    url(r'^r/(?P<board_slug>\w+)/$', 'boards.views.board', name='board'),
    url(r'^r/(?P<board_slug>\w+)/(?P<post_id>\d+)/$', 'boards.views.post', name='post'),
    url(r'^r/(?P<board_slug>\w+)/submit/$', 'boards.views.submit_post', name='submit_post'),
    url(r'^r/(?P<board_slug>\w+)/(?P<post_id>\d+)/submit/$', 'boards.views.submit_comment', name='submit_comment'),
    url(r'^r/(?P<board_slug>\w+)/(?P<post_id>\d+)/(?P<direction>\w+)/$', 'boards.views.post_vote', name='post_vote'),
    url(r'^r/(?P<board_slug>\w+)/(?P<post_id>\d+)/(?P<comment_id>\d+)/(?P<direction>\w+)/$', 'boards.views.comment_vote', name='comment_vote'),
    

)
