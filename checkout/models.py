from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Purchase(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total = self.price * self.qty
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase made for book#{self.book_id} by user#{self.user_id} on {self.purchase_date}"
