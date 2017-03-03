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

# bus_service.create_queue('taskqueue')
for i in range(5):
    msg_str = 'Test Message %s' % (time.ctime(time.time()))
    msg = Message(str.encode(msg_str))
    print('test',msg_str)
    bus_service.send_queue_message('wechat.subscription.exp', msg)
    time.sleep(1)

time.sleep(1)
# message = bus_service.receive_queue_message('wechat.subscription.exp')
while 1:
    message = bus_service.receive_queue_message('wechat.subscription.exp')
    if message.body == None:
        break
    print(message.body == None)
    print('receive--> message','#'*10,message.body)
    # print(message,dump(message),'#'*10,message.body)
    message.delete()


