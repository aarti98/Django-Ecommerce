from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "product/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }

    return render(request, "product/list.html", context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)

        if instance is None:
            raise Http404("Product doesn't exist")
        return instance


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active= True)

        try:
            instance = Product.objects.get(slug = slug)

        except Product.DoesNotExist:
            raise Http404("Not found")

        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()

        except:
            raise Http404("Error")

        return instance


def product_detail_view(request, pk):
    # instance =get_object_or_404(Product,pk=pk)

    # try:
    #     instance = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     print('no products here')
    #     raise Http404("Product doesn't exist")
    #
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")

    # print(instance)
    # qs = Product.objects.filter(id=pk)
    #
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    #
    # else:
    #     raise Http404("Product doesn't exist!")

    context = {
        'object': instance
    }

    return render(request, "product/detail.html", context)


class ProductFeaturedListView(ListView):
    template_name = "product/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "product/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

