from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel

class CustomTreeTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s4)
        self.addLink(h6, s4)
        self.addLink(h7, s4)
        self.addLink(h8, s5)
        self.addLink(h9, s6)
        self.addLink(h10, s6)
        self.addLink(h11, s7)
        self.addLink(h12, s7)
        self.addLink(h13, s8)
        self.addLink(h14, s8)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s2, s8)

def run():
    topo = CustomTreeTopo()
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)
    net = Mininet(topo=topo, controller=controller)
    net.start()

    print("\nTesting network connectivity (pingall):")
    net.pingAll()

    print("\nDumping network details:")
    net.dump()

    print("\nList of nodes (hosts + switches):")
    print(net.nodes)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
