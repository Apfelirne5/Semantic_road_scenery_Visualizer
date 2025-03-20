# Visulisierung eines bestimmten ways der XML-Datei über das Terminal

import argparse
import xml.etree.ElementTree as ET
from jinja2 import Environment, PackageLoader, select_autoescape
import re
import webbrowser
import os


def visualize(bssd, way_id):

    # Deklriert ein HTML-Element als Basis für die Visualisierung.
    # Deklariert den HTML-Elemente für den Aufbau der Legende und Schaltflächen.
    # Ruft die Funktionen für die Visualisierung der ways auf
    # Input:
    #   bssd-element der XML-Datei

    # Output:
    #   HTML-Element als Basis für die Visualisierung

    # root HTML-Element

    div_viz = ET.Element('div', attrib={'id': 'bssd_world', 'class': 'showTla_No'})

    # HTML-header

    header = ET.SubElement(div_viz, 'header')
    div_title = ET.SubElement(header, 'div', attrib={'id': 'title'})
    div_title.text = f'BSSD Visualizer'

    div_info = ET.SubElement(header, 'div', attrib={'id': 'info'})

    div_ref_direction = ET.SubElement(div_info, 'div', attrib={'id': 'ref_direction'})
    div_preferences = ET.SubElement(div_info, 'div', attrib={'id': 'preferences'})
    div_legend = ET.SubElement(div_info, 'div', attrib={'id': 'legend'})

    div_ref_direction_title = ET.SubElement(div_ref_direction, 'div', attrib={'id': 'ref_direction_title'})
    div_ref_direction_title.text = "Reference Direction"
    div_ref_direction_arrow = ET.SubElement(div_ref_direction, 'div', attrib={'id': 'ref_direction_arrow'})

    div_legend_allowed = "allowed conditional prohibited not possible"

    form = ET.SubElement(div_preferences, 'form')
    div = ET.SubElement(form, 'div', attrib={'class': "bd"})
    div_title_bd = ET.SubElement(div, 'div', attrib={'class': "title_bd"})
    div_bd_arrow = ET.SubElement(div, 'div', attrib={'class': "bd_arrow"})

    div_title_bd.text = "Behaviour Direction"
    div_bd = ET.SubElement(div, 'div', attrib={'class': "bd_radio_buttons"})
    input1 = ET.SubElement(div_bd, 'input', attrib={'type': "radio", 'name': "behaviourDirection", 'value': "none",
                                                    'onclick': "handleBehaviourDirectionRadioButton(this);", 'id': "none", 'checked': ""})
    label1 = ET.SubElement(div_bd, 'label', attrib={'class': "radio-inline label_bd none", 'for': "none"})
    label1.text = 'None'

    input2 = ET.SubElement(div_bd, 'input', attrib={'type': "radio", 'name': "behaviourDirection", 'value': "forward",
                                                    'onclick': "handleBehaviourDirectionRadioButton(this);", 'id': "forward"})
    label2 = ET.SubElement(div_bd, 'label', attrib={'class': "radio-inline label_bd forward", 'for': "forward"})
    label2.text = 'Forward Behavior'

    input3 = ET.SubElement(div_bd, 'input', attrib={'type': "radio", 'name': "behaviourDirection", 'value': "backward",
                                                    'onclick': "handleBehaviourDirectionRadioButton(this);", 'id': "backward"})
    label3 = ET.SubElement(div_bd, 'label', attrib={'class': "radio-inline label_bd backward", 'for': "backward"})
    label3.text = 'Backward Behavior'

    div2 = ET.SubElement(form, 'div', attrib={'class': "tla"})
    div_title_tla = ET.SubElement(div2, 'div', attrib={'class': "title_tla"})
    div_tla_tl = ET.SubElement(div2, 'div', attrib={'class': "tla_trafficlight"})

    div_title_tla.text = "Traffic Light Status"
    div_tla = ET.SubElement(div2, 'div')

    input5 = ET.SubElement(div_tla, 'input', attrib={'type': "radio", 'name': "Tla_status", 'value': "Yes",
                                                    'onclick': "handleTrafficLightActiveRadioButton(this);", 'id': "tla_yes"})
    label5 = ET.SubElement(div_tla, 'label', attrib={'class': "radio-inline label_tla_yes", 'for': "tla_yes"})
    label5.text = 'Traffic Light Active: Yes'
    input6 = ET.SubElement(div_tla, 'input', attrib={'type': "radio", 'name': "Tla_status", 'value': "No",
                                                    'onclick': "handleTrafficLightActiveRadioButton(this);", 'id': "tla_no", 'checked': ""})
    label6 = ET.SubElement(div_tla, 'label', attrib={'class': "radio-inline label_tla_no", 'for': "tla_no"})
    label6.text = 'Traffic Light Active: No'

    div_legend_container_reservation_objects = ET.SubElement(div_legend, 'div', attrib={'class': "container_reservation_objects"})

    div_legend_container1 = ET.SubElement(div_legend_container_reservation_objects, 'div',
                                          attrib={'class': "container tt_pedestrian"})
    div_legend_container2 = ET.SubElement(div_legend_container_reservation_objects, 'div',
                                          attrib={'class': "container tt_bicycle"})
    div_legend_container3 = ET.SubElement(div_legend_container_reservation_objects, 'div',
                                          attrib={'class': "container tt_motorvehicle"})
    div_legend_container4 = ET.SubElement(div_legend_container_reservation_objects, 'div',
                                          attrib={'class': "container containerlast tt_railedvehicle"})

    div_legend_reservation_objects_pedestrian = ET.SubElement(div_legend_container1, 'div',
                                                              attrib={'class': "reservation_objects", 'id': "pedestrian"})
    div_legend_reservation_objects_pedestrian_t = ET.SubElement(div_legend_container1, 'div')
    div_legend_reservation_objects_pedestrian_t.text = 'pedestrian'

    div_legend_reservation_objects_pedestrian = ET.SubElement(div_legend_container2, 'div',
                                                              attrib={'class': "reservation_objects_l", 'id': "bicycle"})
    div_legend_reservation_objects_pedestrian_t = ET.SubElement(div_legend_container2, 'div')
    div_legend_reservation_objects_pedestrian_t.text = 'bicycle'

    div_legend_reservation_objects_pedestrian = ET.SubElement(div_legend_container3, 'div',
                                                              attrib={'class': "reservation_objects_", 'id': "motorvehicle"})
    div_legend_reservation_objects_pedestrian_t = ET.SubElement(div_legend_container3, 'div')
    div_legend_reservation_objects_pedestrian_t.text = 'motor vehicle'

    div_legend_reservation_objects_pedestrian = ET.SubElement(div_legend_container4, 'div',
                                                              attrib={'class': "reservation_objects_l", 'id': "railedvehicle"})
    div_legend_reservation_objects_pedestrian_t = ET.SubElement(div_legend_container4, 'div')
    div_legend_reservation_objects_pedestrian_t.text = 'railed vehicle'

    div_legend_container_boundary = ET.SubElement(div_legend, 'div', attrib={'class': "container_boundary"})

    div_legend_container5 = ET.SubElement(div_legend_container_boundary, 'div', attrib={'class': "container tt_allowed"})
    div_legend_container6 = ET.SubElement(div_legend_container_boundary, 'div', attrib={'class': "container tt_conditional"})
    div_legend_container7 = ET.SubElement(div_legend_container_boundary, 'div', attrib={'class': "container tt_prohibited"})
    div_legend_container8 = ET.SubElement(div_legend_container_boundary, 'div', attrib={'class': "container tt_not_possible"})
    div_legend_container9 = ET.SubElement(div_legend_container_boundary, 'div', attrib={'class': "container containerlast tt_link"})

    div_legend_boundary1 = ET.SubElement(div_legend_container5, 'div', attrib={'class': "boundary", 'id': "allowed"})
    div_legend_boundary1_t = ET.SubElement(div_legend_container5, 'div')
    div_legend_boundary1_t.text = 'allowed'

    div_legend_boundary2 = ET.SubElement(div_legend_container6, 'div', attrib={'class': "boundary", 'id': "conditional"})
    div_legend_boundary2_t = ET.SubElement(div_legend_container6, 'div')
    div_legend_boundary2_t.text = 'conditional'

    div_legend_boundary3 = ET.SubElement(div_legend_container7, 'div', attrib={'class': "boundary", 'id': "prohibited"})
    div_legend_boundary3_t = ET.SubElement(div_legend_container7, 'div')
    div_legend_boundary3_t.text = 'prohibited'

    div_legend_boundary4 = ET.SubElement(div_legend_container8, 'div', attrib={'class': "boundary", 'id': "not_possible"})
    div_legend_boundary4_t = ET.SubElement(div_legend_container8, 'div')
    div_legend_boundary4_t.text = 'not possible'

    div_legend_link = ET.SubElement(div_legend_container9, 'div', attrib={'class': "link", 'id': "link"})
    div_legend_link_t = ET.SubElement(div_legend_container9, 'div')
    div_legend_link_t.text = 'link'

    div_legend_container_reservation = ET.SubElement(div_legend, 'div', attrib={'class': "container_reservation"})

    div_legend_container10 = ET.SubElement(div_legend_container_reservation, 'div', attrib={'class': "container tt_own_reserved"})
    div_legend_container11 = ET.SubElement(div_legend_container_reservation, 'div', attrib={'class': "container tt_equally_reserved"})
    div_legend_container12 = ET.SubElement(div_legend_container_reservation, 'div', attrib={'class': "container tt_externally_reserved"})

    div_legend_reservation1 = ET.SubElement(div_legend_container10, 'div',
                                            attrib={'class': "reservation", 'id': "own_reserved"})
    div_legend_reservation1_t = ET.SubElement(div_legend_container10, 'div')
    div_legend_reservation1_t.text = 'own-reserved'

    div_legend_reservation2 = ET.SubElement(div_legend_container11, 'div',
                                            attrib={'class': "reservation", 'id': "equally_reserved"})
    div_legend_reservation2_t = ET.SubElement(div_legend_container11, 'div')
    div_legend_reservation2_t.text = 'equally-reserved'

    div_legend_reservation2 = ET.SubElement(div_legend_container12, 'div',
                                            attrib={'class': "reservation", 'id': "externally_reserved"})
    div_legend_reservation2_t = ET.SubElement(div_legend_container12, 'div')
    div_legend_reservation2_t.text = 'externally-reserved'

    div_lines = ET.SubElement(div_viz, 'div', attrib={'class': "lines"})

    # Visualizing way

    # if bssd.find('way'):                          # Visualize all ways
    #     for way in bssd.findall('way'):
    #         div_viz.append(visualize_way_info(way))
    #         div_viz.append(visualize_way(way))

    # if all(ele.get('trafficLightActive') is None for ele in bssd.findall(".//")):
    #     div2.set('style', 'background-color: gray')
    #     div2.set('id', 'no_tla')

    way = bssd.find(f"./way[@id='{way_id}']")
    div_viz.append(visualize_way_info(way))
    div_viz.append(visualize_way(way))            # pre_id (revisionnumber?)

    if all(ele.get('trafficLightActive') is None for ele in way.findall(".//")):
        div2.set('style', 'background-color: gray')
        div2.set('id', 'no_tla')

    return div_viz


