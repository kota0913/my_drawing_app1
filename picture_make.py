import io
from PIL import Image,ImageEnhance,ImageFilter
import PySimpleGUI as sg

def main():
    #対象画像ファイルの選択
    fname=sg.popup_get_file("画像ファイルを選択してください",no_window=True)
    if not fname:exit()
    #画像を処理してフィルター処理を開始
    show_image_editor(fname)

#画像エディターを表示する関数を定義
def show_image_editor(image_path):
    #画像を読み込む
    raw_img=Image.open(image_path)
    def_image=raw_img.resize((400,400))
    #レイアウト左側の定義
    col_left=[
        [sg.Image(convert_png(def_image),key="image")]
    ]
    #レイアウト右側を定義
    col_right=[
        [sg.Text("コントラスト")],
        [sg.Slider(key="contrast",
        range=(0,2),resolution=0.1,default_value=1,
        orientation="h",enable_events=True)
    ],
    [sg.Text("明るさ")],
    [sg.Slider(key="brightness",
               range=(0,10),resolution=0.1,default_value=1,
               orientation="h",enable_events=True)
               ],
               [sg.Text("ぼかし")],
               [sg.Slider(key="blur",
                          range=(0,10),resolution=1,default_value=0,
                          orientation="h",enable_events=True)
                          ]
    ]
    window=sg.Window("画像の表示",layout=[
    [
        sg.Column(col_left),
        sg.Column(col_right,vertical_alignment="top")
    ],
    [sg.Button("保存"),sg.Button("閉じる")]
    ])

    while True:
        event,values=window.read()
        if event==sg.WIN_CLOSED or event=="閉じる":
            break
    #スライダーを動かしたときの処理
        if event=="contrast" or \
           event=="brightness" or \
           event=="blur":
           f_img=filter_png(raw_img,values)
           bin=convert_png(f_img)
        #画像の更新
           window["image"].update(data=bin)
        save_fname = None #これ入れたら動いた
        if event=="保存":
        #ファイル選択
            save_fname=sg.popup_get_file(
            "保存するファイルを選んでください",
                save_as=True,no_window=True
        )
        if not save_fname:
            continue
        #画像を保存
        img2=filter_png(raw_img,values,False)
        img2.save(save_fname)
        sg.popup("保存しました")
    window.close()

#画像にフィルターをかける関数を定義
def filter_png(image,values,is_resize=True):
    #パラメータから値を取り出す
    contrast=values["contrast"]
    brightness=values["brightness"]
    blur=values["blur"]
    #フィルター処理を行う
    if blur>0:
        #ぼかし処理
        image=image.filter(ImageFilter.GaussianBlur(radius=blur))
    if is_resize:
        image=image.resize((400,400)) #画像サイズを変更 #image=のように戻り値を使う
        #コントラストと明るさを変更
    image=ImageEnhance.Contrast(image).enhance(contrast)
    image=ImageEnhance.Brightness(image).enhance(brightness)
    return image

#画像をPNG形式に変換
def convert_png(image):
    bin=io.BytesIO()
    image.save(bin,format="PNG")
    return bin.getvalue()

if __name__=="__main__":
    main()

#学び
#関数引数 image_path、生成ローカル変数 save_fname などで名前が衝突していないか
#UnboundLocalError: cannot access local variable 'save_fname' where it is not associated with a valueが出たときは変数に問題あり
#後半のfnameをsave_fnameに変更、初期値を設定することで解決

#FFmpegを導入、フォルダの解凍、powershellの見方、環境変数の設定を確認
#パスのコピーを変数設定のところに張り付けるが通らず。

