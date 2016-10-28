# coding: utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .forms import SignupForm, FilteringForm, SurveyForm
from .models import SUser, Filtering, Group, ShotInfo, Clist, Survey

def signup(request):
    signupform = SignupForm()
    if request.method == "POST":
        signupform = SignupForm(request.POST, request.FILES)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.id = signupform.cleaned_data['sUserID']
            
            try:
                temp = Group.objects.get(phone = user.phone.replace('-', ''))   
                user.group = temp.group 
                user.save()
                
            except Group.DoesNotExist:
                user.group = 1
                user.save()
                
 
            return redirect('login')
 
    return render(request, "first/signup.html", {"signupform": signupform})

def contact(request):
    return render(request, "first/contact.html",)

@login_required
def guide(request):
    if request.method == "POST":
        if request.session.has_key('currentShot') == False :
            ID = request.session.get("_auth_user_id")
            sUser = SUser.objects.get(sUserID = ID)
            currentShot = sUser.currentShot
            
            if currentShot == None:
                currentShot = 0
                sUser.currentShot = currentShot
                sUser.save()
                
            request.session["currentShot"] = currentShot
                
        return redirect("/survey")

    # get            
    else:
        ID = request.session.get("_auth_user_id")
        try:
            filtering = Filtering.objects.get(sUserID_id = ID)
            return render(request, "first/guide.html")
        
        except Filtering.DoesNotExist:
            filteringform = FilteringForm()
            return redirect("/filtering")
        
@login_required        
def filtering(request):
    if request.method == "POST":
        filteringform = FilteringForm(request.POST, request.FILES)
        
        if filteringform.is_valid():
            filtering = filteringform.save(commit=False)
            filtering.sUserID = SUser.objects.get(sUserID = request.session.get("_auth_user_id"))
            filtering.save()
 
            return redirect("/guide")
    else:
        filteringform = FilteringForm()
        return render(request, "first/filtering.html",  {"filteringform": filteringform})

@login_required    
def survey(request):
    if request.method == "POST":
        if request.session.has_key('_auth_user_id'):
            surveyForm = SurveyForm(request.POST, request.FILES)
            if surveyForm.is_valid():
                survey = surveyForm.save(commit=False)
                sUser = SUser.objects.get(sUserID = request.session.get("_auth_user_id"))
                sUser.currentShot = survey.shotID
                survey.sUserID_id = sUser.sUserID
                survey.save()
                sUser.save()
                
                if request.POST.get('Islast') == 'true':
                    currentShot = int(sUser.currentShot) + int(sUser.group)
                    
                    if currentShot > 1894 and currentShot < 1908:
                        currentShot = 1908
                    if currentShot > 9581:
                        return render(request, "first/complete.html",)
                        
                    shot = ShotInfo.objects.get(ShotID = currentShot)
                    video = Clist.objects.get(CID = shot.CID_id)
                                        
                    shotList = ShotInfo.objects.extra(where = ["CID_id = '" + str(video.CID) + "' AND shotID >= " + str(currentShot)])
                    
                    surveyList = []
                    startTimeList = []
                    endTimeList = []
                    totalShot = ShotInfo.objects.all().aggregate(Max('ShotID')).get('ShotID__max')
                    
                    for i in range(0, len(shotList), int(sUser.group)):
                        surveyList.append(shotList[i].ShotID)
                        mid = ((shotList[i].StartFrame / video.FPS) + (shotList[i].EndFrame / video.FPS)) / 2
                        dif = ((shotList[i].EndFrame / video.FPS) - (shotList[i].StartFrame / video.FPS)) / 4
                        startTimeList.append(mid - dif)
                        endTimeList.append(mid + dif)
                    videoURL = "/static/first/video/" + video.VideoFileName
                    
                    # currentShot
                    cid = shot.CID_id
                    filename = video.ProgramNameKor
                    
                    surveyForm = SurveyForm()
                    
                    return render(request, "first/survey.html", {"surveyForm" : surveyForm,
                                                                 "startTime"  : startTimeList,
                                                                 "endTime"    : endTimeList,
                                                                 "videoURL"   : videoURL,
                                                                 "currentShot": surveyList,
                                                                 "cid"        : cid,
                                                                 "filename"   : filename,
                                                                 "totalShot"  : totalShot})
                    
    else:
        if request.session.has_key('_auth_user_id'):
            ID = request.session.get("_auth_user_id")
            sUser = SUser.objects.get(sUserID = ID)
            currentShot = int(sUser.currentShot)
            if(currentShot == 0):
                currentShot = 1
            else:
                currentShot += int(sUser.group)
                
            if currentShot > 1894 and currentShot < 1908:
                currentShot = 1908
            if currentShot > 9581:
                return render(request, "first/complete.html",)
                
            shot = ShotInfo.objects.get(ShotID = currentShot)
            video = Clist.objects.get(CID = shot.CID_id)
            
            shotList = ShotInfo.objects.extra(where = ["CID_id = '" + str(video.CID) + "' AND shotID >= " + str(currentShot)])
            
            surveyList = []
            startTimeList = []
            endTimeList = []
            totalShot = ShotInfo.objects.all().aggregate(Max('ShotID')).get('ShotID__max')
            
            for i in range(0, len(shotList), int(sUser.group)):
                surveyList.append(shotList[i].ShotID)
                mid = ((shotList[i].StartFrame / video.FPS) + (shotList[i].EndFrame / video.FPS)) / 2
                dif = ((shotList[i].EndFrame / video.FPS) - (shotList[i].StartFrame / video.FPS)) / 4
                startTimeList.append(mid - dif)
                endTimeList.append(mid + dif)

            videoURL = "/static/first/video/" + video.VideoFileName
            
            # currentShot
            cid = shot.CID_id
            filename = video.ProgramNameKor

            surveyForm = SurveyForm()
            return render(request, "first/survey.html", {"surveyForm" : surveyForm,
                                                         "startTime"  : startTimeList,
                                                         "endTime"    : endTimeList,
                                                         "videoURL"   : videoURL,
                                                         "currentShot": surveyList,
                                                         "cid"        : cid,
                                                         "filename"   : filename,
                                                         "totalShot"  : totalShot})     