def visualize_way_info(way):
    way_id = way.get("id")
    from_node_id = way.get('from')
    to_node_id = way.get('to')
    inside_node = way.get('node')

    way_predecessor = way.find("link").find("predecessor")

    way_successor = way.find("link").find("successor")

    predecessor_type = way_predecessor.get("elementType")
    successor_type = way_successor.get("elementType")

    predecessor_id = way_predecessor.get("elementId")
    successor_id = way_successor.get("elementId")

    div_way_text = ET.Element('div', attrib={'class': 'way_info', 'data-predecessor': f'{predecessor_type} {predecessor_id}', 'data-successor': f'{successor_type} {successor_id}'})

    if int(inside_node) == -1:
        div_way_text.text = f'Way {way_id}:  node {from_node_id} to node {to_node_id}'
    if int(inside_node) != -1:
        div_way_text.text = f'Way {way_id}: node {from_node_id} to node {to_node_id} (in node {inside_node})'

    return div_way_text


def visualize_way(way, pre_id=''):

    div_way_id = f'{pre_id}_way-{way.get("id")}'

    from_node_id = way.get('from')
    to_node_id = way.get('to')

    div_way = ET.Element('div', attrib={'class': 'bssd_way',
                                        'id': div_way_id, 'data-from_node': from_node_id, 'data-to_node': to_node_id})

    if way.find('segment'):
        #   for segment in way.findall('segment'):                         # without left/right difference
        #       div_way.append(visualize_segment(segment, div_way_id))

        div_way.append(visualize_leftside(way, div_way_id))
        div_way.append(visualize_midline(way, div_way_id))
        div_way.append(visualize_rightside(way, div_way_id))

    return div_way


