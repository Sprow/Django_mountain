from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from publications.models import Publication, PublicationLike, PublicationComment
from publications.forms import PublicationForm, PublicationCommentForm
from utils import gen_page_list


def publications(request):
    form = PublicationForm()
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Publication.objects.create(title=data.get("title"),
                                       body=data.get("body"),
                                       image=data.get("image"),
                                       author=request.user)
    publications = Publication.objects.all()
    paginator = Paginator(publications, 2)
    page = request.GET.get('page', 1)
    last_page = paginator.num_pages
    paginator_gen_list = gen_page_list(int(page), paginator.num_pages)
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)

    return render(request, "publications.html", {"publications": publications,
                                                 "form": form,
                                                 "last_page": last_page,
                                                 "paginator_gen_list": paginator_gen_list})

def single_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    form = PublicationCommentForm()
    if request.method == "POST":
        form = PublicationCommentForm(request.POST)
        if form.is_valid():
            PublicationComment.objects.create(comment=form.cleaned_data["comment"],
                                              user=request.user,
                                              publication=publication)
        return HttpResponseRedirect(reverse("single_publication", kwargs={"publication_id": publication_id}))
    return render(request, "single_publication.html", {"publication": publication,
                                                       "form": form})


def like_single_publication(request, publication_id):
    if request.user.is_authenticated():
        publication = get_object_or_404(Publication, pk=publication_id)
        if PublicationLike.objects.filter(publication=publication, user=request.user).exists():
            PublicationLike.objects.filter(publication=publication, user=request.user).delete()
        else:
            PublicationLike.objects.create(publication=publication, user=request.user)
        return HttpResponseRedirect(reverse("single_publication", kwargs={"publication_id": publication_id}))
    else:
        return HttpResponseRedirect(reverse("login"))


