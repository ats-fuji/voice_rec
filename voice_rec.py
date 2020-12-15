import subprocess
import socket

class voice_rec():

    def __init__(self,# 以下は変更が必要なら引数で渡すこと
                 host = '127.0.0.1',# ソケット通信のIPアドレス
                 port = 10500,      # ソケット通信のポート番号
                 main_path = '../julius/julius-kit/dictation-kit-v4.4/main.jconf',    # main.jconfのパス
                 dict_path = '../julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf'): # am-gmm.jconfのパス
        # Juliusモジュールモード起動
        subprocess.Popen(['julius','-C',main_path,'-C',dict_path,'-module'])

        # ソケット生成
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # Juliusソケット通信の接続確認変数 True:接続中 / False:未接続
        connect = False

        while True:
            # Juliusサーバーにソケット通信接続（未接続時）
            while connect == False:
                try:
                        # 接続処理
                    client.connect((host, port))
                    connect = True

                    # ソケット通信接続エラー（Juliusサーバーの起動中）
                except ConnectionRefusedError:
                     pass

            # 音声認識データ格納変数
            data = ""

            # 音声認識データなし → 音声認識データを受け取るまでデータ受信
            while '</RECOGOUT>\n.' not in data:
                data += str(client.recv(1024).decode('utf-8'))

            # 認識文字列格納変数
            self.word = ""

            # 認識結果を1行ずつに分割 → 認識文字列の記載部分を1行ずつ検索
            for line in data.split('\n'):
                # 認識文字列が記載された行か確認
                indexWord = line.find('WORD=')

                # 認識文字列が記載された行のとき
                if indexWord != -1:
                    # 認識文字列を検索 → 変数に格納
                    line = line[indexWord+6:line.find('"',indexWord+6)]
                    self.word = self.word + line
            #↓デバッグ用↓（認識した言葉をターミナルに表示する）
            #print(self.word)
