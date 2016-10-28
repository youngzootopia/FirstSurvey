# coding: utf-8
from django.conf.urls import url
from . import views

from .forms import SignupForm

urlpatterns = [
    # host/ 로 접속하면 로그인 화면을 보여준다. login view와 연결
    url(r'^$', 'django.contrib.auth.views.login', name='login', kwargs={
        'template_name': 'first/login.html'}),
    url(r'^login$', 'django.contrib.auth.views.login', name='login', kwargs={
        'template_name': 'first/login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
    
    # 로그인 하면 설문조사 안내 페이지를 출력한다.
    url(r'^guide$', views.guide, name='guide'),
    
    # 회원 가입
    url(r'^signup$', views.signup, name='signup'),
    
    # 회원 가입
    url(r'^contact$', views.contact, name='contact'),
    
    # 필터링 선호 수집
    url(r'^filtering$', views.filtering, name='filtering'),
    
    # 설문 시작
    url(r'^survey$', views.survey, name='survey'),
    ]