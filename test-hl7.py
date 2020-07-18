# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:06:43 2020

@author: Saswati
"""

import hl7
from hl7apy.core import Message
from hl7apy import core

name = 'Saswati Pal'
dt = '2020-July-12 00:25:890'

# hl7 = core.Message("ORM_O01")
hl7 = core.Message("ORU_R01")

hl7.msh.msh_2 = "Converting Data"
hl7.msh.msh_5 = "ORU^O01"
hl7.msh.msh_9 = dt  
hl7.msh.msh_10 = "168715"
hl7.msh.msh_11 = "P"


age = '67'
gender = 'M'

# PID - Patient Identification
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_3 = age
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_5 = gender
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_6 = name

## OBR Segment -- Patient details
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = "10000"


bt = '98.6'
hr = '89'
spo2 = '101'
sbp = '156'
dbp = '73'

#OBX
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_1 = bt
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_2 = hr
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = spo2
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = sbp  
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_6 = dbp  
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "F" # Observ Result Status -- "F" meaning 'Final result'



assert hl7.validate() is True

print ("\n Validate HL7 Message: ", hl7.validate())

print ("\n\n HL7 Message : \n\n", hl7.value)
print ("\n\n")
# Returns True