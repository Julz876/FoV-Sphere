#
#  FOV Sphere by Lofty
#  Modified and updated by KingxJulz
#  (This is designed for use with a SPHERE object.)
# 
#      This add-on is used to calculate the correct Reprojection (Full)
#      FOV_Y import method parameters by comparing the data from two imports,
#      a Base and a Test. Follow the numbered steps to reach the final values.
#

import bpy
from bpy.props import (FloatProperty, BoolProperty)
from bpy.types import (PropertyGroup, Panel, Operator)
import math

bl_info = {
    "name": "FoV Sphere",
    "blender": (3, 0, 0),
    "category": "Object",
    "author": "Lofty, KingxJulz",
    "version": (1, 5),
    "description": "Calculates FoV based on user-provided values for two imports",
}

v_precise = 6

class FOVProperties(bpy.types.PropertyGroup):

    base_fov_float: FloatProperty(name="1st FoV_Y", precision=v_precise, default=45.0)
    test_fov_float: FloatProperty(name="2nd FoV_Y", precision=v_precise, default=20.0)
    final_fov_float: FloatProperty(name="Final FoV_Y", precision=v_precise, default=0.0)
    base_y_float: FloatProperty(name="Base Y", default=0.00, precision=v_precise)
    base_z_float: FloatProperty(name="Base Z", default=0.00, precision=v_precise)
    test_y_float: FloatProperty(name="Test Y", default=0.0, precision=v_precise)
    calc_fov_bool: BoolProperty(name="FoV Calculated", default=False)

    def calculate_fov(self, context):
        # Retrieve the two selected objects
        objs = context.selected_objects
        if len(objs) != 2:
            return None, "Please select exactly the two imported spheres."

        obj_base, obj_test = objs

        # Ensure objects are valid meshes
        if obj_base.type != 'MESH' or obj_test.type != 'MESH':
            return None, "Selected objects must be meshes."

        # Record dimensions of the base and test objects
        self.base_y_float = obj_base.dimensions[1]
        self.base_z_float = obj_base.dimensions[2]
        self.test_y_float = obj_test.dimensions[1]

        # Calculate the final FoV based on the provided FoV values
        zdepth = ((self.base_y_float / 2) / math.tan(math.radians(self.base_fov_float / 2)) +
                  (self.test_y_float / 2) / math.tan(math.radians(self.test_fov_float / 2))) / 2
        fov_final = math.degrees(2 * math.atan((self.base_z_float / 2) / zdepth))

        return fov_final, None


class FOV_PT_Panel(bpy.types.Panel):
    bl_label = "FoV Calculator"
    bl_idname = "FOV_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "FoV Sphere"

    def draw(self, context):
        layout = self.layout
        fovtool = context.scene.my_tool

        layout.label(text="Imported Sphere")
        layout.prop(fovtool, "base_fov_float", text="1st FoV_Y")
        layout.prop(fovtool, "test_fov_float", text="2nd FoV_Y")
        layout.operator("fovcalc.calculate_fov", text="Calculate")

        if fovtool.calc_fov_bool:
            layout.prop(fovtool, "final_fov_float", text="Final FoV_Y")
        else:
            layout.label(text="FoV Calculation not complete", icon='ERROR')


class FOV_OT_CalculateFoV(Operator):
    bl_label = "Calculate FoV_Y"
    bl_idname = "fovcalc.calculate_fov"

    def execute(self, context):
        fovtool = context.scene.my_tool
        fov_final, error = fovtool.calculate_fov(context)
        
        if error:
            self.report({'ERROR'}, error)
            return {'CANCELLED'}

        fovtool.final_fov_float = fov_final
        fovtool.calc_fov_bool = True
        return {'FINISHED'}


classes = [
    FOVProperties,
    FOV_PT_Panel,
    FOV_OT_CalculateFoV,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=FOVProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
