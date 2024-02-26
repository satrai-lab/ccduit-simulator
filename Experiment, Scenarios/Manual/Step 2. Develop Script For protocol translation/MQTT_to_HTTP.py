# Protocol Translation Layer (Pseudocode)
# Assumption: Federation B uses MQTT, and Federation A uses HTTP

import paho.mqtt.client as mqtt
import requests

def on_message(client, userdata, message, target_data_model, dest_mqtt_client, destpath, destination_protocol, destination_endpoint):
    """
    This function will be invoked when a message is received on a subscribed topic.
    """
    print(f"Received message: {message.payload.decode('utf-8')} on topic {message.topic}")
    
    # Convert the received data using the data model mapping
    source_data = message.payload.decode('utf-8')
    converted_data = convert_data(source_data, userdata['source_data_model'], target_data_model)
    
    # Send the converted data to the destination based on its protocol
    if destination_protocol == "HTTP":
        destination_endpoint_with_path = str(destination_endpoint) + str(destpath)
        requests.post(destination_endpoint_with_path, json=converted_data)
    elif destination_protocol == "MQTT" and dest_mqtt_client:
        try:
            dest_mqtt_client.publish(str(destpath), converted_data)
        except Exception as e:
            print(f"Failed to publish to MQTT broker. Error: {e}")


def interaction_process():
    """
    Process the interaction between source and destination communities.
    """
    print("TRYING TO SETUP INTERACTION")
    source_endpoint = get_endpoint_url(source_community)
    destination_endpoint = get_endpoint_url(destination_community)
    source_protocol = get_protocol(source_community)
    destination_protocol = get_protocol(destination_community)
    print("HERE IS WHAT I FOUND" + str(source_endpoint) + str(source_protocol) + str(destination_endpoint) + str(destination_protocol))
    
    previous_data_hash = None  # Store the hash of the previously fetched data
    dest_mqtt_client = None
    
    if source_protocol == "MQTT":
        source_mqtt_client = mqtt.Client(userdata={'source_data_model': source_data_model})
        customized_on_message = functools.partial(on_message, 
                                                  target_data_model=target_data_model, 
                                                  dest_mqtt_client=dest_mqtt_client, 
                                                  destpath=destpath, 
                                                  destination_protocol=destination_protocol, 
                                                  destination_endpoint=destination_endpoint)
        source_mqtt_client.on_message = customized_on_message
        source_mqtt_client.connect(source_endpoint)
        source_mqtt_client.subscribe(sourcepath)
        source_mqtt_client.loop_start()
    
    while True:  # Continuous loop for checking interaction status
          # Sleep for a short duration
        interaction_status = get_interaction_status(interaction_id)
        
        if interaction_status == "Paused":
            print("I am paused")
            time.sleep(5)
            continue
        
                
        # Send the converted data to the destination based on its protocol
        if destination_protocol == "HTTP":
            destination_endpoint_with_path = str(destination_endpoint) + str(destpath)
            requests.post(destination_endpoint_with_path, json=converted_data)
        elif destination_protocol == "MQTT" and dest_mqtt_client:
            try:
                dest_mqtt_client.publish(str(destpath), converted_data)
            except Exception as e:
                print(f"Failed to publish to MQTT broker. Error: {e}")
        else:
            print(f"Failed to fetch data from {source_endpoint_with_path}. Status code: {response.status_code}")
