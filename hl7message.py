import hl7
from hl7apy.core import Message
from hl7apy import core


a = Message ("ADT_A01")

name = 'Saswati Pal'
dt = '2020-July-12 00:25:890'

hl7 = core.Message("ORM_O01")
hl7.msh.msh_3 = "Converting Data"
hl7.msh.msh_9 = dt  #"ORM^O01^ORM_O01"
hl7.msh.msh_10 = "168715"
hl7.msh.msh_11 = "P"


age = '67'
gender = 'M'

# PID
hl7.add_group("ORM_O01_PATIENT")
hl7.ORM_O01_PATIENT.pid.pid_3 = age
hl7.ORM_O01_PATIENT.pid.pid_5 = gender
hl7.ORM_O01_PATIENT.pid.pid_6 = name #"Saswati Pal"

# ORC
hl7.ORM_O01_ORDER.orc.orc_1 = "1"
hl7.ORM_O01_ORDER.ORC.orc_10 = "20150414120000"

#OBX

assert hl7.validate() is True

print ("\n Validate HL7 Message: ", hl7.validate())

print ("\n\n HL7 Message : \n\n", hl7.value)
print ("\n\n")
# Returns True
