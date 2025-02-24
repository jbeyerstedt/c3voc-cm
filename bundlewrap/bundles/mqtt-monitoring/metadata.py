import bwkeepass as keepass

defaults = {
    'apt': {
        'packages': {
            'jq': {},
            'mosquitto-clients': {},
        },
    },
    'mqtt-monitoring': {
        'server': keepass.url(['ansible', 'mqtt']),
        'username': keepass.username(['ansible', 'mqtt']),
        'password': keepass.password(['ansible', 'mqtt']),
        'plugins': {
            'fan_speed',
        },
    },
    'systemd-timers': {
        'timers': {
            'check_system_and_send_mqtt_message': {
                'command': '/usr/local/sbin/check_system.sh',
                'when': 'minutely',
                'environment': {
                    'TRUNC_HOSTNAME': node.name,
                },
            },
        },
    },
}
