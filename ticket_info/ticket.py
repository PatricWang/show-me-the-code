#coding:utf-8
"""
Usage:
tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help
    -g
    -d
    -t
    -k
    -z
"""

# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

# from docopt import docopt
import re
import requests
from pprint import pprint


def cli():
    # arguments = docopt(__doc__)
    # ss = '成都'.decode('gbk')
    # from_station = stations.get(arguments['<from>'].decode('gbk'), )
    # to_station = stations.get(arguments['<to>'].decode('gbk'))

    stations = parse_station()
    usr_input = input("input start station, terminal station, date\n")
    argu_list = usr_input.split('，')
    print(usr_input)
    print(argu_list)
    from_station, to_station, date = argu_list[0], argu_list[1], argu_list[2]

    from_station = stations.get(from_station)
    to_station = stations.get(to_station)
    # date = arguments['<date>']

    # from_station = 'AOH'
    # to_station = 'AOH'
    # date = '2018-02-15'

    print(from_station, to_station)
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
    # url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-14&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=NCG&purpose_codes=ADULT'
    print(url)
    r = requests.get(url, verify=False)
    train_dict = r.json()
    one_train = train_dict['data']['result'][4]
    raw_train_info = train_dict['data']['result']
    # for info in train_info:
    #     info.split('|')
    train_info = [info.split('|') for info in raw_train_info]
    no = 1
    for i in one_train.split('|'):
        print('[%s]: %s' % (no, i))
        no += 1
    print(r.json()['data']['result'][0])



def parse_station():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9044'
    response = requests.get(url,verify=False)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    sta_dict = dict(stations)
    # pprint(dict(stations))
    return dict(stations)



def recv_argu():
    usr_input = input("input start station, terminal station, date\n")
    argu_list = usr_input.split(',')
    print(usr_input)
    print(argu_list)
    return

if __name__ == '__main__':
    # parse_station()
    cli()
    # recv_argu()