from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

# 関数ベースビューの場合、HTMLから渡ってきた値が、urlpatternsで解析され、変数へ格納される
# urlpatternsで指定された変数名をそのまま関数ベースビューの引数として受け取ることができる
def room(request, room_name):
    return render(request, 'chat/room.html', {
        # 左側がHTMLで使う変数, 右側が変数
        'room_name': room_name
    })