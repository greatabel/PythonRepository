from azure.servicebus import ServiceBusService, Message

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %s" % (attr, getattr(obj, attr)))
    
bus_service = ServiceBusService(
    service_namespace='lumi001',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='AFOA06OWcNUsDQyi8jHuqIhumuV5QN+jObsfv5QhNBM=',
    host_base='.servicebus.chinacloudapi.cn')

# bus_service.create_queue('taskqueue')
msg = Message(b'Test Message')
# print('test')
# bus_service.send_queue_message('wechat.subscription.exp', msg)
message = bus_service.receive_queue_message('wechat.subscription.exp')
print(message,dump(message))


