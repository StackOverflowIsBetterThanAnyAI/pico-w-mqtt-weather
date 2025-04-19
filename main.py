import api
import connect
import network
import random
import time
from umqtt.simple import MQTTClient

def main():
    try:
        mqtt_host = "io.adafruit.com"
        mqtt_username = ""                                  # user name
        mqtt_password = ""                                  # password   

        mqtt_client_id = ""                                 # globally unique value

        mqtt_client = MQTTClient(
            client_id = mqtt_client_id,
            server = mqtt_host,
            user = mqtt_username,
            password = mqtt_password
        )
        
        connect.connect_to_wifi()

        mqtt_client.connect()
        
        while True:
            weather = api.get_weather_for("")                      # add location

            mqtt_publish_topic = ""                                # publish topic

            mqtt_client.publish(mqtt_publish_topic, str(weather))
            print(f'Published {weather}°C')

            time.sleep(900)
    except KeyboardInterrupt:
        print("Program has been terminated by the user.")
    except Exception as e:
        print(f'Failed to publish message: {e}')
    finally:
        mqtt_client.disconnect()
    
    
if __name__ == '__main__':
    main()
