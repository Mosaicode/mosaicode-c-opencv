#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Select class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Select(BlockModel):
    """
    This class contains methods related the Select class.
    """

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Select"
        self.color = "0:64:191:220"
        self.group = "General"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image1",
                          "label":"First Image",
                          "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image2",
                          "label":"Second Image",
                          "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "label":"Output Image",
                          "conn_type":"Output"}]
        self.properties = [{"name": "key",
                            "label": "Key",
                            "type": MOSAICODE_COMBO,
                            "value": "IMAGE 1",
                            "values": ["IMAGE 1",
                            "IMAGE 2"]
                            }
                           ]
#---------------------------------- C/OpenCv Code --------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image1]$;
    Mat $port[input_image2]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image1]$.empty() && !$port[input_image2]$.empty()){
        if("$prop[key]$" == "IMAGE 1")
            $port[output_image]$ = $port[input_image1]$.clone();
        else
            $port[output_image]$ = $port[input_image2]$.clone();
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image1]$.release();
    $port[input_image2]$.release();
    $port[output_image]$.release();     
"""

# -----------------------------------------------------------------------------
