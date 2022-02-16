# automateDCM2NII

Python script automating the conversion of fMRI images from DICOM to nifti.
The conversion is performed using the dcm2niix converter developed by Chris Rorden's Lab.
The software is available on https://github.com/rordenlab/dcm2niix under a BSD License.

## Usage

automateDCM2NII features a tkinter interface where users can indicate the path to DICOM data, the number of the participant currently being processed and whether the conversion should compress files to nii.gz format.

The script automatically converts DICOM files using dcm2niix, and renames them according to the subject number.

fr 2020-01-22
