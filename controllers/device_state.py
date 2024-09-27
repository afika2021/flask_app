from controllers.controller_base import ControllerBase
from common.devices_data import get_device_data, set_device_data


class DeviceState(ControllerBase):
    def get (self):
        parser = DeviceState.parser.copy()
        parser.add_argument('deviceId', type=int, location='args', required=True)
        args = parser.parse_args()
        data=get_device_data(args['deviceId'])
        if data !=None:
            return {
                'error': 0,
                'message': 'OK',
                'data': data
            }, 200
        return {
                'error': 1,
                'message': 'Неверный идентификатор устройства',
                'data': None
            }, 200
        
    def post(self):
        parser = DeviceState.parser.copy()
        parser.add_argument('deviceId', type=int, location='json', required=True)
        parser.add_argument('value', type=int, location='json', required=True)
        args = parser.parse_args()
        data = get_device_data(args['deviceId'])
        if data==None:
            return {
                'error': 1,
                'message': 'Неверный идентификатор устройства',
                'data': None
            },200
        if data['type']== 'sensor':
            return {
                'error': 2,
                'message': 'Невозможно изменить состояние данного устройства',
                'data': None
            }, 200
        set_device_data(args['deviceId'], args['value'])
        data = get_device_data(args['deviceId'])
        if data['status'] != args['value']:
            return {
                'error': 3,
                'message': 'Не удалось изменить состояние устройства',
                'data': None
            }, 200
        
        return {
                'error': 0,
                'message': 'OK',
                'data': data
            }, 200
        