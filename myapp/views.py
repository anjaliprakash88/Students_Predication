from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserDataForm
from .models import UserData
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
# Register user






def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login user
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

# Logout user
def user_logout(request):
    logout(request)
    return redirect('login')

# Dashboard
@login_required
def dashboard(request):
    form = UserDataForm()
    user_data = UserData.objects.filter(user=request.user)
    graph_type = request.GET.get('graph_type', None)
    graph_image = None

    if graph_type:
        graph_image = generate_graph(user_data, graph_type)

    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            student_data = form.save(commit=False)
            student_data.user = request.user
            student_data.save()
            return redirect('dashboard')

    return render(request, 'dashboard.html', {
        'form': form,
        'user_data': user_data,
        'graph_image': graph_image
    })

def generate_graph(user_data, graph_type):
    plt.figure(figsize=(6, 4))
    df = pd.DataFrame(list(user_data.values(
        'name', 'place', 'marks', 'class_name', 'semester', 'gender', 'nationality', 
        'grade', 'section', 'topic', 'stage', 'absent_days'
    )))

    if df.empty:
        return None  

    if graph_type == "marks_class_count":
        df.groupby("class_name")["marks"].count().plot(kind="bar", color="blue")
        plt.ylabel("Count")
        plt.title("Marks Class Count Graph")

    elif graph_type == "marks_class_semester":
        df.groupby(["class_name", "semester"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Semester-wise Graph")

    elif graph_type == "marks_class_gender":
        df.groupby(["class_name", "gender"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Gender-wise Graph")

    elif graph_type == "marks_class_nationality":
        df.groupby(["class_name", "nationality"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Nationality-wise Graph")

    elif graph_type == "marks_class_grade":
        df.groupby(["class_name", "grade"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Grade-wise Graph")

    elif graph_type == "marks_class_section":
        df.groupby(["class_name", "section"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Section-wise Graph")

    elif graph_type == "marks_class_topic":
        df.groupby(["class_name", "topic"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Topic-wise Graph")

    elif graph_type == "marks_class_stage":
        df.groupby(["class_name", "stage"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Stage-wise Graph")

    elif graph_type == "marks_class_absent_days":
        df.groupby(["class_name", "absent_days"])["marks"].mean().unstack().plot(kind="bar")
        plt.ylabel("Average Marks")
        plt.title("Marks Class Absent Days-wise Graph")

    else:
        return None  

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode("utf-8")

# Save User Data
@login_required
def save_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
    return redirect('dashboard')