def visualize_leftside(way, pre_id=''):
    side = 'left'
    div_leftside_id = f'{pre_id}_leftside'
    div_leftside = ET.Element('div', attrib={'class': 'bssd_leftside', 'id': div_leftside_id})

    list_segments = way.findall('segment')
    list_ids = []

    for segment in list_segments:
        id_n = segment.get('id')
        list_ids.append(id_n)

    list_segments_sorted = list_sort(list_segments, list_ids)

    for segment in list_segments_sorted:
        if len(list_segments_sorted) != 1:
            if segment == list_segments_sorted[0]:
                seg_position = "first"
                div_leftside.append(visualize_segment(segment, div_leftside_id, side, seg_position))
            if segment == list_segments_sorted[-1]:
                seg_position = "last"
                div_leftside.append(visualize_segment(segment, div_leftside_id, side, seg_position))
            if segment != list_segments_sorted[0] and segment != list_segments_sorted[-1]:
                seg_position = "middle"
                div_leftside.append(visualize_segment(segment, div_leftside_id, side, seg_position))
        if len(list_segments_sorted) == 1:
            seg_position = "one_segment"
            div_leftside.append(visualize_segment(segment, div_leftside_id, side, seg_position))

    return div_leftside


def visualize_midline(way, pre_id=''):

    from_node_id = way.get('from')
    to_node_id = way.get('to')

    div_midline_id = f'{pre_id}_way_midline'
    div_midline = ET.Element('div', attrib={'class': 'bssd_midlane', 'id': div_midline_id, 'data-from_node': from_node_id, 'data-to_node': to_node_id})

    return div_midline


def visualize_rightside(way, pre_id=''):
    side = 'right'
    div_rightside_id = f'{pre_id}_rightside'
    div_rightside = ET.Element('div', attrib={'class': 'bssd_rightside', 'id': div_rightside_id})

    list_segments = way.findall('segment')
    list_ids = []

    for segment in list_segments:
        id_n = segment.get('id')
        list_ids.append(id_n)

    list_segments_sorted = list_sort(list_segments, list_ids)

    for segment in list_segments_sorted:
        if len(list_segments_sorted) != 1:
            if segment == list_segments_sorted[0]:
                seg_position = "first"
                div_rightside.append(visualize_segment(segment, div_rightside_id, side, seg_position))
            if segment == list_segments_sorted[-1]:
                seg_position = "last"
                div_rightside.append(visualize_segment(segment, div_rightside_id, side, seg_position))
            if segment != list_segments_sorted[0] and segment != list_segments_sorted[-1]:
                seg_position = "middle"
                div_rightside.append(visualize_segment(segment, div_rightside_id, side, seg_position))
        if len(list_segments_sorted) == 1:
            seg_position = "one_segment"
            div_rightside.append(visualize_segment(segment, div_rightside_id, side, seg_position))
    return div_rightside


def visualize_segment(segment, pre_id='', side='', seg_position=""):
    div_seg_id = f'{pre_id}_seg-{segment.get("id")}'
    div_seg = ET.Element('div', attrib={'class': 'bssd_segment',
                                        'id': div_seg_id,
                                        'data-segment_id': f'{segment.get("id")}'})

    # for d in ['left', 'right']:

    if segment.find(side) is not None:
        list_lanes = segment.find(side).findall('lane')
        list_ids = []

        for lane in list_lanes:
            id_n = lane.get('id')
            list_ids.append(id_n)

        list_lanes_sorted = list_reverse_sort(list_lanes, list_ids)

        if segment.find(side):
            for lane in list_lanes_sorted:
                div_seg.append(visualize_lane(lane, div_seg_id, seg_position))

    return div_seg


