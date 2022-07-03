# Django-Channels-sample

ChannelsチュートリアルのChapter2までのサンプルソースです。
ChannelLayerを有効化すると、複数のブラウザからの書き込みが行えますが、
今回はその部分は不要なので実装してません。
クライアント側のWebSocketの送り方のイメージの参考にして下さい。

* Venvアクティベート
<pre>
cd django-channnels-sample
source venv/bin/activate
</pre> 

* サーバー起動
<pre>
cd mysite
python3 manage.py runserver
</pre>

* ブラウザで下記へアクセス
<pre>
http://127.0.0.1:8000/chat
</pre>
