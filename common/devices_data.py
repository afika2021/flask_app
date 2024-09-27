devices_data = {
    0:{
        'name': 'Air pump',
        'type': 'switch',
        'status': 1,
    },
    1:{
        'name': 'Light',
        'type': 'switch',
        'status': 1,
    },
    2:{
        'name': 'Temperature sensor',
        'type': 'sensor',
        'status': 25,
    },
}

def get_device_data(id: int):
    return devices_data.get(id)

def set_device_data(id: int, value: int):
    if id in devices_data:
        devices_data[id]['status'] = value
        
