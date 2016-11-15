# -*- coding: utf-8 -*-
"""
Animation data utilities.

Utilities for the maya api 2.0

Todo:
    Extend documentation.

.. moduleauthor:: Christian López Barrón <christianlb.vfx@outlook.com>

"""

# standard
import maya.api.OpenMaya as om
# grill
from grill_maya.names import MyAttribute


def find_plug(target_dg_name, mplugs, depth=0, depth_limit=5):
    if depth > depth_limit:
        return
    depth += 1
    for mplug in mplugs:
        mdepnode, dg_name = get_mdependency_node_path(mplug.node())
        if dg_name == target_dg_name:
            return mplug
        affected_plugs = {}
        for p in mdepnode.getAffectedAttributes(mplug.attribute()):
            mp = om.MPlug(mplug.node(), p)
            affected_plugs[mp.partialName(useLongNames=True)] = mp
        if len(affected_plugs)!=1:
            try:
                attribute = MyAttribute(mplug.partialName(useLongNames=True))
            except NameError:  # not a valid or supported attribute
                continue
            plugs = affected_plugs[attribute.get_name(plug='out', index='')].destinations()
        else:
            plugs = mp.destinations()
        return find_plug(target_dg_name, plugs, depth, depth_limit)


def get_mdependency_node_path(mobject):
    mdepnode = om.MFnDagNode(mobject)
    try:
        node_dg_name = mdepnode.getPath().fullPathName()
    except RuntimeError:
        mdepnode = om.MFnDependencyNode(mobject)
        node_dg_name = mdepnode.name()
    return mdepnode, node_dg_name
