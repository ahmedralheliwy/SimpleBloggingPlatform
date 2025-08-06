from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
    
    def short_description(self):
        return self.content[:70] + '...' if len(self.content) > 70 else self.content

    def edit(self, new_title, new_content, new_image):
        self.title = new_title
        self.content = new_content
        self.image = new_image
        self.save()