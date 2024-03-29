from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import *
from .forms import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import django_filters 
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import status
from django.db.models import Q
from rest_framework import generics, pagination
from rest_framework import filters

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    cats = Categories.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['cats'] = self.cats
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', None)
        if category:
            queryset = queryset.filter(category__name=category, user=self.request.user)
        else:
            queryset = queryset.filter(user=self.request.user)
        return queryset
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','category', 'filter', 'hashtag', 'description', 'complete', 'notice']
    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','category', 'filter','hashtag', 'description', 'complete', 'notice']
    success_url = reverse_lazy('tasks')
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
# class TaskAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
# class TaskAPIView(APIView):
#     def get(self, request):
#         t = Task.objects.all()
#         return Response({'tasks': TaskSerializer(t, many=True).data})

@api_view(['GET'])
def api_root(request, format=None):
        return Response({
        'tasks': reverse('task-list', request=request, format=format),
        'user': reverse('user-list-create', request=request, format=format),
        
    })  


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskApiListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'complete']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user_id=user)
    
    @action(detail=False, methods=['GET'])
    def custom_action_list(self, request):
        tasks = Task.objects.filter(complete=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['POST'])
    def custom_action_detail(self, request, pk=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserAPIListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    
class QueryTask1APIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get_queryset(self):
        queryset = Task.objects.filter(Q(title__startswith = 'К') | (Q(title__startswith = 'П') | ~ Q(title__startswith = 'С')))
        return queryset
    
class QueryTask2APIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get_queryset(self):
        queryset = Task.objects.filter(Q(title__startswith = 'К') | (Q(title__startswith = 'О') & ~ Q(description__startswith = 'д')))
        return queryset