
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic.base import View
from .models import Player

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        client = request.POST.get('client')
        score = request.POST.get('score')
        print(client)
        if not client:
            return HttpResponse('输入错误')
        if 0<int(score)<10000000:
            player = Player.objects.filter(clientid=client).first()
            if player:
                player.grade = score
                player.save()
            else:
                player = Player.objects.create(clientid=client,grade=score)
        else:
            return HttpResponse('您输入的分数有误')
        result = {'code':200,'msg':'提交成功'}
        return JsonResponse(result)

class RankView(View):
    def get(self,request,name,start,end):
        start = int(start)
        end = int(end)
        player = Player.objects.filter(clientid=name)
        player = player[0]
        print(player.clientid)
        if player:
            ranks = Player.objects.all().order_by('-grade')
            print(ranks)
            rankcount = ranks.count()
            ranklist = []
            index = start
            for rank in ranks[start-1:end]:
                ranklist.append({
                    'ranking':index,
                    "client":rank.clientid,
                    "score":rank.grade
                })
                index += 1
            # print(ranklist)
            player_ranking = 1
            for i in ranks:
                if i.clientid == player.clientid:
                    player_ranking_num = player_ranking
                player_ranking += 1
            context = {
                'rank_list':ranklist,
                'rank':player_ranking_num,
                'clientid':player.clientid,
                'score':player.grade
            }
            return render(request,'rank.html',context)

class FindView(View):
    def get(self,request):
        return render(request,'find.html')
    def post(self,request):
        ranks = Player.objects.all()
        rangcount = ranks.count()
        print(rangcount)
        client = request.POST.get('client')
        start = request.POST.get('start')
        end = request.POST.get('end')
        start = int(start)
        end = int(end)
        if start > rangcount or end > rangcount:
            return HttpResponse('总数量为{},输入有误,请重新输入'.format(rangcount))
        return HttpResponseRedirect('/chart/rank/{}/{}/{}'.format(client,start,end))
def find_server(request):
    if request.method == 'GET':
        result = {'code':200,'msg':'/chart/find'}
        return JsonResponse(result)
