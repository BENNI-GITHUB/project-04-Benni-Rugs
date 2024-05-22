"""Testimonial Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Testimonial
from django.urls import reverse_lazy
from .forms import TestimonialForm

class Testimonials(generic.ListView):
    """ This view is used to display all testimonials """
    model = Testimonial
    template_name = 'testimonials/testimonials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddTestimonial(
        LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):

    """This view is used to allow a user to add a testimonial"""
    form_class = TestimonialForm
    template_name = 'testimonials/add_testimonial.html'
    success_message = "Your testimonial was added successfully"

    def form_valid(self, form):
        """
        Override the form_valid() method in model form view
        in order to set the signed in user as the name on the testimonial.
        """
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditTestimonial(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView):

    """
    This view is used to allow logged in users to edit their own testimonials
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/edit_testimonial.html'
    success_message = "Testminonial edited successfully"

    def test_func(self):
        """
        Prevent another user from editing user's testminonial
        """
        testimonial = self.get_object()
        return testimonial.name == self.request.user\
            or self.request.user.is_superuser


class DeleteTestimonial(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own testimonials
    """
    model = Testimonial
    template_name = 'testimonials/delete_testimonial.html'
    success_message = "Testminonial successfully deleted"
    success_url = reverse_lazy('testimonials')

    def test_func(self):
        """
        Prevent another user from deleting another user's testminonial
        """
        testimonial = self.get_object()
        return testimonial.name == self.request.user\
            or self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteTestimonial, self).delete(request, *args, **kwargs)
