# Visulisierung des Streckennetzes

import networkx as nx
from pyvis.network import Network


def vis_network(bssd):

    way_list = bssd.findall("./way[@node='-1']")

    node_list = bssd.findall("node")

    g = nx.MultiGraph()

    for node in node_list:
        node_id = node.get("id")
        if node.get("infinitesimal") == "yes":
            g.add_node(node_id, color='lightgreen', shape="ellipse", physics=False)
        if node.get("infinitesimal") == "no":
            g.add_node(node_id, color='lightblue', shape="ellipse", physics=False)

    for way in way_list:
        from_node = way.get("from")
        to_node = way.get("to")
        way_id = way.get("id")
        g.add_edge(from_node, to_node, color='#aaaaaa', label=f'{way_id}', width="5")

    nt = Network("700px", "72%", bgcolor='white', directed=True, font_color='black')
    nt.from_nx(g)

    nt.set_edge_smooth('dynamic')
    nt.show_buttons(filter_='physics')

    nt.show('network.html')

