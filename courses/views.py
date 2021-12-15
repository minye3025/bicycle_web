from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import CourseInfo, CourseAdd
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     courseinf = CourseInfo.objects.all()
#     context = {'courseinf':courseinf}
#     return render(request, 'courses/index.html', context)



def index(request):
    courseinfo_list = CourseInfo.objects.all()
    context = {'courseinfo_list': courseinfo_list}
    return render(request, 'courses/index.html', context)
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') #페이지

    # 조회
    courses_list = CourseInfo.objects.all()

    # 페이징처리
    paginator = Paginator(courses_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'courses_list': page_obj}
    return render(request, 'courses/index.html', context)
    """



def detail(request, courseinfo_id):
    """
    board 내용 출력
    """
    courseinfo = get_object_or_404(CourseInfo, pk=courseinfo_id)
    context = {'courseinfo': courseinfo}
    return render(request, 'courses/detail.html', context)