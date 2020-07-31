# 正方形を表すクラス
# Rectangleクラスの派生クラスとして作成する
import sys,os
sys.path.append(os.path.dirname(__file__))
from rectangle import Rectangle
'''
`__file__は、実行スクリプトのファイルを表す。
1) スクリプトファイルを相対パスで実行した時は、相対パスを返す。
2) スクリプトファイルを絶対パスで実行した時、または、他のスクリプトからインポートされたときは、絶対パスを返す
'''

class Square(Rectangle):
    def __init__(self, edge):
        super().__init__(edge, edge)


if __name__ == '__main__':
    s = Square(10)
    print('area:' + str(s.area()))

