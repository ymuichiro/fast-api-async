# 非同期処理を全体として workers が 1, 接続保持数を Max 3000, timeout を 60秒とした場合
# 注意: 3001 以上の保持数を設定しても最小構成では 500 となった為、別の設定値、または限界がある想定
# FastAPI の endpoint が async def である場合、シングルスレッドとして動作
# ただしデフォルト値は同時接続 >2000 であり、ここから増えていく際には LB で振り分けした方が良さげ
# 2500 近辺の同時接続は不安定で 500 となるケースもあり
uvicorn main:app --workers 1 --backlog 3000 --limit-concurrency 3000 --timeout-keep-alive 60