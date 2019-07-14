from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse
class BlogFeed(Feed):
    title="xdc"
    desc="学习django开发"
    link="/"
    def items(self):
        return Article.objects.order_by("-create_time")
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.author.username+":"+item.title
    def item_link(self, item):
        return reverse("blog:single",args=(item.id,))



