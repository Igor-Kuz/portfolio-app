from django.contrib import messages
from .models import (
    Blog,
    Portfolio,
    Testimonial
)
from django.views import generic
from .forms import ContactForm


class MainPageView(generic.TemplateView):
    """класс для главной страницы"""
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context


class ContactView(generic.FormView):
    """класс для связи"""
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    """ класс для отображения списка портфолио"""
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    """ класс для отображения портфолио"""
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
    """ класс для списка постов"""
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    """ класс для отображения поста"""
    model = Blog
    template_name = "main/blog-detail.html"