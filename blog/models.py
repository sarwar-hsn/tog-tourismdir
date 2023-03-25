from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django import forms
import os
from pathlib import Path
from django.conf import settings
from django.db.models.signals import post_delete,post_save,pre_save
from django.dispatch import receiver
import shutil
from meta.models import ModelMeta

def validate_file_size(value):
    filesize= value.size
    if filesize > 1048576:
        raise ValidationError("You cannot upload file more than 1MB")
    else:
        return value


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    bio = models.CharField(max_length=240, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.user.get_username()}"


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,blank=True,null=True)
    view_count = models.PositiveIntegerField(default=0)
    # thumbnail = models.ImageField()

    def get_absolute_url(self):
        return reverse('blog-categorydetails', kwargs={"category_slug": self.category.slug})

    def is_uniqueslug(self):
        #trying to find a slug by category name 
        try:
            category = Category.objects.get(slug=slug)
            return category #if category is present then we return the category
        except: #if we encounter any error then we will return the error
            return None
    
    def clean(self):
        if self.slug is None:
            self.slug = slugify(self.title)
        category = self.is_uniqueslug()
        if category is None: #that mean the slug is unique, no category using this slug
            return
        else: #if the category is found that means the slug is not unique
            raise ValidationError(f"slug: {self.slug} is not unique. change it manually")

    def save(self, *args, **kwargs):
        super(Category,self).save(*args, **kwargs)  # Call the "real" save() method.
    class Meta:
        ordering = ['-id']
        verbose_name = "category"
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-categorydetails", kwargs={"category_slug": self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=30)
    view_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog-tags', kwargs={"hashtag": self.name})
    


def post_thumbnail_path(instance,filename,*args, **kwargs):
    datetime = instance.created_at
    year = datetime.strftime('%Y')
    month = datetime.strftime('%b')
    base, ext = os.path.splitext(filename)
    return f"blogs/{year}/{month}/{instance.slug}/thumbnail/{base}{ext}"


class Post(ModelMeta,models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    post_status =(
        (DRAFT,DRAFT),
        (PUBLISHED,PUBLISHED)
    )
    seo_title = models.CharField(max_length=200,blank=True,null=True)
    seo_description = models.TextField(blank=True,null=True)
    seo_keywords = models.TextField(blank=True,null=True)
    seo_imagelink = models.URLField(null=True,blank=True)
    #seolinks
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to=post_thumbnail_path,validators=[validate_file_size,])
    alttag = models.CharField(max_length=100)
    overview = models.TextField()
    tags = models.ManyToManyField(Tag,blank=True)
    content = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,default=DRAFT,choices=post_status)
    rating = models.IntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
        
    #seo meta
    #expects array of string
    def get_seo_keywords(self):
        if self.seo_keywords:
            return str.split(self.seo_keywords,sep=",")
        else:
            keywords = []
            for tag in self.tags.all():
                keywords.append(tag.name)
        return keywords
    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return self.title
    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description;
        return self.overview;
    def get_seo_image(self):
        if self.seo_imagelink:
            return self.seo_imagelink;
        else:
            return self.thumbnail.url;
                    
    _metadata = {
        'use_og':True,
        'use_twitter':True,
        'use_facebook':True,
        'use_schemaorg':True,
        'title':'get_seo_title',
        'description':'get_seo_description',
        'keywords':'get_seo_keywords',
        'image': 'get_seo_image',
        'url':'get_absolute_url',
        'locale':'en_US',
    }
    #end se0

    def is_uniqueslug(self):
        #trying to find a slug by category name 
        try:
            post = Post.objects.get(slug=slug)
            return post #if category is present then we return the category
        except: #if we encounter any error then we will return the error
            return None

    def clean(self):
        if self.slug is None:
            self.slug = slugify(self.title)
        post = self.is_uniqueslug()
        if post is None: #that mean the slug is unique, no category using this slug
            return
        else: #if the category is found that means the slug is not unique
            raise ValidationError(f"slug: {self.slug} is not unique. change it manually")

    def save(self, *args, **kwargs):
        super(Post,self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.title

    def getthumbnail(self):
        try:
            thumbnail = self.thumbnail
        except:
            thumbnail = None
        return thumbnail

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={"category_slug": self.category.slug,"blog_slug":self.slug})




def post_image_path(instance,filename,*args, **kwargs):
    datetime = instance.blog.created_at
    year = datetime.strftime('%Y')
    month = datetime.strftime('%b')
    base, ext = os.path.splitext(filename)
    return f"blogs/{year}/{month}/{instance.property.slug}/images/{base}{ext}"

class PostImages(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to=post_image_path,validators=[validate_file_size,])
    alttag = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.post.slug}_{self.post.pk}"
    