from celery import shared_task
from .models import Review
from django.contrib.auth.models import User
@shared_task
def save_review(user_id, memo):
    try:
        user = User.objects.get(id=user_id)
        review = Review(author=user, memo=memo)
        review.save()
    except Exception as e:
        print(f"Error saving review: {e}")