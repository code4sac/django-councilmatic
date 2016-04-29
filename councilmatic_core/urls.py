from django.conf.urls import url
from . import views
from . import feeds

from django.contrib import admin
admin.autodiscover() # XXX necessary?

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='abouts'),
    url(r'^committees/$', views.CommitteesView.as_view(), name='committees'),
    url(r'^council-members/$', views.CouncilMembersView.as_view(),
        name='council_members'),
    url(r'^committee/(?P<slug>[^/]*)/events/rss/$',
        feeds.CommitteeDetailEventsFeed(), name='committee_detail_events_feed'),
    url(r'^committee/(?P<slug>[^/]*)/actions/rss/$',
        feeds.CommitteeDetailActionFeed(), name='committee_detail_action_feed'),
    url(r'^committee/(?P<slug>[^/]*)/$',
        views.CommitteeDetailView.as_view(), name='committee_detail'),
    url(r'^legislation/(?P<slug>[^/]*)/$',
        views.BillDetailView.as_view(), name='bill_detail'),
    url(r'^person/(?P<slug>[^/]*)/rss/$', feeds.PersonDetailFeed(), name='person_feed'),
    url(r'^person/(?P<slug>[^/]*)/$', views.PersonDetailView.as_view(), name='person'),
    url(r'^events/$', views.EventsView.as_view(), name='events'),
    url(r'^event/(?P<slug>[^/]*)/$',
        views.EventDetailView.as_view(), name='event_detail'),
    url(r'^flush-cache/(.*)/$', views.flush, name='flush'),
    url(r'^pdfviewer/$', views.pdfviewer, name='pdfviewer'),
]
