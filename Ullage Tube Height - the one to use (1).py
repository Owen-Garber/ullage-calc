###########################Algorithm 1####################################################################################
#want to find the max ullage space we have available so we can place a vent at the right spot
#know mass of n2o, volume of tank, roughly the temperature
########################################################################################################################
print("################## ALGORITHM 1 ########################")
from CoolProp.CoolProp import PropsSI
import math
Fluid='N2O'
#inputs
tank_volume = 0.008068420320081144 #[m^3] # prev number: 0.0091947816
bulk_radius = 0.05231892 #[m]
bulk_height = 0.04445 #[m]
main_radius = 0.0635 #[m]
main_height = 0.57658 #[m]
print("Tank Volume [m^3]: ", (math.pi * (main_radius**2) * main_height) + 2*(math.pi * (bulk_radius**2) * bulk_height))
ullage = float(input("input ullage [%] "))
temperature = float(input("Input temperature [K] "))
N2O_liquid_volume = (1 - (ullage/100))*tank_volume
#obtain vapor pressure and density
vapor_pressure= PropsSI('P','T',temperature,'Q',0,Fluid) #Q here is the vapor quality, Q=0 since saturated liquid in the tank
print("the vapor pressure at ", temperature, " [k] is", vapor_pressure, "[Pa]")
saturated_liquid_density = PropsSI ('D','P', vapor_pressure ,'Q' ,0 , Fluid ) #this is reasonable according to internet
print("the saturated liquid density is", saturated_liquid_density, "[kg/m^3]")
#obtain and display mass
mass = N2O_liquid_volume*saturated_liquid_density
print("the theoretical max mass of liquid N2O in the internal tank at", temperature, "[k] with ",ullage, "percent ullage is ",mass, "[kg]")

###########################Algorithm 2####################################################################################
#want to find the max ullage space we have available so we can place a vent at the right spot
#know mass of n2o, volume of tank, roughly the temperature
########################################################################################################################
print("##################### ALGORITHM 2 ######################")
#inputs
mass_N2O=5.131354403 #kg in internal tank, found from avg mass flow rate times 7 seconds
#find volume liquid N2O
volume_liquid_N2O= mass_N2O/saturated_liquid_density
print("volume of liquid N2O is ", volume_liquid_N2O, "[m^3]")
calculated_ullage_percent = (1-(volume_liquid_N2O/tank_volume))*100
volume_in_main = ((1-(calculated_ullage_percent/100))*tank_volume) - (3.14*(bulk_radius**2)*bulk_height)
height_from_bottom_main = volume_in_main / (3.14*(main_radius**2))
tube_height = (main_height - height_from_bottom_main) + bulk_height
print("the percent ullage available with ", mass_N2O, " [kg] of liquid N2O in the tank at ", temperature, "[k] is ", calculated_ullage_percent, "%")
print("the tube height from the top is", tube_height, "[m]")

###########################Algorithm 3####################################################################################
#want to find the max ullage space we have available so we can place a vent at the right spot
#know mass of n2o, volume of tank, roughly the temperature
# **we are unsure of this**
########################################################################################################################
print("####################### Algorithm 3 ########################")
total_height = main_height + 2 * bulk_height
print(f"Total height: {total_height} [m]")
# similar to algo 2 but uses volume of N2O not main
#height_from_bottom_to_main_top = volume_liquid_N2O / (math.pi*(main_radius**2)) #height from bottom to top of main
#tube_height2 = main_height - height_from_bottom_to_main_top + bulk_height
# calculating the hegiht N2O based off the volume and knowns
Volume_bulk_head = bulk_height * (bulk_radius**2) * math.pi
print(f"the volume of the bulkhead is {Volume_bulk_head} [m^3]")
height_main_used = (volume_liquid_N2O - Volume_bulk_head)/(math.pi * main_radius**2)
Height_used = height_main_used + bulk_height
tube_height2=total_height-Height_used
print(f"Height of main used: {height_main_used} [m].)")
print(f" The total height used is {Height_used} [m]")
print(f"the tube height from the top is {tube_height2} [m]")

Vol_liq_N20_check = (math.pi * height_main_used * (main_radius**2)) + Volume_bulk_head
print(f"volume of n20: {N2O_liquid_volume}")
print(f"program calculated volume to check vol liq n20 against algorithm 1: {Vol_liq_N20_check} [m]")
if volume_liquid_N2O == Vol_liq_N20_check:
    print("they are equal")
else:
    print("They arent equal. fix it")

if calculated_ullage_percent < ullage:
    raise Exception("Temperature is causing inadequate ullage in the tank compared to requested ullage percent input")

#problems
# 1) need an error message if the ullage percent in the tank goes below the ullage % input