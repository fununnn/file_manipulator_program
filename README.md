# さて、ファイルの読み書きとシェルの引数入力の取り方について学んだので、いよいよ File Manipulator というプロジェクトに取り組んでみましょう。以下のコマンドとその機能を提供する file_manipulator.py という Python スクリプトを作成してください。引数の入力が正しいかどうかをチェックするバリデータを必ず記述しましょう。
reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

# 要件定義
input.txtのファイルの内容を逆にしてoutput.txtに出力する関数
input.txtのコピーを作成し出力する関数
input.txtの内容を読み取り、複数回output.txtに出力する関数
input.txtの全てのneedleをnewstringに変換する関数
引数があっているかどうかのバリデータ関数
メインの動作を記載する関数
main()

# 疑似コード
class Filemanipulator:

def reverseFile():

def copyFile():

def pasteManyTimes():

def replaceString():

def validationArg():

def main():
    validationArg()
    if sys.argv(1) == reverse =>reverseFile() 
    if sys.argv(1) == copy =>copyFile()
    if sys.argv(1) == paste =>pasteManyTimes()
    if sys.argv(1) == replac =>replaceString() 
main()     
    