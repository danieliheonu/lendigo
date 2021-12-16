from .models import Story
import requests
from django.views.generic import ListView


class indexView(ListView):
    model = Story
    paginate_by = 20
    template_name = "home.html"
    ordering = '-id'

class Search(ListView):
    model =Story
    template_name = 'search.html'
    
    def get_queryset(self):
        if self.request.GET['search'] is not None:
            story = Story.objects.filter(title__icontains=self.request.GET['search'])
        else:
            story = Story.objects.all()
        return story

def new_story():
    stories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()[:100]

    new_story_id = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()[0]

    if new_story_id not in stories:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{new_story_id}.json?print=pretty").json()

        Story.objects.create(title=story['title'], url=story['url'])
