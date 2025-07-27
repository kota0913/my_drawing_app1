import PySimpleGUI as sg

layout=[[
    sg.Canvas(
        size=(400,400),#キャンバスの大きさ
        key="canvas", #"キャンバスを後で操作するための識別名
        background_color="White"
    )
]]
window=sg.Window("キャンバスのテスト",layout) #ウィンドウの作成、タイトルバーに表示するタイトル
painted=False #描画したかどうかのフラグ。最初はまだ描いていないので False。

while True:
    event,_=window.read(timeout=10)  #eventにはボタンのクリックなどのイベントが入る
    if event==sg.WINDOW_CLOSED:      
        break
    if not painted:
        painted=True
        #描画用のウィジェットを取得
        widget=window["canvas"].Widget
        #長方形を描画
        widget.create_rectangle(10,10,300,300,fill="yellow")
        #円を描画
        widget.create_oval(50,50,350,350,fill="blue")
        #線を描画
        widget.create_line(10,10,390,390,fill="red",width=10)
window.close()