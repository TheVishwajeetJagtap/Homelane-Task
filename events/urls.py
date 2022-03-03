from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
	path('<int:year>/<str:month>/', views.home, name="home"),
	path('events', views.all_events, name="list-events"),
	path('add_venue', views.add_venue, name='add-venue'),
	path('list_venues', views.list_venues, name='list-venues'),
	path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
	path('add_event', views.add_event, name='add-event'),
	path('my_events', views.my_events, name='my_events'),
	path('admin_approval', views.admin_approval, name='admin_approval'),
	path('venue_events/<venue_id>', views.venue_events, name='venue-events'),
	path('show_event/<event_id>', views.show_event, name='show-event'),

    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
]