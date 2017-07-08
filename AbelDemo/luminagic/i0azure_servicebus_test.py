from azure.servicebus import ServiceBusService, Message
import time

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %s" % (attr, getattr(obj, attr)))

bus_service = ServiceBusService(
    service_namespace='lumi001',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='AFOA06OWcNUsDQyi8jHuqIhumuV5QN+jObsfv5QhNBM=',
    host_base='.servicebus.chinacloudapi.cn')

queue_name = 'temp_queue'
# queue_name = 'wechat.subscription.exp'
# bus_service.create_queue('temp_queue')
for i in range(15):
    msg_str = 'Follow#oQ_DVvyaYU_iFEpJCI5WW9lLkvG4@%s' % (time.ctime(time.time()))
    if i % 2== 0:
            msg_str = 'UnFollow#oQ_DVvyaYU_iFEpJCI5WW9lLkvG4@%s' % (time.ctime(time.time()))
    msg = Message(str.encode(msg_str))
    print('push to queue: ',msg_str)
    bus_service.send_queue_message(queue_name, msg)
    time.sleep(1)

# time.sleep(1)
# # message = bus_service.receive_queue_message(queue_name)
# message = bus_service.receive_queue_message(queue_name)
# while 1:
#     message = bus_service.receive_queue_message(queue_name)
#     if message.body == None:
#         break
#     print(message.body == None)
#     print('receive--> message','#'*10,message.body)
#     # print(message,dump(message),'#'*10,message.body)
#     message.delete()


