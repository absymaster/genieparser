expected_output =  {
    "binding_table_configuration": {
        "max/box": "no limit",
        "max/mac": "no limit",
        "max/port": "no limit",
        "max/vlan": "no limit"
    },
    "binding_table_count": {
        "dynamic": 2,
        "local": 1,
        "total": 5
    },
    "binding_table_state_count": {
        "down": 1,
        "reachable": 2,
        "stale": 1,
        "total": 5,
        "verify": 1
    },
    "device": {
        1: {
            "age": "8364mn",
            "client_id": "0000.0000.0000",
            "dev_code": "L",
            "filter": "no",
            "in_crimson": "yes",
            "interface": "Vl39",
            "link_layer_address": "5c5a.c791.d69f(R)",
            "mode": "svi",
            "network_layer_address": "39.39.39.1",
            "policy": "",
            "pref_level_code": 100,
            "state": "REACHABLE",
            "time_left": "",
            "vlan_id": 39
        },
        2: {
            "age": "8453mn",
            "client_id": "0000.0000.0000",
            "dev_code": "S",
            "filter": "no",
            "in_crimson": "yes",
            "interface": "Twe1/0/42",
            "link_layer_address": "dead.beef.0001(S)",
            "mode": "access",
            "network_layer_address": "10.10.10.10",
            "policy": "",
            "pref_level_code": 100,
            "state": "STALE",
            "time_left": "N/A",
            "vlan_id": 39
        },
        3: {
            "age": "5mn",
            "client_id": "0000.0000.0000",
            "dev_code": "ND",
            "filter": "no",
            "in_crimson": "yes",
            "interface": "Twe1/0/42",
            "link_layer_address": "0050.56b0.afed(S)",
            "mode": "access",
            "network_layer_address": "FE80::6AF3:3E56:FE0B:BEE9",
            "policy": "test1 (Device-tracking)",
            "pref_level_code": 5,
            "state": "VERIFY",
            "time_left": "15 s try 2",
            "vlan_id": 39
        },
        4: {
            "age": "171s",
            "client_id": "0000.0000.0000",
            "dev_code": "ND",
            "filter": "no",
            "in_crimson": "yes",
            "interface": "Twe1/0/42",
            "link_layer_address": "0050.56b0.babc(R)",
            "mode": "access",
            "network_layer_address": "FE80::5786:483C:BD32:CC21",
            "policy": "test1 (Device-tracking)",
            "pref_level_code": 5,
            "state": "REACHABLE",
            "time_left": "137 s try 0",
            "vlan_id": 39
        },
        5: {
            "age": "38959mn",
            "client_id": "0000.0000.0000",
            "dev_code": "S",
            "filter": "no",
            "in_crimson": "yes",
            "interface": "Twe1/0/1",
            "link_layer_address": "000a.000b.000c(D)",
            "mode": "trunk",
            "network_layer_address": "1000::1",
            "policy": "",
            "pref_level_code": 100,
            "state": "DOWN",
            "time_left": "N/A",
            "vlan_id": 100
        }
    }
    }