from translate import Translator


city = "China"
translator = Translator(from_lang="en", to_lang="zh-CN")
city = translator.translate(city)

print(city)