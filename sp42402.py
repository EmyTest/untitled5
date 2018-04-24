from urllib import  request
if __name__ =='__main__':
    url = "http://www.renren.com/965187997/profile"
    headers = {
        "Cookie":"anonymid=jgd497hooudrd6; depovince=GW; _r01_=1; JSESSIONID=abcm7A4Jyo1ZS9mwYT1lw; jebe_key=c4ea4a7f-fec4-4583-8dd1-7e8338f9b4e0%7Cedc35e4843a227ccaf07ccba7d5e6050%7C1524548669060%7C1%7C1524548822846; ick_login=aa99726d-6385-4707-8db1-5ed2c0a4e854; t=83c9c70923796faed38949b7ff7646209; societyguester=83c9c70923796faed38949b7ff7646209; id=965539999; xnsid=9ce747e; jebecookies=b6b7345f-db17-4edc-b7a4-0613bea1341d|||||; ch_id=10016; wp_fold=0"
    }

    # rsp = request.Request(url,headers=headers)
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    with open("rsp.html","w") as f:
        f.write(html)
