import threading
import datetime
import time

DETAILED_VAPPS = {}
vapp_names = ['vapp1', 'vapp2', 'vapp3']
dd = {'key1': 'value1', 'key2': 'value2'}


def get_vapp_info(vapp_name):
    delay_between_calls_sec = 3
    calls_timeout_sec = 3 * 5
    total_attempts_number = calls_timeout_sec // delay_between_calls_sec
    current_attempt = 0

    res = ''
    while current_attempt < total_attempts_number:
        current_attempt += 1
        time.sleep(delay_between_calls_sec)
        res = res + ' ' + str(current_attempt)

    res = res + ' ' + vapp_name + '_' + str(datetime.datetime.now().time())
    print(vapp_name + '_' + 'thread\n')
    DETAILED_VAPPS[vapp_name] = res


print('----')
print(dd.get('key2'))
print(dd.get('key3', []))
print('----')

threads = []
print('started at ', str(datetime.datetime.now().time()))
for vapp_name in vapp_names:
    detailer = threading.Thread(
        target=get_vapp_info,
        args=(vapp_name,))
    threads.append(detailer)
    detailer.start()

for t in threads:
    t.join()

print('ended at ', str(datetime.datetime.now().time()))
print(DETAILED_VAPPS)
