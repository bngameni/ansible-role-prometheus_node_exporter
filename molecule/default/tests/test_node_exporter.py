#!/usr/bin/env python

def test_if_node_exporter_binary_exists(host):
    node_exporter_binary_file = host.file("/usr/local/bin/node_exporter")
    assert node_exporter_binary_file.exists

def test_if_node_exporter_user_exists(host):
    assert host.user("node_exporter").exists

def test_if_node_exporter_is_running_and_or_is_enabled(host):
    node_exporter_service = host.service("node_exporter")
    assert node_exporter_service.is_running

    node_exporter_service_enabled = host.ansible("debug","var=prometheus_node_exporter_service_enabled")
    if node_exporter_service_enabled == "true" :
        assert node_exporter_service.is_enabled


def test_if_node_exporter_socket_is_listening(host):
    assert host.socket("tcp://0.0.0.0:9100").is_listening