def visualize_lane(lane, pre_id='', seg_position=""):
    div_lane_id = f'{pre_id}_lane-{lane.get("id")}'
    way_id = int(re.findall(f"way-(\d*)_", div_lane_id)[0])
    segment_id = int(re.findall(f"seg-(\d*)_", div_lane_id)[0])
    predecessor_ids = ""
    successor_ids = ""

    link = lane.find('link')
    predecessor_list = link.findall('predecessor')
    for predecessor in predecessor_list:

        if len(predecessor_ids) == 0:
            predecessor_ids = predecessor.get('laneId')
        else:
            predecessor_ids = predecessor_ids + ', ' + predecessor.get('laneId')

    successor_list = link.findall('successor')
    for successor in successor_list:

        if len(successor_ids) == 0:
            successor_ids = successor.get('laneId')
        else:
            successor_ids = successor_ids + ', ' + successor.get('laneId')

    div_lane = ET.Element('div', attrib={'class': 'bssd_lane',
                                         'id': div_lane_id,
                                         'data-lane_id': f'{lane.get("id")}',
                                         'data-all-id': f'{div_lane_id}', 'data-way-id': f'{way_id}',
                                         'data-segment-id': f'{segment_id}',
                                         'data-predecessor-ids': f'{predecessor_ids}',
                                         'data-successor-ids': f'{successor_ids}'})

    div_lane.append(visualize_lane_info(lane, div_lane, seg_position))

    return div_lane


