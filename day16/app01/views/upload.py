from django.shortcuts import render,HttpResponse
import os

def upload_list(request):
    if request.method=='GET':
        return render(request,'upload_list.html')
    # print(request.POST)
    # print(request.FILES)
    file_object=request.FILES.get('avatar')
    with open(file_object.name,mode='wb') as f:
        for chunk in file_object.chunks():
            f.write(chunk)
    return HttpResponse('...')


from django import forms
from app01.utils.bootstrap import BootStrapForm
from app01 import models

class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']
    name=forms.CharField(label='姓名')
    age=forms.IntegerField(label='年龄')
    img=forms.FileField(label='头像')

def upload_form(request):
    title='Form上传'
    if request.method=='GET':
        form=UpForm()
        return render(request,'upload_form.html',{'form':form,'title':title})
    form=UpForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        image_object=form.cleaned_data.get('img')
        from django.conf import settings

        media_path=os.path.join('media',image_object.name)
        with open(media_path,mode='wb') as f:
            for chunk in image_object.chunks():
                f.write(chunk)
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            img=media_path,
        )
        return HttpResponse('...')
    return render(request,'upload_form.html',{'form':form,'title':title})

from app01.utils.bootstrap import BootStrapModelForm
class UpModeForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model=models.City
        fields='__all__'
def upload_modelform(request):
    title='ModelForm上传文件'
    if request.method=='GET':
        form=UpModeForm()
        return render(request,'upload_form.html',{'form':form,'title':title})
    form=UpModeForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('上传成功')
    return render(request, 'upload_form.html', {'form': form, 'title': title})