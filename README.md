# FoV-Sphere

A Blender add-on designed for determining the correct Field of View (FoV) and Aspect Ratio when importing a scene ripped with NR 2.

### [Download the Add-on](https://github.com/Julz876/FoV-Sphere/releases)

### Purpose:
To calculate the correct FoV_Y value to use when importing using World Space. The correct Width value should be obtained from the `_log.txt` outputted by Ninja Ripper (NR) and used when importing.

- **Find Width and Height:** 
  - Open the `_log.txt` file and search for "backbuffer." 
  - Use the width and height values found there.

### Requirements:
- Two imports must be made with different FoV values.
- The resulting sphere mesh dimensions of these imports will be used in the calculations.
- **Important:** The same sphere mesh file should be used for all imports. 
- **Note:** Do **NOT** change the Height import value during the process, or the calculated final values will be incorrect.

---

### Quick Use Guide:

#### **FoV_Y Calculator**
1. **Do 1st FoV_Y Import:**
   - In the Importer settings, use the Width and Height values from the log file, or you can supply higher values for better precision.

2. **Enter FoV_Y used:**
   - Input the value from the first FoV_Y import.

3. **Do 2nd FoV_Y Import:**
   - Perform another import using a different FoV_Y value.

4. **Enter FoV_Y used:**
   - Input the value from the second FoV_Y import.

5. **Do FoV_Y Calculation:**
   - Run the calculation, and the result will be displayed in the next step.

6. **Correct FoV_Y:**
   - If everything worked correctly, copy this value and use it for all imports of this scene.

---

### Detailed Step-by-Step Instructions:

1. **Import the Sphere Mesh:**
   - Use the first FoV value and the Width and Height from the log file. 
   - Do not change the Height value once you start.

2. **Enter the 1st FoV Value:**
   - After the first import, enter the FoV value into "1st FoV."

3. **Import the Sphere Mesh Again:**
   - Use the second FoV value and the same Width and Height.

4. **Enter the 2nd FoV Value:**
   - After the second import, enter the FoV value into "2nd FoV."

5. **Calculate and Copy the Final FoV:**
   - Copy the calculated value from "Final FoV."

6. **Delete the Imported Meshes:**
   - Clear the scene to prepare for the final imports.

7. **Import All Mesh Files:**
   - Use the calculated FoV value and the same Width and Height values from the log file.

8. **Done!**
