from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    request.GET.get('item_name')
    context = {
        'reviews': reviews,
        'item_name': request.GET.get('item_name')
    }
    return render(request, 'reviews/index.html', context)

    


def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user 
            review.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
    }
    return render(request,'reviews/form.html', context)



def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        'review': review,
        'comments': review.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)