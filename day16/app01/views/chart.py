from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    """数据统计页面"""
    return render(request,'chart_list.html')

def chart_bar(request):
    """构造柱状图的数据"""
    legend=["杨承科","叶萍"]
    series_list= [
                    {
                        "name": '杨承科',
                        "type": 'bar',
                        "data": [5, 20, 36, 10, 10, 20]
                    },
                    {
                        "name": '叶萍',
                        "type": 'bar',
                        "data": [15, 30, 26, 20, 70, 30]
                    }
                ]
    x_axis= ['1月', '2月', '3月', '4月', '5月', '6月']
    result={
        "status":True,
        "data":{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis,
        }
    }
    return JsonResponse(result)

def chart_pie(request):
    """构造饼图的数据"""
    db_data_list=[
        {"value": 1048, "name": 'IT部门'},
        {"value": 735, "name": '运营部门'},
        {"value": 580, "name": '新媒体部门'},
    ]
    result={
        "status":True,
        "data":db_data_list,
    }
    return JsonResponse(result)