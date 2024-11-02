import sys
import logging
import json
from datetime import datetime
import time
from PyViCare.PyViCare import PyViCare

import myauth

client_id = myauth.client_id
email = myauth.email
password = myauth.password

vicare = PyViCare()
print("init")
vicare.initWithCredentials(email, password, client_id, "token.save")
for device in vicare.devices:
    if device.service.hasRoles(["type:heatpump"]):
        break

#device = vicare.devices[0]

print("Online" if device.isOnline() else "Offline")

t = device.asAutoDetectDevice()
# print(t.getDomesticHotWaterConfiguredTemperature())
# print(t.getDomesticHotWaterStorageTemperature())
# print(t.getOutsideTemperature())
# print(t.getRoomTemperature())
# print(t.getBoilerTemperature())
# print(t.setDomesticHotWaterTemperature(59))

for circuit in t.circuits:
    print(circuit.getName())
    print(circuit.getType())

circuit = t.circuits[0] #select heating circuit

for i in range(2*2*60):

    curTime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    print("supply temperature, " + str(circuit.getSupplyTemperature()) + ", " + str(circuit.getSupplyTemperatureTimeStamp()) + ", " + curTime)
    print("return temperature, " + str(t.getReturnTemperature())  + ", " + str(t.getReturnTemperatureTimeStamp()) + ", " + curTime)
    print("volumetric flow, " + str(t.getVolumetricFlowReturn())  + ", " + str(t.getVolumetricFlowReturnTimeStamp()) + ", " + curTime)
    print("power consumption, " + str(t.getPowerSummaryConsumptionHeatingCurrentDay())  + ", " + str(t.getPowerSummaryConsumptionHeatingCurrentDayTimeStamp()) + ", " + curTime)
    print("outside temperature, " + str(t.getOutsideTemperature())  + ", " + str(t.getOutsideTemperatureTimeStamp()) + ", " + curTime)
    time.sleep(30)

exit(0)
print(circuit.getHeatingCurveShift())
print(circuit.getHeatingCurveSlope())
print(circuit.getActiveProgram())
print(circuit.getPrograms())

print(circuit.getCurrentDesiredTemperature())
print(circuit.getDesiredTemperatureForProgram("comfort"))
print(circuit.getActiveMode())

print(circuit.getDesiredTemperatureForProgram("comfort"))
print(circuit.setProgramTemperature("comfort",21))
print(circuit.activateProgram("comfort"))
print(circuit.deactivateComfort())

# burner = t.burners[0] #select burner
# print(burner.getActive())

compressor = t.compressors[0] #select compressor
print(compressor.getActive())




