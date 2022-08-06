from django.shortcuts import render,HttpResponse,redirect
from app01 import models
def city_list(request):
    queryset=models.City.objects.all()
    return render(request,'city_list.html',{'queryset':queryset})


from app01.utils.bootstrap import BootStrapModelForm
class UpModeForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model=models.City
        fields='__all__'
def city_add(request):
    title='新建城市'
    if request.method=='GET':
        form=UpModeForm()
        return render(request,'upload_form.html',{'form':form,'title':title})
    form=UpModeForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/city/list/')
    return render(request, 'upload_form.html', {'form': form, 'title': title})