# coding: utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.images import get_image_dimensions
 
from .models import SUser, Filtering, Survey
 
class SignupForm(UserCreationForm):
    sUserID = forms.CharField(
        label="아이디  ",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label="이름  ",
        max_length=30,                     
        widget=forms.TextInput(
            attrs={  
                'class': 'form-control',
                'placeholder': '이름',
                'required': 'true',
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호  ',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="비밀번호 확인  ",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인',
                'required': 'True',
            }
        )
    )
    birthday = forms.DateField(
        label="생년월일  ",
        input_formats=
            ['%Y-%m-%d',
             '%Y/%m/%d',
             ],
        widget=forms.DateInput(
            attrs={
                'required': 'True',
                'readonly': 'True',
                'style': "background-image:url('/static/first/images/calendar1.png'); background-repeat: no-repeat; background-position: center;",
                'onselect' : 'focusCalendar()',
                }
        )
    )
    SEX = [
        ('M','남자'),
        ('F','여자')
    ]
    sex = forms.ChoiceField(
        label = "성별  ",
        choices = SEX,
        widget = forms.RadioSelect()
    )
    phone = forms.CharField(
        label="핸드폰  ",
        max_length=20,                     
        widget=forms.TextInput(
            attrs={  
                'class': 'form-control',
                'placeholder': '010-0000-0000',
                'required': 'true',
                'onselect' : 'focusPhone()',
                'onclick' : 'focusPhone()',
            }
        )
    )
    MARRIED = [
        ('T','기혼'),
        ('F','미혼')
    ]
    married = forms.ChoiceField(
        label = "결혼 여부  ",
        choices = MARRIED,
        widget = forms.RadioSelect()
    )
    CHILDREN = [
        ('T','자녀 있음'),
        ('F','자녀 없음')
    ]
    children = forms.ChoiceField(
        label = "자녀 유무  ",
        choices = CHILDREN,
        widget = forms.RadioSelect()
    )
    job = forms.CharField(
        label = "직업  ",
        max_length=30,                     
        widget=forms.TextInput(
            attrs={  
                'class': 'form-control',
                'placeholder': '직업',
                'required': 'true',
            }
        )
    )
    company = forms.CharField(
        label = "직장  ",
        max_length=30,                     
        widget=forms.TextInput(
            attrs={  
                'class': 'form-control',
                'placeholder': '직장',
                'required': 'true',
            }
        )
    )
    hobby = forms.CharField(
        label = "취미  ",
        max_length=30,                     
        widget=forms.TextInput(
            attrs={  
                'class': 'form-control',
                'placeholder': '취미',
                'required': 'true',
            }
        )
    )

    class Meta: # SignupForm에 대한 기술서
        model = SUser
        fields = ("sUserID", "name", "password1", "password2",
                  "birthday", "sex", "phone", "married", "children",
                  "job", "company", "hobby") # 작성한 필드만큼 화면에 보여짐
 
class LoginForm(AuthenticationForm):
    sUserID = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'sUserID',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    
class FilteringForm(forms.ModelForm):
    SP = [
        ('Youtube','Youtube'),
        ('Facebook','Facebook'),
        ('Instagram','Instagram'),
        ('Naver TV캐스트','Naver TV캐스트'),
        ('Daum TV팟','Daum TV팟'),
        ('afreeca TV','afreeca TV'),
        ('기타','기타'),        
    ]
    serviceProvider = forms.ChoiceField(
        label = "좋아하는 사이트",
        choices = SP,
        widget = forms.Select()
    )
    DEGREE = [
        ('청소년관람불가','청소년관람불가'),
        ('15세 이상 관람가','15세 이상 관람가'),
        ('12세 이상 관람가','12세 이상 관람가'),
        ('전체관람가','전체관람가'),       
    ]
    degree = forms.ChoiceField(
        label = "시청 등급",
        choices = DEGREE,
        widget = forms.Select()
    )
    PRICE = [
        ('무료','무료'),
        ('1,000원 이하','1,000원 이하'),     
        ('5,000원 이하','5,000원 이하'),
        ('10,000원 이상','10,000원 이상'),  
    ]
    price = forms.ChoiceField(
        label = "시청 가격",
        choices = PRICE,
        widget = forms.Select()
    )
    
    class Meta:
        model = Filtering
        fields = ("serviceProvider", "degree", "price") # 작성한 필드만큼 화면에 보여짐
        
class SurveyForm(forms.ModelForm):
    PREFERENCE = [
        ('0',''),
        ('1',''),
        ('2',''),
        ('3',''),
        ('4',''),
        ('5',''),
        ('6',''),
        ('7',''),  
        ('8',''),
        ('9',''),
        ('10',''),       
    ]
    preference = forms.ChoiceField(
        label = "선호도",
        choices = PREFERENCE,
        widget = forms.RadioSelect()
    )
    reason = forms.CharField(
        max_length=254,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '색조, 화질, 영상길이 등 마음에 들거나 그렇지 않은 이유를 써주세요.',
                'required': 'True',
                'style': 'resize:none;',
            }
        )
    )
    cID = forms.CharField(
            widget = forms.HiddenInput()
        )
    shotID = forms.CharField(
            widget = forms.HiddenInput()
        )
    fileName = forms.CharField(
            widget = forms.HiddenInput()
        )
    
    class Meta:
        model = Survey
        fields = ("preference", "reason", "cID", "shotID", "fileName") # 작성한 필드만큼 화면에 보여짐