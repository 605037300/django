import os
from django.core.mail import send_mail,EmailMultiAlternatives

os.environ["DJANGO_SETTINGS_MODULE"]='django_afx.settings'

if __name__=="__main__":
    # send_mail(
    #     '来自www.liujiangblog.com的测试邮件',
    #     '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！',
    #     'byjdh@qq.com',
    #     ['byjdh@qq.com'],
    # )

    subject,from_count,to_count='来自www.liujiangblog.com的测试邮件', 'byjdh@qq.com', '605037300@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg=EmailMultiAlternatives(subject,text_content,from_count,[to_count])
    msg.attach_alternative(html_content,"text/html")
    msg.send()