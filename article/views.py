from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt


def basic(request):
    return HttpResponse('Hello world')


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(request)
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    return render_to_response('article.html', args)


def like(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/articles/all')
        else:
            obj = Article.objects.get(id=article_id)
            obj.article_likes += 1
            obj.save()
            response = redirect('/articles/all')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/articles/all')


@csrf_exempt
def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
    return redirect('/articles/get/%s' % article_id)
