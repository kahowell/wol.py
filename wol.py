#!/usr/bin/env python
# Copyright 2016 Kevin Howell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import socket
import codecs

parser = argparse.ArgumentParser(description='Send a Wake on LAN packet.')
parser.add_argument('-b', '--broadcast', default='255.255.255.255',
                    help='address to broadcast to (default: 255.255.255.255)')
parser.add_argument('-p', '--port', type=int, default=7, help='port to use')
parser.add_argument('mac', nargs='+',
                    help='MAC addresses to send magic packets for')

args = parser.parse_args()

for mac in args.mac:
    # parse mac
    mac = mac.replace('-', '')
    mac = mac.replace(':', '')
    mac = codecs.decode(mac, 'hex')

    # generate magic packet
    magic_packet = b'\xff' * 6 + mac * 16

    client = socket.socket(type=socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    client.sendto(magic_packet, (args.broadcast, args.port))
