from wsgiref.simple_server import make_server
from urllib.parse import  parse_qs

def login(environ):
    with open("login.html","rb") as f:
        data = f.read()
    return data


def auth(environ):
    request_body_size = int(environ.get('CONTENT_LENGTH',0))
    print("request_body_size",request_body_size)
    request_body = environ['wsgi.input'].read(request_body_size)
    request_data = parse_qs(request_body)
    user = request_data.get(b"user")[0].decode('utf8')
    pwd = request_data.get((b"pwd"))[0].decode('utf8')
    print("====>",user,pwd)
   
    #2 去数据库校验，查看提交用户是否合法
    import pymysql
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        database='web',
        port=3306,
        unix_socket=None,
        charset='utf8'
    )
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from userinfo where name=%s and password=%s"
    cur.execute(sql,[user,pwd])
    # print("cur.fetchone:",cur.fetchone())
    if cur.fetchone():
        data = "验证成功".encode('gbk')
    else:
        data = "验证失败".encode('gbk')
        
    return data

def application(environ, start_response):
    """
    environ : 请求信息字典
    start_response : 封装响应格式
    """
    # print("environ:",environ)
    # print("start_response",environ.get("PATH_INFO"))
    path = environ.get("PATH_INFO")
    data = b'404'
    if path == "/login":
        data = login(environ)
    elif path == "/auth":
        #登录认证
        #1 获取用户输入得用户名密码
        data = auth(environ)
        #3 响应返回
    start_response('200 OK',[('Content-Type','text/html')])
    return [data]

http = make_server('',8080,application)
print('Serving HTTP on port 8080...')

http.serve_forever()























