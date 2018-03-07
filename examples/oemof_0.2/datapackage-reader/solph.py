# -*- coding: utf-8 -*-
"""
General description
-------------------
This example shows how to create an oemof energysystem that can be optimized
using solph from a datapackage by using the oemof datapackge reader.

Data
----
Data is provided in the datapackage directory:

data/elements/
   demands.csv',
   volatile-generators.csv
   combined-heat-and-power-plants.csv
   header.csv
   dispatchable-generators.csv
   storages.csv
   transshipment.csv

data/geometries/
   components.csv
   hubs.csv

data/sequences/
   demand-profiles.csv
   solar-profiles.csv
   wind-profiles.csv


Installation requirements
-------------------------
This example requires the latest version of oemof. Install
by:

    pip install 'oemof<0.3,>=0.2'

06.03.2018 - simon.hilpert@uni-flensubrg.de, stephan.guenther@uni-flensburg.de
"""
import os

from matplotlib import pyplot as plt
import networkx as nx
import pandas as pd

from oemof.graph import create_nx_graph as create_graph
from oemof.solph import EnergySystem, Source, Bus, Transformer, Flow, Sink, Model
from oemof.solph.components import GenericStorage, ExtractionTurbineCHP
from oemof.solph.custom import Link
from oemof.tools.datapackage import FLOW_TYPE


es = EnergySystem.from_datapackage(
        'examples/oemof_0.2/datapackage-reader/datapackage/datapackage.json',
        typemap={
            'volatile-generator': Source,
            'hub': Bus,
            'bus': Bus,
            'storage': GenericStorage,
            'dispatchable-generator': Source,
            'transshipment': Link,
            #'extraction-turbine': ExtractionTurbineCHP,
            'backpressure-turbine': Transformer,
            'demand': Sink,
            FLOW_TYPE: Flow})

m = Model(es)