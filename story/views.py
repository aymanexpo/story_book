from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Category,Story

def story_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    story=Story.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        story=story.filter(category=category)
    return render(request,'story/story_list.html',{'categories':categories,
                                                   'story':story,
                                                   'category':category,
    })
def story_detail(request,id):
    story=get_object_or_404(Story,id=id)
    return render(request,'story/story_detail.html',{'story':story})
