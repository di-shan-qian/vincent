import json
import os
import urllib.request


def tv_spider(url, a, z):
    for i in range(a, z):
        page = i
        my_url = url + str(page) + "/10.json"
        save_page(my_url)
    # os.system("shutdown -s -t  60 ")
    # print("OK")

def save_page(u):
    name = u[u.rfind("105196402/162/") + 14: u.rfind("/10.json")]

    urllib.request.urlretrieve(u, './' + name + '.txt')
    txt_to_dic(name)


def txt_to_dic(txt_name):
    file = open(txt_name + '.txt', 'r', encoding='UTF-8')
    js = file.read()
    dic = json.loads(js)
    file.close()

    for i in range(0, 10):
        new_dic = {
            'id': dic['data']['data'][i]['id'],
            'title': dic['data']['data'][i]['title'],
            'M3U8': dic['data']['data'][i]['playUrl']
        }
        MV_name = new_dic['id'] + '-' + new_dic['title'] + '.mp4'
        print (MV_name)
        os.system('ffmpeg -i "' + new_dic['M3U8'] + '" -c copy ' + MV_name)
        #print(new_dic['M3U8'])

def dl_4_id(ID):

    idurl='https://www.zhanqi.tv/v2/videos/'+ID+'.html?from=roomVideo'
    #http://dlvod.cdn.zhanqi.tv/869972-YzA2ODZmN2FmZWI0MDFmNzBiYjFiN2M2YzNiYjdiNDg.m3u8
    res=urllib.request.urlopen(idurl)
    html=res.read().decode('utf-8')
    h=str(html)
    u=h.rfind(ID+'-')
    #print(h[u:h.rfind('.m3u8',u,u+99)])
    newurl='http://dlvod.cdn.zhanqi.tv/'+h[u:h.rfind('.m3u8',u,u+99)]+'.m3u8'
    #print(newurl)
    os.system('ffmpeg -i "' + newurl + '" -c copy ' + ID+'.mp4')


if __name__ == '__main__':

    op=input('1:批量下载\n2:单独下载\n')
    if op == '1':

        url ="https://www.zhanqi.tv/api/static/v2.2/video/recommend/105196402/162/"
        a_page=int(input('请输入起始页码：'))
        z_page=int(input('请输入终止页码：'))
        tv_spider(url,a_page,z_page+1)
    else:
        id=input('请输入ID：\n')
        dl_4_id(str(id))
