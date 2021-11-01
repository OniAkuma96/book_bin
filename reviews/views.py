from django.shortcuts import render

def new_review(request):
    return render(request, 'reviews/new_review.html')
