from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from shopapp import forms
from .models import Product

def index(request):
    listings = Product.objects.filter(is_published=True)

    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'index.html', context)


def detail_view(request, listing_id):
    single_view = get_object_or_404(Product, pk=listing_id) #Return 404 error if no object found

    context = {
        'single_view': single_view}
    return render(request, 'detail.html', context=context)

def create_product_view(request):
    form = forms.ProductForm()
    if request.method=='POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'post-product.html', {'form': form})
