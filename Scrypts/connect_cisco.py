import netmiko
import click


def connect_ssh(ip):
    device = {'device_type':'cisco_ios',
    'ip':ip,
    'username':'admin',
    'password':'admin',
    'secret':''
    }
    return netmiko.ConnectHandler(**device)


@click.command()
@click.option('--ip')
def main(ip):
    print(connect_ssh(ip).send_command('sh ip int br'))
    # return connect_ssh(ip)

if __name__=='__main__':
    main()
