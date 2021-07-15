from Inverter import Inverter
class Delta33G3Inverter(Inverter):

    #Known Commands
            ##code, name, format, divisor, units, response size

    cmds = [
            ['\x00\x09','Serial',11,0,'',100],
            ['\x10\x07','Date Code',11,0,'',100],
            ['\x10\x01','DC Current 1',0,10.0,'A',100],
            ['\x10\x02','DC Voltage 1',0,1,'V',100],
            ['\x10\x03','DC Power 1',0,1,'W',100],
            ['\x10\x04','DC Current 2',0,10.0,'A',100],
            ['\x10\x05','DC Voltage 2',0,1,'V',100],
            ['\x10\x06','DC Power 2',0,1,'W',100],
            ['\x10\x08','AC Voltage',0,1,'V',100],            
            ['\x10\x09','AC Power',0,1,'W',100],
            ['\x11\x07','AC I Avg',0,10.0,'A',100],
            ['\x11\x08','AC V Avg',0,1,'V',100],
            ['\x11\x09','AC P Avg',0,1,'W',100],
            ['\x13\x03','Energy Today',0,1,'Wh',100],
            ['\x13\x04','Uptime',0,1,'min',100],
            ['\x00\x01','01',1,0,'',100],
            ['\x00\x02','02',0,1,'',100],
            ['\x00\x03','03',0,1,'',100],
            ['\x00\x04','04',11,0,'',100],
            ['\x00\x05','05',11,0,'',100],
            ['\x00\x06','06',0,1,'',100],
            ['\x00\x07','07',11,0,'',100],
            ['\x00\x08','08',11,0,'',100],
            ['\x00\x40','FW Version',10,0,'',100],                        
            ['\x20\x05','AC Temp',0,1,'o',100],
            ['\x21\x08','DC Temp',0,1,'o',100]
        ]

    
