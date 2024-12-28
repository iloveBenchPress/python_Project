from celery import shared_task
from .models import ReviewsOfProduct, Product
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def save_review(user_id, product_id, memo):
    try:
        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)  # Получаем продукт по ID
        review = ReviewsOfProduct(author=user, product=product, memo=memo)  # Устанавливаем продукт
        review.save()
    except Exception as e:
        print(f"Error saving review: {e}")

@shared_task
def send_purchase_email(email, product_title):
    subject = 'Ваш заказ успешно оформлен!'
    message = f'Спасибо за покупку {product_title}. Ваш заказ был успешно оформлен.'
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )