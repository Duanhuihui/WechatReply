import apiutil  # 这里我上端代码独立生成一个文件“apiutil.py"，所以要导入一下
import json
import itchat
import  requests
app_key = 'P3RcAydvZ8FYCDjR'
app_id = '2118092607'
#questionS = '我想你了'
url= 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
#登录微信
itchat.auto_login(hotReload=True)
#接收好友消息并回复
def anso(message):
    str_question = message
    session = 10000
    ai_obj = apiutil.AiPlat(app_id, app_key)

    rsp = ai_obj.getNlpTextChat(session, str_question)
    if rsp['ret'] == 0:
        print('............................................................')
        ask = (rsp['data'])['answer']
        print(ask)
        return ask
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))

#回复给微信好友
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    defaultReply="我知道了"
    #搜索好友
    realFriend= itchat.search_friends(name='曹佳旋')
    #研究群消息自动回复
    realFriendsName=realFriend[0]['UserName']
    #微信好友回复内容
    print("message:%s"%msg['Text'])

    ask= anso(msg['Text'])
    if msg['FromUserName'] == realFriendsName:
        itchat.send(ask,toUserName=realFriendsName)

if __name__ == '__main__':
    anso(message=auto_reply)
itchat.run()
#注释



