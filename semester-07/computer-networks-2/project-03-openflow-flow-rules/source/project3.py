from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def customTopo():
    net = Mininet(controller=RemoteController, link=TCLink)

    controller = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')

    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)

    net.addLink(s1, s2)
    net.addLink(s2, s3)

    net.start()

    s1.cmd('ovs-ofctl add-flow s1 priority=10,ip,nw_src=10.0.0.1,nw_dst=10.0.0.2,actions=output:2')
    s2.cmd('ovs-ofctl add-flow s2 priority=10,ip,nw_src=10.0.0.1,nw_dst=10.0.0.2,actions=output:2')
    s2.cmd('ovs-ofctl add-flow s2 priority=10,ip,nw_src=10.0.0.2,nw_dst=10.0.0.1,actions=output:1')
    s1.cmd('ovs-ofctl add-flow s1 priority=10,ip,nw_src=10.0.0.2,nw_dst=10.0.0.1,actions=output:1')

    s3.cmd('ovs-ofctl add-flow s3 priority=10,ip,nw_src=10.0.0.3,nw_dst=10.0.0.2,actions=output:2')
    s2.cmd('ovs-ofctl add-flow s2 priority=10,ip,nw_src=10.0.0.3,nw_dst=10.0.0.2,actions=output:1')
    s2.cmd('ovs-ofctl add-flow s2 priority=10,ip,nw_src=10.0.0.2,nw_dst=10.0.0.3,actions=output:3')
    s3.cmd('ovs-ofctl add-flow s3 priority=10,ip,nw_src=10.0.0.2,nw_dst=10.0.0.3,actions=output:1')

    print("Testing connectivity with ping:")
    print(h1.cmd('ping -c 3 10.0.0.2'))
    print(h3.cmd('ping -c 3 10.0.0.2'))

    print("Testing bandwidth with iperf:")
    print("Between h1 and h2:")
    net.iperf((h1, h2), l4Type='UDP')

    print("Between h3 and h2:")
    net.iperf((h3, h2), l4Type='UDP')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopo()
