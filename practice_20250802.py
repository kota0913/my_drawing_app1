import PySimpleGUI as sg

layout=[[sg.Button("OK")]]
window=sg.Window("sample",layout)

while True:
    event,values=window.read() #イベントを受け取る
    if event==sg.WINDOW_CLOSED:
        break
    if event=="OK":  #どのボタンが押されたか判定
        print("OKボタンが押されました")
        print(values)


window.close()

#event: ユーザーが起こしたイベント（例：ボタン名、ウィンドウを閉じた、など）

#values: 入力欄などに入力された値の辞書（フォームの内容など）
