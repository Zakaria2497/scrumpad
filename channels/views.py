from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from . import forms

# Create your views here.
class ChannelCreate(CreateView):
    form_class = forms.ChannelCreateForm
    success_url = reverse_lazy('home') #change it later to my_teams
    template_name = 'channels/create_channel.html'



from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ChannelCreateForm
from .models import Membership, Channel

def channelcreate(request):
    if request.method == 'POST':
        form = ChannelCreateForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            membership = Membership(channel=object.id, user=request.user.username, view=True, report=True, manage=True)
            membership.save()
            return redirect('home')
    else:
        form = ChannelCreateForm()
    return render(request, 'channels/create_channel.html', {'form': form})



class ChannelManage(TemplateView):
    template_name = 'channels/manage_channels.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        membership_list = list(Membership.objects.filter(user=self.request.user.username))
        channel_id_list = []
        for obj in membership_list:
            channel_id_list.append(obj.channel)
        context['channel_list'] = list(Channel.objects.filter(id__in=channel_id_list))
        
        class MyChannel:
            channel_id = 0
            channel_name = 'dummy'
            channel_description = 'dummy'
            view_perm = True
            report_perm = True
            manage_perm = True
        
        context['my_channels'] = []
        for channel in context['channel_list']:
            obj = MyChannel()
            obj.channel_id = channel.id
            obj.channel_name = channel.Name
            obj.channel_description = channel.Description
            for m in membership_list:
                if m.channel == channel.id:
                    obj.view_perm = m.view
                    obj.report_perm = m.report
                    obj.manage_perm = m.manage
                    break
            context['my_channels'].append(obj)
        
        return context

class IndividualChannelManage(TemplateView):
    template_name = 'channels/manage_individual_channel.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        id = self.kwargs['id']
        current_channel = list(Channel.objects.filter(id=id))
        context['this_channel'] = current_channel[0]
        return context

class ManageBasic(TemplateView):
    template_name = 'channels/manage_basic.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        id = self.kwargs['id']
        current_channel = list(Channel.objects.filter(id=id))
        context['this_channel'] = current_channel[0]
        return context



from django.shortcuts import get_object_or_404

def channelmanage(request, id):
    instance = get_object_or_404(Channel, id=id)
    form = ChannelCreateForm(request.POST or None, instance=instance)
    current_channel = list(Channel.objects.filter(id=id))
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'channels/manage_basic.html', {'form':form, 'this_channel':current_channel[0]}) 
