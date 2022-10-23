#!/usr/bin/env python
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(args):

    net = Mininet_wifi()

    info("*** Creating nodes\n") 
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='10' )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', range='10' )
    ap1 = net.addAccessPoint('ap1', ssid='Reynaldi1', mode='g', channel='1', position='10,20,0', range='20')
    ap2 = net.addAccessPoint('ap2', ssid='Reynaldi2', mode='g', channel='1', position='10,50,0', range='20')
    ap3 = net.addAccessPoint('ap3', ssid='Reynaldi3', mode='g', channel='1', position='40,20,0', range='20')
    ap4 = net.addAccessPoint('ap4', ssid='Reynaldi4', mode='g', channel='1', position='40,50,0', range='20')
    ap5 = net.addAccessPoint('ap5', ssid='Reynaldi5', mode='g', channel='1', position='70,20,0', range='20')
    ap6 = net.addAccessPoint('ap6', ssid='Reynaldi6', mode='g', channel='1', position='70,50,0', range='20')
    c1 = net.addController( 'c1' )

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
    net.addLink(ap1, h1)

    if '-p' not in args:
        net.plotGraph(max_x=100, max_y=100)

    net.setMobilityModel(time=0, model='RandomDirection',
                         max_x=100, max_y=100, seed=20)
    
    info("*** Starting network\n")
    net.build()
    c1.start()   
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])
    ap6.start([c1])

    info("*** Running CLI\n")
    CLI( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology(sys.argv)
