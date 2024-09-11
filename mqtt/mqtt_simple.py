import json, sys, time, os
import paho.mqtt.client as mqtt
from threading import Thread

ACCESS_TOKEN='izmgrkbcskpjbmd7'
PROJECT_KEY='ARN2eaUkit'
HOST='sh-1-mqtt.iot-api.com'
subscribe_topic = "attributes/push" 
publish_topic = "attributes"
SSID = '"szyyw"'
PWD = '"szyywdz501"'

# 建立mqtt连接
def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connection successful")
    elif rc == 1:
        print("Protocol version error")
    elif rc == 2:
        print("Invalid client identity")
    elif rc == 3:
        print("server unavailable")
    elif rc == 4:
        print("Wrong user name or password")
    elif rc == 5:
        print("unaccredited")
    print("Connect with the result code " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    json_msg = json.loads(msg.payload.decode('utf-8'))
    pass

def on_publish(client, obj, mid):
    print("on_Publish, mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("on_Subscribed: " + str(mid) + " " + str(granted_qos))

def on_unsubscribe(client, userdata, mid):
    print("on_unsubscribe, mid: " + str(mid))

def on_log(client, obj, level, string):
    print("on_Log:" + string)

def mqtt_subscribe():
    global client
    client.loop_forever()

def mqtt_publish(sensor_data, topic=publish_topic, qos=1):
    global client
    try:
        client.publish(topic=topic, payload=sensor_data, qos=qos)
    except KeyboardInterrupt:
        print("exit")
        client.disconnect()
        sys.exit(0)
    time.sleep(2)

client = mqtt.Client()
message = '{"version":"2.0.0"}'

def mqtt_demo():
    client.username_pw_set(ACCESS_TOKEN, PROJECT_KEY)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_log = on_log
    client.connect(host=HOST, port=1883)
    client.reconnect_delay_set(min_delay=1, max_delay=2000)
    client.subscribe(subscribe_topic, qos=0)
    subscribe_thread = Thread(target=mqtt_subscribe)
    subscribe_thread.start()

def connect_wifi():
    with open('/etc/wpa_supplicant.conf', 'r') as f:
        lines = f.readlines()
        lines[3] = '  ssid=%s'%SSID + '\n'
        lines[4] = '  psk=%s'%PWD + '\n'
    with open('/etc/wpa_supplicant.conf', 'w') as f:
        f.writelines(lines)
    
    os.system('wpa_supplicant -D nl80211 -i wlan0 -c /etc/wpa_supplicant.conf -B')
    os.system('udhcpc -i wlan0')
    time.sleep(2)

if __name__ == "__main__":
    connect_wifi()
    mqtt_demo()
    mqtt_publish(message)
