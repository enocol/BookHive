import datetime
from django.test import TestCase
from django.urls import reverse
from .forms import ReviewForm
from .models import Book

# Create your tests here.

class ReviewFormTest(TestCase):
    def test_review_form_valid_data(self):
        form = ReviewForm(data={
            'comment': 'Great book!',
            'rating': 5
        })
        self.assertTrue(form.is_valid(), msg="Form should be valid with correct data")

    def test_review_form_invalid_data(self):
        form = ReviewForm(data={
            'comment': '',
            'rating': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors)
        self.assertIn('rating', form.errors)

    def test_review_form_comment_required(self):
        form = ReviewForm(data={'rating': 5})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors)

class TestbookDetailsView(TestCase):
    def setUp(self):
       self.book = Book.objects.create(
            id=1,
            title='Test Book',
            author='Test Author',
            category='Fiction',
            published_date=datetime.date(2023, 1, 1),
            cover_image='https://example.com/image.jpg',
            number_of_pages=200,
            number_of_copies=5,
            description='This is a test book description.',
            featured=True,
            created_at=datetime.date(2023, 1, 1)
        )
        

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/book_detail.html')
        self.assertContains(response, self.book.title)

    

    


   