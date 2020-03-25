import requests
import json


if __name__ == '__main__':

    # https://openweathermap.org/current
    api_adress = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

    appid = {Your AppID}

    city_name = "London,uk"

    # urlの生成, cityとkeyに各値を代入
    #url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={Your AppID}"
    url = api_adress.format(city=city_name, key=appid)

    # GETでリクエストを送信して、そのレスポンスを保存
    response = requests.get(url)

    # JSON文字列を辞書変換する
    data = json.loads(response.text)

    # 辞書dataから天気予報の情報を取り出す
    title = data["name"]
    weather_text = data["weather"][0]["description"]

    print(title)
    print(weather_text)
