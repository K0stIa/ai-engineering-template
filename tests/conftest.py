"""Hermetic PR gate: exclude expensive tiers and block in-process external sockets."""

import ipaddress
import os
import socket

import pytest


@pytest.fixture(autouse=True)
def offline_pr_gate(monkeypatch):
    if os.environ.get("AI_PROJECT_PR_GATE") != "1":
        return
    original = socket.socket.connect

    def guarded_connect(sock, address):
        if isinstance(address, tuple):
            host = address[0]
            try:
                local = ipaddress.ip_address(host).is_loopback
            except ValueError:
                local = host == "localhost"
            if not local:
                raise RuntimeError("External network disabled in PR gate")
        return original(sock, address)

    monkeypatch.setattr(socket.socket, "connect", guarded_connect)
