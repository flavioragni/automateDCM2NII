#!python3
#automateDCM2NII.py - Automatically convert all DICOM files in folder to nifti
#and moves them to subject folder
#Usage: automateDCM2NII.py <DICOM to convert path>
from __future__ import print_function
import os, sys, subprocess, shutil
from tkinter import filedialog
from tkinter import *

class userInput(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.show_path = StringVar()
        self.sub_tk = StringVar()
        self.subChoice_tk = StringVar()
        self.comp_tk = StringVar()
        self.lbl0 = Label(text='Select DICOM path:')
        self.lbl0.grid(row=0, column=1)
        self.lbl1 = Label(master=self,textvariable=self.show_path)
        self.lbl1.grid(row=1, column=1)
        self.button2 = Button(text="Browse", command=self.browse_button)
        self.button2.grid(row=1, column=3)
        #Ask for patients or healthy
        self.lb2=Label(self,text='Healthy or patients study? healthy/patients')
        self.lb2.grid(row=3, column=1)
        self.entrySubChoice=Entry(self,textvariable=self.subChoice_tk)
        self.entrySubChoice.grid(row=3, column=2)
        #Ask the user to insert subject number
        self.lb3=Label(self,text='Insert subject number/code:')
        self.lb3.grid(row=4, column=1)
        self.entrySub=Entry(self,textvariable=self.sub_tk)
        self.entrySub.grid(row=4, column=2)
        #Ask for compression of nii files
        self.lb4=Label(self,text='Do you want .gz files? y/n')
        self.lb4.grid(row=5, column=1)
        self.entryComp=Entry(self,textvariable=self.comp_tk)
        self.entryComp.grid(row=5, column=2)
        self.button3 = Button(text="Ok", command=self.ok_button)
        self.button3.grid(row=5, column=3)

    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        #global path
        self.path = filedialog.askdirectory()
        self.show_path.set(self.path)

    def ok_button(self):
        self.sub=self.entrySub.get()
        self.comp=self.entryComp.get()
        self.subChoice=self.entrySubChoice.get()
        self.destroy()

currentUser = userInput()
currentUser.mainloop()

#Set dcm2nii path
conv_path = ".\\dcm2niix.exe"
#conv_path = "D:\\Utilities\\dcm2niix\\dcm2niix.exe"

#List subfolder inside main folder
all_dir = os.listdir(currentUser.path)
#STEP1: conversion of dicom files to nifti
#Select ONLY folders containing actual runs or mprage
#dir = [x for x in all_dir if "mprage" or "Run" or "Localizer" in x]
func_dir = [x for x in all_dir if "Run" in x]
loc_dir = [x for x in all_dir if "Localizer" in x]
struct_dir = [x for x in all_dir if "mprage" in x]
rs_dir = [x for x in all_dir if "RS" in x]

#Convert FUNC RUNS with DICOM2NIIX
for name in func_dir:
    #Define folder with dicom images path
    full_path = os.path.join(currentUser.path, name)

    if currentUser.comp == "y":
        #This applies for functional runs
        comp_choice = " -z y "
        if currentUser.subChoice == "healthy":
            rename_choice = " -f SUB{}_{} "
        elif currentUser.subChoice == "patients":
            rename_choice = " -f {}_{} "
        #command = 'cmd.exe ' + conv_path + comp_choice + rename_choice.format(sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + comp_choice + rename_choice.format(currentUser.sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        print(command)
    else:
        rename_choice = " -f SUB{}_{} "
        #command = 'cmd.exe ' + conv_path + rename_choice.format(sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        command = 'powershell.exe' + conv_path + rename_choice.format(currentUser.sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        print(command)
    #Start the conversion
    os.system(command)

#Convert Localizer runs
for name in loc_dir:
    #Define folder with dicom images path
    full_path = os.path.join(currentUser.path, name)

    if currentUser.comp == "y":
        #This applies for functional runs
        comp_choice = " -z y "
        if currentUser.subChoice == "healthy":
            rename_choice = " -f SUB{}_{} "
        elif currentUser.subChoice == "patients":
            rename_choice = " -f {}_{} "
        #command = 'cmd.exe ' + conv_path + comp_choice + rename_choice.format(sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + comp_choice + rename_choice.format(currentUser.sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        print(command)
    else:
        rename_choice = " -f SUB{}_{} "
        #command = 'cmd.exe ' + conv_path + rename_choice.format(sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + rename_choice.format(currentUser.sub, name.split("_")[1].upper()) + "\'" + full_path + "\'"
        print(command)
    #Start the conversion
    os.system(command)

#Convert structural runs
for name in struct_dir:
    #Define folder with dicom images path
    full_path = os.path.join(currentUser.path, name)

    if currentUser.comp == "y":
        #This applies for functional runs
        comp_choice = " -z y "
        if currentUser.subChoice == "healthy":
            rename_choice = " -f SUB{} -x y "
        elif currentUser.subChoice == "patients":
            rename_choice = " -f {} -x y "
        #command = 'cmd.exe ' + conv_path + comp_choice + rename_choice.format(sub) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + comp_choice + rename_choice.format(currentUser.sub) + "\'" + full_path + "\'"
        print(command)
    else:
        if currentUser.subChoice == "healthy":
            rename_choice = " -f SUB{} -x y "
        elif currentUser.subChoice == "patients":
            rename_choice = " -f {} -x y "
        #command = 'cmd.exe ' + conv_path + rename_choice.format(sub) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + rename_choice.format(currentUser.sub) + "\'" + full_path + "\'"
        print(command)
    #Start the conversion
    os.system(command)

#Convert resting state runs
for name in rs_dir:
    #Define folder with dicom images path
    full_path = os.path.join(currentUser.path, name)

    if currentUser.comp == "y":
        #This applies for functional runs
        comp_choice = " -z y "
        if currentUser.subChoice == "healthy":
            rename_choice = " -f SUB{}_{} "
        elif currentUser.subChoice == "patients":
            rename_choice = " -f {}_{} "
        #command = 'cmd.exe ' + conv_path + comp_choice + rename_choice.format(sub, name.split("_")[1]) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + comp_choice + rename_choice.format(currentUser.sub, name.split("_")[1]) + "\'" + full_path + "\'"
        print(command)
    else:
        if currentUser.subChoice == "healthy":
            rename_choice = " -f SUB{}_{} "
        elif currentUser.subChoice == "patients":
            rename_choice = " -f {}_{} "
        #command = 'cmd.exe ' + conv_path + rename_choice.format(sub, name.split("_")[1]) + "\'" + full_path + "\'"
        command = 'powershell.exe ' + conv_path + rename_choice.format(currentUser.sub, name.split("_")[1]) + "\'" + full_path + "\'"
        print(command)
    #Start the conversion
    os.system(command)

print("Conversion completed!")

#STEP2: move nifti files to different folder
#Check if SUB folder exists otherwise make it
if currentUser.subChoice == "healthy":
    if os.path.exists(f"C:\\Users\\flavio.ragni\\Documents\\Resting_state_project\\SUB{currentUser.sub}"):
        pass
    else:
        os.mkdir(f"C:\\Users\\flavio.ragni\\Documents\\Resting_state_project\\SUB{currentUser.sub}")
    #Search for all nii files in DICOM path
    for root, dirs, files in os.walk(currentUser.path):
        if currentUser.comp == 'y':
            for filename in [f for f in files if f.endswith(('.nii.gz', '.json'))]:
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), f"C:\\Users\\flavio.ragni\\Documents\\Resting_state_project\\SUB{currentUser.sub}")
        else:
            for filename in [f for f in filename if f.endswith(('.nii', '.json'))]:
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), f"C:\\Users\\flavio.ragni\\Documents\\Resting_state_project\\SUB{currentUser.sub}")
elif currentUser.subChoice == "patients":
    if os.path.exists(f"C:\\Users\\flavio.ragni\\Documents\\Patients_leftRight\\{currentUser.sub}"):
        pass
    else:
        os.mkdir(f"C:\\Users\\flavio.ragni\\Documents\\Patients_leftRight\\{currentUser.sub}")
    #Search for all nii files in DICOM path
    for root, dirs, files in os.walk(currentUser.path):
        if currentUser.comp == 'y':
            for filename in [f for f in files if f.endswith(('.nii.gz', '.json'))]:
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), f"C:\\Users\\flavio.ragni\\Documents\\Patients_leftRight\\{currentUser.sub}")
        else:
            for filename in [f for f in filename if f.endswith(('.nii', '.json'))]:
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), f"C:\\Users\\flavio.ragni\\Documents\\Patients_leftRight\\{currentUser.sub}")

print("Job completed: all nii moved to main folder!")
