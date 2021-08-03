import pyshark
from pyshark import FileCapture
from pyshark.packet.packet import Packet
from pyshark.packet.layer import Layer


TOSERVER_PLAYERPOS = 0x0023
TOSERVER_INTERACT = 0x0039
TOSERVER_GOTBLOCKS = 0x0024
TOCLIENT_REMOVENODE = 0x0022
TOCLIENT_BLOCKDATA = 0x0020

START_DIGGING = 0
STOP_DIGGING = 1
COMPLETE_DIGGING = 2
INTERACT_PLACE = 3


all_events = []


def interact_handler(layer: Layer):
    #print(layer._all_fields)
    action: int = layer.interact_action.int_value

    if action == 5:
        return

    try:
        under_x = int(layer.interact_pointed_under_x)
        under_y = int(layer.interact_pointed_under_y)
        under_z = int(layer.interact_pointed_under_z)
        above_x = int(layer.interact_pointed_above_x.fields[0].show)
        above_y = int(layer.interact_pointed_above_x.fields[1].show)
        above_z = int(layer.interact_pointed_above_x.fields[2].show)
        if action == START_DIGGING:
            pass
            # print(f'Started digging ({x}, {y}, {z})')
        elif action == STOP_DIGGING:
            pass
            # print(f'Stopped digging ({x}, {y}, {z})')
        elif action == COMPLETE_DIGGING:
            # print(f'Completed digging ({x}, {y}, {z})')
            all_events.insert(0, f'{{ x={under_x}, y={under_y}, z={under_z}, event="place" }}')
        elif action == INTERACT_PLACE:
            # print(f'Placed block ({x}, {y}, {z})')
            all_events.insert(0, f'{{ x={above_x}, y={above_y}, z={above_z}, event="break" }}')
    except AttributeError:
        print(layer._all_fields)


command_handlers = {
    TOSERVER_INTERACT: interact_handler,
}


def handle(packet: Packet):
    try:
        print(packet.layers)
        packet['MINETEST']

        last_layer: Layer = packet.layers[-1]
        if last_layer.layer_name == 'minetest.server':
            command: int = last_layer.command.hex_value
            if (cb := command_handlers.get(command, None)) is not None:
                cb(last_layer)
        elif last_layer.layer_name == 'minetest.client':
            command: int = last_layer.command.hex_value
            if (cb := command_handlers.get(command, None)) is not None:
                cb(last_layer)
        elif last_layer.layer_name == 'minetest.control':
            pass
        elif last_layer.layer_name == 'minetest.split':
            pass
        else:
            print(last_layer.layer_name)
    except KeyError:
        pass


def main():
    capture: FileCapture = FileCapture('handouts/toobeetootee.pcap')

    current_packet: Packet = capture.next()
    i = 0
    try:
        while current_packet is not None:
            print(i)
            handle(current_packet)
            current_packet = capture.next()
            i += 1
    except StopIteration:
        print('Done!')

    with open('events.lua', 'w') as f:
        content = "{\n"
        for event in all_events:
            content += "  " + event + ",\n"
        content += "}"
        f.write(content)


if __name__ == '__main__':
    main()
