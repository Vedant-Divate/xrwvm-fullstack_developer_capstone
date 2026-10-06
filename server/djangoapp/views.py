"""Views: pages, auth APIs, dealer/review APIs and sentiment analysis."""

import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, Dealer, Review
from .sentiment import analyze_sentiment


def _dealer_dict(dealer):
    """Serialize a dealer for JSON APIs."""
    return {
        'id': dealer.id, 'name': dealer.name, 'city': dealer.city,
        'state': dealer.state, 'address': dealer.address,
        'zip': dealer.zip_code, 'phone': dealer.phone,
    }


def _review_dict(review):
    """Serialize a review for JSON APIs."""
    return {
        'id': review.id, 'dealer_id': review.dealer_id,
        'user': review.user.username, 'content': review.content,
        'rating': review.rating, 'sentiment': review.sentiment,
    }


# ------------------------------- Pages -------------------------------------

def home(request):
    """Home page with dealers, optionally filtered by state."""
    state = request.GET.get('state', '').upper()
    dealers = Dealer.objects.filter(state=state) if state else Dealer.objects.all()
    return render(request, 'djangoapp/home.html', {'dealers': dealers, 'state': state})


def dealer_detail(request, dealer_id):
    """Dealer details page with reviews."""
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    reviews = dealer.review_set.order_by('-created_at')
    return render(request, 'djangoapp/dealer_detail.html', {'dealer': dealer, 'reviews': reviews})


def add_review_page(request, dealer_id):
    """Post Review page: form shown before submission."""
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'djangoapp/add_review.html', {'dealer': dealer})


def about_page(request):
    """About Us page."""
    return render(request, 'about.html')


def contact_page(request):
    """Contact Us page."""
    return render(request, 'contact.html')


def login_page(request):
    """Student login form page."""
    error = ''
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        error = 'Invalid credentials'
    return render(request, 'djangoapp/login.html', {'error': error})


def frame_page(request):
    """Local screenshot helper: renders a browser bar around any page."""
    return render(request, 'djangoapp/frame.html', {'path': request.GET.get('u', '/')})


# ------------------------------- Auth APIs ---------------------------------

@csrf_exempt
def api_register(request):
    """Register a new user account."""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body or '{}')
    if User.objects.filter(username=data.get('username')).exists():
        return JsonResponse({'error': 'User already exists'}, status=400)
    user = User.objects.create_user(
        username=data.get('username'), password=data.get('password'),
        first_name=data.get('first_name', ''), last_name=data.get('last_name', ''),
        email=data.get('email', ''),
    )
    return JsonResponse({'message': 'Registered', 'username': user.username})


@csrf_exempt
def api_login(request):
    """Log in with username and password."""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body or '{}')
    user = authenticate(username=data.get('username'), password=data.get('password'))
    if user is None:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    login(request, user)
    return JsonResponse({'message': 'Logged in', 'username': user.username})


@csrf_exempt
def api_logout(request):
    """Log out the current user."""
    logout(request)
    return JsonResponse({'message': 'Logged out'})


# ------------------------------ Dealer APIs --------------------------------

def api_dealers(request):
    """Return all dealers, optionally filtered by ?state=KS."""
    state = request.GET.get('state', '').upper()
    dealers = Dealer.objects.filter(state=state) if state else Dealer.objects.all()
    return JsonResponse(list(map(_dealer_dict, dealers)), safe=False)


def api_dealer_by_id(request, dealer_id):
    """Return details of a single dealer."""
    return JsonResponse(_dealer_dict(get_object_or_404(Dealer, pk=dealer_id)))


def api_reviews(request, dealer_id):
    """Return reviews for a dealer."""
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return JsonResponse(list(map(_review_dict, dealer.review_set.all())), safe=False)


@csrf_exempt
def api_add_review(request, dealer_id):
    """Add a review for a dealer (logged-in users)."""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=403)
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body or '{}')
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    sentiment = analyze_sentiment(data.get('content', ''))['label']
    review = Review.objects.create(
        dealer=dealer, user=request.user, content=data.get('content', ''),
        rating=int(data.get('rating', 5)), sentiment=sentiment,
    )
    return JsonResponse({'message': 'Review added', 'review': _review_dict(review)})


# ------------------------------ Catalog APIs -------------------------------

def api_cars(request):
    """Return all car makes with their models."""
    out = []
    for make in CarMake.objects.all():
        out.append({
            'make': make.name, 'description': make.description,
            'models': [
                {'name': m.name, 'body_type': m.body_type, 'year': m.year}
                for m in make.carmodel_set.all()
            ],
        })
    return JsonResponse(out, safe=False)


@csrf_exempt
def api_analyze(request):
    """Analyze sentiment of the posted review text."""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body or '{}')
    result = analyze_sentiment(data.get('text', ''))
    return JsonResponse({'text': data.get('text', ''), **result})
