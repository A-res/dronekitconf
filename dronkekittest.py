#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:54:01 2020

@author: ppz
"""

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#-----------
import argparse
parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()

connection_string = args.connect

print("Connection to the vehicle on %s", connection_string)
vehicle = connect(connection_string, wait_ready = True)

#-- Define the function for takeoff 
def arm_and_takeoff(tgt_altitude):
    print("Arming motors")
    
    while not vehicle.is_armable:
        time.sleep(1)
        
        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True 
        
        print("TakeOff")
        vehicle.simple_takeoff(tgt_altitude)
        
#--wait 
        while True :
            altitude =  vehicle.location.global_relative_frame.alt
        
        if altitude >= tgt_altitude -1:
            print("Altitude reached")
            break
        time.sleep(1)
       
#----Main
        
arm_and_takeoff(10)

vehicle.airspeed = 7
print("go to wp1")
wp1 = LocationGlobalRelative(35.9872609, -958753037, 10)

vehicle.simple_goto(wp1)

time.sleep(30)

print("Coming Back")
vehicle.mode = VehicleMode("Rtl")

time.sleep(20)

vehicle.close