def visualize_lane_info(lane, div_lane, seg_position=""):
    div_lane_info = ET.Element('div', attrib={'class': 'bssd_lane_info'})

    link = lane.find('link')
    predecessor = link.findall('predecessor')
    div_lane_id = div_lane.get("id")
    div_lane_id_predecessor = 0

    # search ids of way, segment and lane in div_lane_id for predecessor lines
    w_num = int(re.findall(f"way-(\d*)_", div_lane_id)[0])
    s_num = int(re.findall(f"seg-(\d*)_", div_lane_id)[0])
    l_num = int(re.findall(f"lane-([\d-]*)", div_lane_id)[0])
    side_str = re.findall(f"_(\D*)side_", div_lane_id)[0]

    # drawing predecessor lines
    for predecessor_list_item in predecessor:
        if int(predecessor_list_item.get('laneId')) >= 0:
            div_lane_id_predecessor = div_lane_id.replace(f"seg-{s_num}", f"seg-{s_num - 1}").replace(
                f"_{side_str}side_", f"_leftside_").replace(f"lane-{l_num}",
                                                            f"lane-{int(predecessor_list_item.get('laneId'))}")

        if int(predecessor_list_item.get('laneId')) < 0:
            div_lane_id_predecessor = div_lane_id.replace(f"seg-{s_num}", f"seg-{s_num - 1}").replace(
                f"_{side_str}side_", f"_rightside_").replace(f"lane-{l_num}",
                                                             f"lane-{int(predecessor_list_item.get('laneId'))}")

        script = ET.Element('script', attrib={'type': 'module'})
        script.text = f'connect(getId("{div_lane_id}"), getId("{div_lane_id_predecessor}"), "yellow", 2);'
        div_lane.insert(1, script)

    # Visualize boundary, reservation, speed, overtake and links

    behavior_directions = [f'{d}Behavior' for d in ['forward', 'backward']]
    for bd in behavior_directions:
        behavior = lane.find(bd)
        if behavior is not None:

            # ==== BOUNDARY ====

            boundary = behavior.find('boundary')
            if boundary is not None:
                longitudinal_list = boundary.findall('longitudinal')
                if longitudinal_list[0] is not None:
                    if longitudinal_list[0].get('trafficLightActive') is None:
                        if 'crossing' in longitudinal_list[0].attrib:
                            add_html_class(div_lane, f'{bd}_boundary_longitudinal_{longitudinal_list[0].get("crossing")}')

                            condition = longitudinal_list[0].findall('condition')
                            if len(condition) > 0:
                                div_conditional = ET.SubElement(div_lane_info, 'div',
                                                                attrib={'class': f'bssd_lane_boundary_crossing '
                                                                                 f'bssd_lane_boundary_crossing_{bd}'})

                                for condition_tag in condition:
                                    if condition_tag.get('type') is not None:
                                        condition_type = condition_tag.get("type").replace(' ', '')
                                        ET.SubElement(div_conditional, 'div',
                                                      attrib={'class': f'boundary_longitudinal_condition '
                                                                       f'bd_boundary_longitudinal_condition_{condition_type}'})

                    if longitudinal_list[0].get('trafficLightActive') is not None:
                        if 'crossing' in longitudinal_list[0].attrib:
                            for longitudinal_el in longitudinal_list:

                                # longitudinal TrafficLightActive YES
                                if longitudinal_el.get('trafficLightActive') == 'yes':
                                    add_html_class(div_lane,
                                                   f'Tla_Yes_{bd}_boundary_longitudinal_{longitudinal_el.get("crossing")}')

                                    condition = longitudinal_el.findall('condition')
                                    if len(condition) > 0:
                                        div_conditional = ET.SubElement(div_lane_info, 'div',
                                                                        attrib={'class': f'bssd_lane_boundary_crossing '
                                                                                         f'bssd_lane_boundary_crossing_{bd}_Tla_Yes'})

                                        for condition_tag in condition:
                                            if condition_tag.get('type') is not None:
                                                condition_type = condition_tag.get("type").replace(' ', '')
                                                ET.SubElement(div_conditional, 'div',
                                                              attrib={'class': f'boundary_longitudinal_condition '
                                                                               f'bd_boundary_longitudinal_condition_{condition_type}'})
                                # longitudinal TrafficLightActive NO
                                if longitudinal_el.get('trafficLightActive') == 'no':
                                    add_html_class(div_lane,
                                                   f'Tla_No_{bd}_boundary_longitudinal_{longitudinal_el.get("crossing")}')

                                    condition = longitudinal_el.findall('condition')
                                    if len(condition) > 0:
                                        div_conditional = ET.SubElement(div_lane_info, 'div',
                                                                        attrib={'class': f'bssd_lane_boundary_crossing '
                                                                                         f'bssd_lane_boundary_crossing_{bd}_Tla_No'})

                                        for condition_tag in condition:
                                            if condition_tag.get('type') is not None:
                                                condition_type = condition_tag.get("type").replace(' ', '')
                                                ET.SubElement(div_conditional, 'div',
                                                              attrib={'class': f'boundary_longitudinal_condition '
                                                                               f'bd_boundary_longitudinal_condition_{condition_type}'})

                lateral = boundary.find('lateral')
                if lateral is not None:
                    for side in ['left', 'right']:
                        side_boundary = lateral.find(side)
                        if side_boundary is not None:
                            if 'crossing' in side_boundary.attrib:
                                add_html_class(div_lane,
                                               f'{bd}_boundary_lateral_{side}_{side_boundary.get("crossing")}')

            # ===== OVERTAKE ======

            overtake = behavior.find("overtake")
            if overtake is not None:
                div_overtake = ET.SubElement(div_lane_info, 'div', attrib={'class': f'bssd_lane_overtake '
                                                                                    f'bssd_lane_overtake_{bd}'})
                ET.SubElement(div_overtake, 'div',
                              attrib={'class': f'bssd_overtake_permission '
                                               f'bssd_overtake_permission_{overtake.get("permission")}'})

            # ===== RESERVATION ======

            reservation_list = behavior.findall("reservation")
            if reservation_list[0].get('trafficLightActive') is None:

                if reservation_list[0] is not None:
                    div_reservation = ET.SubElement(div_lane_info, 'div',
                                                    attrib={'class': f'bssd_lane_reservation '
                                                                     f'bssd_lane_reservation_{bd}'})

                    if 'type' in reservation_list[0].attrib:
                        reservation_type = reservation_list[0].get("type").replace('-', '')
                        add_html_class(div_lane,
                                       f'{bd}_reservation_type_{reservation_type}')

                    for reservation_el in reservation_list:
                        if reservation_el.get('object') is not None:
                            reservation_obj = reservation_el.get("object").replace(' ', '')
                            reservation_obj_id = f'{div_lane_id}_{bd}_{reservation_obj}'
                            link_string = ""
                            if reservation_el.find('link') is not None:
                                for link in reservation_el.findall('link'):
                                    linked_way = link.get('linkedWay')
                                    linked_segment = link.get('linkedSegment')
                                    linked_area = link.get('linkedArea')
                                    if int(link.get('linkedWay')) != w_num:
                                        if len(link_string) == 0:
                                            link_string = "linkedWay: " + linked_way + " linkedSegment: " + linked_segment + " linkedArea: " + linked_area
                                        else:
                                            link_string = link_string + " " + "linkedWay: " + linked_way + " linkedSegment: " + linked_segment + " linkedArea: " + linked_area

                            div_reservation_object = ET.SubElement(div_reservation, 'div',
                                                                   attrib={'class': f'reservation_objects ' f'reservation_object_{reservation_obj}', 'onmouseout': 'deleteElement()',
                                                                           'id': f'{reservation_obj_id}', 'data-links': f'{link_string}'})
                            add_html_class(div_reservation, 'gradient')

                            if reservation_el.get("type") != reservation_list[0].get("type"):
                                different_reservation_type = reservation_el.get("type").replace('-', '')
                                add_html_class(div_reservation_object, f'reservation_object_{different_reservation_type}')

            # ===== Links =====

                            if reservation_el.find('link') is not None:
                                if reservation_el.findall('link')[0] is not None:

                                    line_thickness = 20
                                    line_color = "#648FFF"

                                    string_onmouseover = ""
                                    for link in reservation_el.findall('link'):
                                        if int(link.get('linkedWay')) == w_num:
                                            linked_segment = int(link.get('linkedSegment'))
                                            if link.get('linkedArea').lstrip('-').isdigit() and link.get('linkedArea') != '0':
                                                if linked_segment > s_num:
                                                    lane_number = int(link.get('linkedArea'))

                                                    if lane_number > 0:
                                                        div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}", f"seg-{linked_segment}").replace(
                                                            f"_{side_str}side_", f"_leftside_").replace(f"lane-{l_num}",
                                                                                                        f"lane-{lane_number}")
                                                    if lane_number < 0:
                                                        div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}", f"seg-{linked_segment}").replace(
                                                            f"_{side_str}side_", f"_rightside_").replace(f"lane-{l_num}",
                                                                                                        f"lane-{lane_number}")

                                                    if len(string_onmouseover) == 0:
                                                        connect_function = f'connectNextSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                    else:
                                                        connect_function = f' connectNextSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                if linked_segment < s_num:
                                                    lane_number = int(link.get('linkedArea'))

                                                    if lane_number > 0:
                                                        div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}", f"seg-{linked_segment}").replace(
                                                            f"_{side_str}side_", f"_leftside_").replace(f"lane-{l_num}",
                                                                                                        f"lane-{lane_number}")

                                                    if lane_number < 0:
                                                        div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}", f"seg-{linked_segment}").replace(
                                                            f"_{side_str}side_", f"_rightside_").replace(f"lane-{l_num}",
                                                                                                        f"lane-{lane_number}")

                                                    if len(string_onmouseover) == 0:
                                                        connect_function = f'connectLastSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                    else:
                                                        connect_function = f' connectLastSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                if linked_segment == s_num:
                                                    lane_number = int(link.get('linkedArea'))
                                                    if lane_number > l_num:
                                                        if lane_number > 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_", f"_leftside_").replace(f"lane-{l_num}",
                                                                                                    f"lane-{lane_number}")
                                                        if lane_number < 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_", f"_rightside_").replace(f"lane-{l_num}",
                                                                                                    f"lane-{lane_number}")

                                                        if len(string_onmouseover) == 0:
                                                            connect_function = f'connectLaneTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                        else:
                                                            connect_function = f' connectLaneTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                    if lane_number < l_num:
                                                        if lane_number > 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_", f"_leftside_").replace(f"lane-{l_num}",
                                                                                                    f"lane-{lane_number}")
                                                        if lane_number < 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_", f"_rightside_").replace(f"lane-{l_num}",
                                                                                                    f"lane-{lane_number}")

                                                        if len(string_onmouseover) == 0:
                                                            connect_function = f'connectLaneBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                        else:
                                                            connect_function = f' connectLaneBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                            if link.get('linkedArea') == 'inf':
                                                div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_",
                                                                                         f"_leftside_").replace(
                                                    f"_lane-{l_num}", "")

                                                if len(string_onmouseover) > 0:
                                                    connect_function = f' connectSegmentTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function

                                                else:
                                                    connect_function = f'connectSegmentTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function

                                            if link.get('linkedArea') == '-inf':

                                                div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_",
                                                                                         f"_rightside_").replace(
                                                    f"_lane-{l_num}", "")

                                                if len(string_onmouseover) > 0:
                                                    connect_function = f' connectSegmentBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function

                                                else:
                                                    connect_function = f'connectSegmentBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function

                                        if int(link.get('linkedWay')) != w_num:
                                            if seg_position == "first":
                                                if len(string_onmouseover) > 0:
                                                    connect_function = f' connectWayFirst(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function
                                                else:
                                                    connect_function = f' connectWayFirst(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function

                                        if int(link.get('linkedWay')) != w_num:
                                            if seg_position == "last":
                                                if len(string_onmouseover) > 0:
                                                    connect_function = f' connectWayLast(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function
                                                else:
                                                    connect_function = f' connectWayLast(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                    string_onmouseover = string_onmouseover + connect_function

                                    div_reservation_object.set('onmouseover', f'{string_onmouseover}')

            if reservation_list[0].get('trafficLightActive') is not None:

                reservation_yes_list = behavior.findall("./reservation[@trafficLightActive='yes']")
                if reservation_yes_list[0].get('trafficLightActive') == 'yes':

                    div_reservation = ET.SubElement(div_lane_info, 'div',
                                                    attrib={'class': f'bssd_lane_reservation '
                                                                     f'bssd_lane_reservation_{bd}_Tla_Yes'})

                    if 'type' in reservation_yes_list[0].attrib:
                        reservation_type = reservation_yes_list[0].get("type").replace('-', '')
                        add_html_class(div_lane,
                                       f'Tla_Yes_{bd}_reservation_type_{reservation_type}')

                        for reservation_el in reservation_yes_list:
                            if reservation_el.get('object') is not None:
                                reservation_obj = reservation_el.get("object").replace(' ', '')
                                reservation_obj_id = f'{div_lane_id}_{bd}_tlaYes_{reservation_obj}'
                                link_string = ""
                                if reservation_el.find('link') is not None:
                                    for link in reservation_el.findall('link'):
                                        linked_way = link.get('linkedWay')
                                        linked_segment = link.get('linkedSegment')
                                        linked_area = link.get('linkedArea')
                                        if int(link.get('linkedWay')) != w_num:
                                            if len(link_string) == 0:
                                                link_string = "linkedWay: " + linked_way + " linkedSegment: " + linked_segment + " linkedArea: " + linked_area
                                            else:
                                                link_string = link_string + " " + "linkedWay: " + linked_way + " linkedSegment: " + linked_segment + " linkedArea: " + linked_area
                                div_reservation_object = ET.SubElement(div_reservation, 'div', attrib={'class': f'reservation_objects '
                                                                                       f'reservation_object_{reservation_obj}', 'onmouseout': 'deleteElement()',
                                                                           'id': f'{reservation_obj_id}', 'data-links': f'{link_string}'})
                                add_html_class(div_reservation, 'gradient')

                                if reservation_el.get("type") != reservation_list[0].get("type"):
                                    different_reservation_type = reservation_el.get("type").replace('-', '')
                                    add_html_class(div_reservation_object,
                                                   f'reservation_object_{different_reservation_type}')

                            # ===== Links =====

                                if reservation_el.find('link') is not None:
                                    if reservation_el.findall('link')[0] is not None:

                                        line_thickness = 20
                                        line_color = "#648FFF"

                                        string_onmouseover = ""
                                        for link in reservation_el.findall('link'):
                                            if int(link.get('linkedWay')) == w_num:
                                                linked_segment = int(link.get('linkedSegment'))
                                                if link.get('linkedArea').lstrip('-').isdigit() and link.get('linkedArea') != '0':
                                                    if linked_segment > s_num:
                                                        lane_number = int(link.get('linkedArea'))

                                                        if lane_number > 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_leftside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")
                                                        if lane_number < 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_rightside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")

                                                        if len(string_onmouseover) == 0:
                                                            connect_function = f'connectNextSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                        else:
                                                            connect_function = f' connectNextSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                    if linked_segment < s_num:
                                                        lane_number = int(link.get('linkedArea'))

                                                        if lane_number > 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_leftside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")

                                                        if lane_number < 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_rightside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")

                                                        if len(string_onmouseover) == 0:
                                                            connect_function = f'connectLastSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                        else:
                                                            connect_function = f' connectLastSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                    if linked_segment == s_num:
                                                        lane_number = int(link.get('linkedArea'))
                                                        if lane_number > l_num:
                                                            if lane_number > 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_leftside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")
                                                            if lane_number < 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_rightside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")

                                                            if len(string_onmouseover) == 0:
                                                                connect_function = f'connectLaneTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                            else:
                                                                connect_function = f' connectLaneTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                        if lane_number < l_num:
                                                            if lane_number > 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_leftside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")
                                                            if lane_number < 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_rightside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")

                                                            if len(string_onmouseover) == 0:
                                                                connect_function = f'connectLaneBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                            else:
                                                                connect_function = f' connectLaneBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                if link.get('linkedArea') == 'inf':
                                                    div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_",
                                                                                             f"_leftside_").replace(
                                                        f"_lane-{l_num}", "")

                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectSegmentTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                    else:
                                                        connect_function = f'connectSegmentTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                if link.get('linkedArea') == '-inf':

                                                    div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_",
                                                                                             f"_rightside_").replace(
                                                        f"_lane-{l_num}", "")

                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectSegmentBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                    else:
                                                        connect_function = f'connectSegmentBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                            if int(link.get('linkedWay')) != w_num:
                                                if seg_position == "first":
                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectWayFirst(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function
                                                    else:
                                                        connect_function = f' connectWayFirst(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                            if int(link.get('linkedWay')) != w_num:
                                                if seg_position == "last":
                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectWayLast(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function
                                                    else:
                                                        connect_function = f' connectWayLast(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                        div_reservation_object.set('onmouseover', f'{string_onmouseover}')

                reservation_no_list = behavior.findall("./reservation[@trafficLightActive='no']")
                if reservation_no_list[0].get('trafficLightActive') == 'no':

                    div_reservation = ET.SubElement(div_lane_info, 'div',
                                                    attrib={'class': f'bssd_lane_reservation '
                                                                     f'bssd_lane_reservation_{bd}_Tla_No'})

                    if 'type' in reservation_no_list[0].attrib:
                        reservation_type = reservation_no_list[0].get("type").replace('-', '')
                        add_html_class(div_lane,
                                       f'Tla_No_{bd}_reservation_type_{reservation_type}')

                        for reservation_el in reservation_no_list:
                            if reservation_el.get('object') is not None:
                                reservation_obj = reservation_el.get("object").replace(' ', '')
                                reservation_obj_id = f'{div_lane_id}_{bd}_tlaNo_{reservation_obj}'
                                link_string = ""
                                if reservation_el.find('link') is not None:
                                    for link in reservation_el.findall('link'):
                                        linked_way = link.get('linkedWay')
                                        linked_segment = link.get('linkedSegment')
                                        linked_area = link.get('linkedArea')
                                        if int(link.get('linkedWay')) != w_num:
                                            if len(link_string) == 0:
                                                link_string = "linkedWay: " + linked_way + " linkedSegment: " + linked_segment + " linkedArea: " + linked_area
                                            else:
                                                link_string = link_string + " " + "linkedWay: " + linked_way + " linkedSegment: " + linked_segment + " linkedArea: " + linked_area
                                div_reservation_object = ET.SubElement(div_reservation, 'div', attrib={'class': f'reservation_objects '
                                                                                       f'reservation_object_{reservation_obj}', 'onmouseout': 'deleteElement()',
                                                                           'id': f'{reservation_obj_id}', 'data-links': f'{link_string}'})
                                add_html_class(div_reservation, 'gradient')

                                if reservation_el.get("type") != reservation_list[0].get("type"):
                                    different_reservation_type = reservation_el.get("type").replace('-', '')
                                    add_html_class(div_reservation_object,
                                                   f'reservation_object_{different_reservation_type}')

                            # ===== Links =====

                                if reservation_el.find('link') is not None:
                                    if reservation_el.findall('link')[0] is not None:

                                        line_thickness = 20
                                        line_color = "#648FFF"

                                        string_onmouseover = ""
                                        for link in reservation_el.findall('link'):
                                            if int(link.get('linkedWay')) == w_num:
                                                linked_segment = int(link.get('linkedSegment'))
                                                if link.get('linkedArea').lstrip('-').isdigit() and link.get('linkedArea') != '0':
                                                    if linked_segment > s_num:
                                                        lane_number = int(link.get('linkedArea'))

                                                        if lane_number > 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_leftside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")
                                                        if lane_number < 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_rightside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")

                                                        if len(string_onmouseover) == 0:
                                                            connect_function = f'connectNextSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                        else:
                                                            connect_function = f' connectNextSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                    if linked_segment < s_num:
                                                        lane_number = int(link.get('linkedArea'))

                                                        if lane_number > 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_leftside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")

                                                        if lane_number < 0:
                                                            div_lane_id_origin = div_lane_id.replace(f"seg-{s_num}",
                                                                                                     f"seg-{linked_segment}").replace(
                                                                f"_{side_str}side_", f"_rightside_").replace(
                                                                f"lane-{l_num}",
                                                                f"lane-{lane_number}")

                                                        if len(string_onmouseover) == 0:
                                                            connect_function = f'connectLastSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                        else:
                                                            connect_function = f' connectLastSegment(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                            string_onmouseover = string_onmouseover + connect_function

                                                    if linked_segment == s_num:
                                                        lane_number = int(link.get('linkedArea'))
                                                        if lane_number > l_num:
                                                            if lane_number > 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_leftside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")
                                                            if lane_number < 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_rightside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")

                                                            if len(string_onmouseover) == 0:
                                                                connect_function = f'connectLaneTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                            else:
                                                                connect_function = f' connectLaneTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                        if lane_number < l_num:
                                                            if lane_number > 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_leftside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")
                                                            if lane_number < 0:
                                                                div_lane_id_origin = div_lane_id.replace(
                                                                    f"_{side_str}side_", f"_rightside_").replace(
                                                                    f"lane-{l_num}",
                                                                    f"lane-{lane_number}")

                                                            if len(string_onmouseover) == 0:
                                                                connect_function = f'connectLaneBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                            else:
                                                                connect_function = f' connectLaneBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                                string_onmouseover = string_onmouseover + connect_function

                                                if link.get('linkedArea') == 'inf':
                                                    div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_",
                                                                                             f"_leftside_").replace(
                                                        f"_lane-{l_num}", "")

                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectSegmentTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                    else:
                                                        connect_function = f'connectSegmentTop(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                if link.get('linkedArea') == '-inf':

                                                    div_lane_id_origin = div_lane_id.replace(f"_{side_str}side_",
                                                                                             f"_rightside_").replace(
                                                        f"_lane-{l_num}", "")

                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectSegmentBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                                    else:
                                                        connect_function = f'connectSegmentBottom(getId("{reservation_obj_id}"), getId("{div_lane_id_origin}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                            if int(link.get('linkedWay')) != w_num:
                                                if seg_position == "first":
                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectWayFirst(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function
                                                    else:
                                                        connect_function = f' connectWayFirst(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                            if int(link.get('linkedWay')) != w_num:
                                                if seg_position == "last":
                                                    if len(string_onmouseover) > 0:
                                                        connect_function = f' connectWayLast(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function
                                                    else:
                                                        connect_function = f' connectWayLast(getId("{reservation_obj_id}"), getId("{reservation_obj_id}"), "{line_color}", {line_thickness});'
                                                        string_onmouseover = string_onmouseover + connect_function

                                        div_reservation_object.set('onmouseover', f'{string_onmouseover}')

            # ===== SPEED =====

            speed = behavior.find("speed")
            if speed is not None:
                div_speed_wrapper = ET.SubElement(div_lane_info, 'div', attrib={'class': f'bssd_lane_speed '
                                                                                         f'bssd_lane_speed_{bd}'})

                speed_lane_id = f'bssd_speed_max_{bd}_{div_lane_id}'.replace('-', '_')
                speed_container_lane_id = f'speed_container_{bd}_{div_lane_id}'.replace('-', '_')
                if speed.get('max') is not None:
                    ET.SubElement(div_speed_wrapper, 'div', attrib={'class': 'bssd_speed_max ' f'{speed_lane_id}',
                                                                             'data-speed': speed.get('max')}).text = speed.get('max')

                    if speed.get('timeMax') or speed.get('wetMax') is not None:
                        div_speed_container = ET.SubElement(div_speed_wrapper, 'div', attrib={'class': 'speed_container ' f'{speed_container_lane_id}'})

                        if speed.get('timeMax') is not None:
                            ET.SubElement(div_speed_container, 'div', attrib={'class': 'time', 'data-speed': speed.get('timeMax'), 'data-timeInterval': speed.get('timeInterval')})

                        if speed.get('wetMax') is not None:
                            ET.SubElement(div_speed_container, 'div', attrib={'class': 'wetMax', 'data-speed': speed.get('wetMax')})

                        script_speed = ET.Element('script')
                        script_speed.text = f'const {speed_lane_id} =document.querySelector(".{speed_lane_id}"),\n'+f'{speed_container_lane_id} = document.querySelector(".{speed_container_lane_id}");\n\n'+f'{speed_container_lane_id}.addEventListener("mouseover", e => {{\n'+f'if (e.target.matches(".{speed_container_lane_id} > *")) {speed_lane_id}.textContent = e.target.dataset.speed;}})\n\n'+f'{speed_container_lane_id}.addEventListener("mouseout", e => {{\n'+f'if(e.target.matches(".{speed_container_lane_id} > *")) {speed_lane_id}.textContent = {speed_lane_id}.dataset.speed;}})'
                        # script.text = f'const speed_{div_lane_id} = document.querySelector(".bssd_speed_max_{div_lane_id}"),speed_container_{div_lane_id} = document.querySelector(".speed_container_{div_lane_id}"); speed_container_{div_lane_id}.addEventListener("mouseover", e => {{if(e.target.matches(".speed_container_{div_lane_id} > *")) speed_container_{div_lane_id}.textContent = e.target.dataset.speed;}})'
                        div_speed_container.insert(1, script_speed)

    return div_lane_info


def add_html_class(element, new_class):
    classes = element.get('class')
    if classes:
        classes = classes.split()
    else:
        classes = []
    classes.append(new_class.replace(' ', ''))
    element.set('class', ' '.join(classes))


def list_sort(list1, list2):
    list2 = map(int, list2)
    zipped_lists = zip(list2, list1)
    sorted_zipped_lists = sorted(zipped_lists)
    sorted_list = [element for _, element in sorted_zipped_lists]

    return sorted_list


def list_reverse_sort(list1, list2):
    list2 = map(int, list2)
    zipped_lists = zip(list2, list1)
    sorted_zipped_lists = sorted(zipped_lists)
    sorted_list = [element for _, element in sorted_zipped_lists]
    reverse_sorted_list = list(reversed(sorted_list))

    return reverse_sorted_list


if __name__ == '__main__':
    # Setting up arguments and --help
    parser = argparse.ArgumentParser(description="Visualize BSSD.")
    parser.add_argument('-b', '--bssd', type=str,
                        help="Path to BSSD file")
    parser.add_argument('--id', type=str,
                        help="Path to Way-id file")
    args = parser.parse_args()

    # Parse BSSD file
    bssd = ET.parse(args.bssd).getroot()

    # Define way_id
    way_id = int(args.id)

    # Visualize
    viz = visualize(bssd=bssd, way_id=way_id)
    viz_txt = ET.tostring(viz, encoding='UTF-8', method='html', short_empty_elements=False).decode()

    # Generate HTML file
    env = Environment(
        loader=PackageLoader('__init__', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('index.html')
    template.stream(viz=viz_txt).dump('output/output_one_way.html')

    # Open HTML file
    filename = 'file:///' + os.getcwd() + '/output/' + 'output_one_way.html'
    webbrowser.open_new_tab(filename)
