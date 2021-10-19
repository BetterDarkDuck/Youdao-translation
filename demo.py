import youdaofanyi

sentences = input('请输入要翻译的内容（5000字以内容，自动检测语言）：')
youdao = youdaofanyi.YouDao(sentences)
print(youdao.translation())