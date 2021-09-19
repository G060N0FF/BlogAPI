from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

blog_categories = (
    (1, 'Technology'),
    (2, 'Travel'),
    (3, 'Music'),
    (4, 'Lifestyle'),
    (5, 'Sports'),
    (6, 'Finance'),
    (7, 'Political'),
    (8, 'Business'),
    (9, 'Personal'),
    (10, 'Movie'),
    (11, 'Car'),
    (12, 'Gaming'),
)


class BlogPost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog_images')
    category = models.IntegerField(choices=blog_categories)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
