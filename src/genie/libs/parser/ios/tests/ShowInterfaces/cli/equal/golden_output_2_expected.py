expected_output = {
    "Embedded-Service-Engine0/0": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 10000,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_with_dribble": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_no_carrier": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 1000,
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "keepalive": 10,
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "mac_address": "0000.0000.0000",
        "mtu": 1500,
        "oper_status": "down",
        "output_hang": "never",
        "phys_address": "0000.0000.0000",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 64,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "Embedded Service Engine",
    },
    "GigabitEthernet0/0": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 100000,
        "counters": {
            "in_broadcast_pkts": 35509555,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 1837369,
            "in_no_buffer": 0,
            "in_octets": 2700786656,
            "in_overrun": 0,
            "in_pkts": 38129643,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 2,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 256973121,
            "out_pkts": 3553802,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 181716,
            "rate": {
                "in_rate": 7000,
                "in_rate_pkts": 13,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 100,
        "description": "************",
        "duplex_mode": "full",
        "enabled": True,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "ipv4": {"192.168.151.3/24": {"ip": "192.168.151.3", "prefix_length": "24"}},
        "keepalive": 10,
        "last_input": "00:00:00",
        "last_output": "00:00:01",
        "line_protocol": "up",
        "mac_address": "10f3.11ff.5167",
        "media_type": "RJ45",
        "mtu": 1500,
        "oper_status": "up",
        "output_hang": "never",
        "phys_address": "10f3.11ff.5167",
        "port_channel": {"port_channel_member": False},
        "port_speed": "100mbps",
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 75,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "CN Gigabit Ethernet",
    },
    "GigabitEthernet0/1": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 1000000,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "duplex_mode": "auto",
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "keepalive": 10,
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "mac_address": "10f3.11ff.5168",
        "media_type": "RJ45",
        "mtu": 1500,
        "oper_status": "down",
        "output_hang": "never",
        "phys_address": "10f3.11ff.5168",
        "port_channel": {"port_channel_member": False},
        "port_speed": "auto speed",
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 75,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "CN Gigabit Ethernet",
    },
}
