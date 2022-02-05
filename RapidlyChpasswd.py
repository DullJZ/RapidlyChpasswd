'''
快速改密码python脚本
请用python3运行
需要安装paramiko库
命令：pip install paramiko
失联等不负责任！
'''
import paramiko
import random


def main(tmp):
    ssh_ip = tmp[0]
    ssh_passwd = tmp[1]

    # 创建一个ssh的客户端，用来连接服务器
    ssh = paramiko.SSHClient()
    # 创建一个ssh的白名单
    know_host = paramiko.AutoAddPolicy()
    # 加载创建的白名单
    ssh.set_missing_host_key_policy(know_host)
    # 输出有关信息
    print('\nIP: ' + ssh_ip)
    print('password: ' + ssh_passwd)
    # 连接服务器
    ssh.connect(hostname=ssh_ip, port=22, username="root", password=ssh_passwd)
    # 生成随机密码
    alphabet = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
    new_passwd = ""
    for i in range(10):
        new_passwd += random.choice(alphabet)
    print('\n新密码：' + new_passwd + '\n')
    s = [r'echo "root:{t}" | chpasswd'.format(t=new_passwd)]
    print(s[0])
    # 是否重启
    input_reboot_or_not = input('\n是否重启？（默认是）(y/n)')
    if input_reboot_or_not == 'y' or input_reboot_or_not == '':
        print('更改密码后将重启')
        s.append('reboot')

    # 执行命令
    for i in s:
        stdin, stdout, stderr = ssh.exec_command(i)
        # stdin  标准格式的输入，是一个写权限的文件对象
        # stdout 标准格式的输出，是一个读权限的文件对象
        # stderr 标准格式的错误，是一个写权限的文件对象

        print(stdout.read().decode())

    ssh.close()


tmp = []
tmp.append(input('输入IP：'))
tmp.append(input('输入root账户密码：'))
main(tmp)