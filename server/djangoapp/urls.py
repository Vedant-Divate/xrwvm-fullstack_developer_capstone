"""URL routes for the dealership app: pages, auth, dealer and catalog APIs."""

from django.urls import path

from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', views.login_page, name='login_page'),
    path('frame/', views.frame_page, name='frame'),
    path('dealer/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealer/<int:dealer_id>/review/', views.add_review_page, name='add_review_page'),
    path('api/register/', views.api_register, name='api_register'),
    path('api/login/', views.api_login, name='api_login'),
    path('api/logout/', views.api_logout, name='api_logout'),
    path('api/dealers/', views.api_dealers, name='api_dealers'),
    path('api/dealers/<int:dealer_id>/', views.api_dealer_by_id, name='api_dealer_by_id'),
    path('api/reviews/<int:dealer_id>/', views.api_reviews, name='api_reviews'),
    path('api/reviews/<int:dealer_id>/add/', views.api_add_review, name='api_add_review'),
    path('api/cars/', views.api_cars, name='api_cars'),
    path('api/analyze/', views.api_analyze, name='api_analyze'),
    path('djangoapp/login', views.djangoapp_login, name='djangoapp_login'),
    path('djangoapp/logout', views.djangoapp_logout, name='djangoapp_logout'),
    path('djangoapp/get_cars', views.get_cars, name='get_cars'),
    path('fetchDealers', views.fetch_dealers, name='fetch_dealers'),
    path('fetchDealers/<str:state>', views.fetch_dealers_by_state, name='fetch_dealers_by_state'),
    path('fetchDealer/<int:dealer_id>', views.fetch_dealer, name='fetch_dealer'),
    path('fetchReviews/dealer/<int:dealer_id>', views.fetch_reviews, name='fetch_reviews'),
    path('analyze/<str:text>', views.analyze_text, name='analyze_text'),
]
