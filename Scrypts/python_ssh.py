import yaml
from pathlib import Path
from netmiko import ConnectHandler
from pprint import pprint

COMMAND_LIST = [
    'sh clock',
    'sh ip route static',
    'sh ip int br'
]


def read_yaml():
    with open(Path('../Files/inventory.yml')) as f:
        content = yaml.load(f.read())
    return content


def connection_from_yaml(parsed_yaml):
    global_params = parsed_yaml['all']['vars']
    all_host_dict = parsed_yaml['all']['groups']['main']
    result = {}
    for host in all_host_dict['hosts']:
        host_dict = {}
        hostname = host.pop('hostname')
        host_dict.update(global_params)
        host_dict.update(host)
        result[hostname] = host_dict
    return result

def collect_outputs(devices, commands=COMMAND_LIST):
    answers = {}
    for hostname, params in devices.items():
        ssh = ConnectHandler(**params)
        answers[hostname] = {}
        for command in COMMAND_LIST:
            answers[hostname][command] = ssh.send_command(command)
        ssh.disconnect()
    return answers


def print_result(output):
    for host, answers in output.items():
        print (f'{"*"*40} {host} {"*"*40}')
        for command, answer in answers.items():
            print (f'{"="*40} {command} {"="*40}')
            print(answer)
        print('*'*80, '\n\n')


def main():
    content = read_yaml()
    hosts = connection_from_yaml(content)
    result = collect_outputs(hosts)
    print_result(result)

if __name__ == '__main__':
    main()
