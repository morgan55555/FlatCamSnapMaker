# ##########################################################
# FlatCAM: 2D Post-processing for Manufacturing            #
# Website:      https://github.com/morgan55555             #
# File Author:  Alex Morgan (c)                            #
# Date:         4-Jun-2023                                 #
# License:      MIT Licence                                #
# ##########################################################

from appPreProcessor import PreProc

IMG_NO_IMAGE = ('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'
'qNvN/E70SHU7IQTbTb7Vqt5ugS4UBiCbe1tbWwsJBVh7Gd5eXl8Zxz/vnnn+eO7ombnoWoFempPHf0Y2PweIDET6LDx48fp367mMTa2trYLkscH+gTeXTimV'
'6/fh2nqVevXnWYmYRnjMH+IH/77bcRj+Y47FK83d+IHU7VQtQwFGGaMZjY2dn59ddfR7mgMqn7xaZTnBjbGyIcdAz2L6JiHqbrMI6595/gVGbtdrtardoPIh'
'x0DPZ3GPPwzHdNe/+AG8/1mNliRSrC4cZgIvqMeThUh7FB7yB96p7M8K0vRFiKMdh/9Aw+D2N4+pL/IV7pK8Khx2Ci2WxGh2fOt263u7S0ZK9+SJwW5nfzkA'
'gLOwaH6nBjYyPXR+vOulhNuDwjwjRjMBGBfaTDg4ODiTxIYrZ4ub0IU47B/g5/+eWXUzuMhai11plin4//qVMiLMgYTLRarejw8PCw/xfr9bpXkRuGIsx9DP'
'Z3GOvSpMMYgK7HDK5SqZR5ySDCUcfgiXl4/OCmtbU1b445uCgw75d3ibDgYzCxt7cX8zBWoWO+UbsAyvytVBFmMwb7O1xYWPC+C8Pa3d2d2hd8iHBmxiCGoQ'
'gnPwYZRbVaHfbOeBEag2Sp2+2W8/JM2SM0Bq1IRWgM8q9Wq1XClz6XOkJj0DAUoTHISbVarWwvgC5vhMbgdOp2u5ubmyI0Bpmkst3PXdIIjcFptre3F18lRW'
'gMMkmlWpGWMUJjcPqV6vJM6SI0BmdCqS7PlC5CY3BWlOcbhuWK0BicIfv7+yW5PFOuCI1Bw1CExiBDqNfrJx6fJUJjkLHq9Xpl+MZ9WSI0BmdURFj4Z4WU5e'
'2y4yz/iy++cEzPordv316+fFmEM0+BWI4CIgQRAiIEEQIiBBECIgQRAiIEEQIiBBGCCAERgggBEYIIgYmY9sdb9Hq9ZrPp88Qout2uCNPrdDo//fSTwwjLUU'
'CEIEJAhCBCQIQgQkCEIEJAhCBCQIQgQkCEIEJAhCBCQIQgQkCEIEJAhCBCQIQgQkCEIEJAhCBCQIQgQkCEIEJAhCBCQIQgQkCEIEJAhCBCQIQgQkCEIEJAhC'
'BCECEgQhAhIEIQISBCECEgQhAhIEIQISBCECEgQhAhIEIQISBCECEgQhAhIEIQIZCx871ez14AEYIIARGCCAERgggBEYIIARGCCAERgggBEYIIARGCCAERgg'
'gBEYIIARGCCAERgggBEYIIARGCCAERgggBEYIIARHC7PqvAAMA/BkrMLAeft8AAAAASUVORK5CYII=')


def units_to_mm(value, units):
    units = str(units).upper()
    if units == "IN":
        value = value * 25.4
    return value


def power_to_percents(value):
    return value / 255 * 100


class Snapmaker_laser(PreProc):
    include_header = True
    coordinate_format = "%.*f"
    feedrate_format = "%.*f"
    feedrate_rapid_format = feedrate_format

    def start_code(self, p):
        gcode = ";Header Start\n"
        gcode += ";header_type: laser\n"
        gcode += ";renderMethod: line\n"
        gcode += ";is_rotate: false\n"

        units = p["units"]

        xmin = units_to_mm(p["options"]["xmin"], units)
        xmax = units_to_mm(p["options"]["xmax"], units)
        ymin = units_to_mm(p["options"]["ymin"], units)
        ymax = units_to_mm(p["options"]["ymax"], units)

        xmin_str = "%.*f" % (p.coords_decimals, xmin)
        xmax_str = "%.*f" % (p.coords_decimals, xmax)
        ymin_str = "%.*f" % (p.coords_decimals, ymin)
        ymax_str = "%.*f" % (p.coords_decimals, ymax)

        gcode += ";max_x(mm): " + "{: >9s}".format(xmax_str) + "\n"
        gcode += ";max_y(mm): " + "{: >9s}".format(ymax_str) + "\n"
        gcode += ";max_z(mm): 0\n"
        gcode += ";max_b(mm): 0\n"
        gcode += ";min_x(mm): " + "{: >9s}".format(xmin_str) + "\n"
        gcode += ";min_y(mm): " + "{: >9s}".format(ymin_str) + "\n"
        gcode += ";min_b(mm): 0\n"
        gcode += ";min_z(mm): 0\n"

        workspeed = units_to_mm(p["feedrate"], units)
        jogspeed = units_to_mm(p["feedrate_rapid"], units)

        gcode += ";work_speed(mm/minute): " + str(workspeed) + "\n"
        gcode += ";jog_speed(mm/minute): " + str(jogspeed) + "\n"

        power = power_to_percents(p["spindlespeed"])

        gcode += ";power(%): " + str(power) + "\n"

        gcode += ";thumbnail: data:image/png;base64," + IMG_NO_IMAGE + "\n"
        gcode += ";Header End\n"

        gcode += "\n"
        gcode += "; Laser single-pass, pass 1 with Z = 0\n"
        gcode += "; G-code for laser engraving\n"
        gcode += "; Generated by FlatCAM Beta\n"
        gcode += "; G-code START <<<\n"

        gcode += "G90\n"
        gcode += ("G20" if p.units.upper() == "IN" else "G21")

        return gcode

    def startz_code(self, p):
        if p.startz is not None:
            return "G0 Z" + self.coordinate_format % (p.coords_decimals, p.z_move)
        else:
            return ""

    def lift_code(self, p):
        gcode = "M400\n"
        gcode += "M5"
        return gcode

    def down_code(self, p):
        if p.spindlespeed:
            power = power_to_percents(p.spindlespeed)
            return "M3 P%s" % (str(power))
        else:
            return "M3"

    def toolchange_code(self, p):
        return ""

    def up_to_zero_code(self, p):
        gcode = "M400\n"
        gcode += "M5"
        return gcode

    def position_code(self, p):
        return ("X" + self.coordinate_format + " Y" + self.coordinate_format) % \
               (p.coords_decimals, p.x, p.coords_decimals, p.y)

    def rapid_code(self, p):
        return ("G0 " + self.position_code(p)).format(**p) + " " + self.feedrate_rapid_code(p)

    def linear_code(self, p):
        return ("G1 " + self.position_code(p)).format(**p) + " " + self.inline_feedrate_code(p)

    def end_code(self, p):
        gcode = "M107 P0\n"
        gcode += "; G-code END <<<\n"

        coords_xy = p["xy_end"]
        gcode += ("G0 Z" + self.feedrate_format % (p.fr_decimals, p.z_end) + " " + self.feedrate_rapid_code(p) + "\n")

        if coords_xy and coords_xy != "":
            gcode += "G0 X{x} Y{y}".format(x=coords_xy[0], y=coords_xy[1]) + " " + self.feedrate_rapid_code(p) + "\n"

        return gcode

    def feedrate_code(self, p):
        return "G1 F" + str(self.feedrate_format % (p.fr_decimals, p.feedrate))

    def z_feedrate_code(self, p):
        return "G1 F" + str(self.feedrate_format % (p.fr_decimals, p.z_feedrate))

    def inline_feedrate_code(self, p):
        return "F" + self.feedrate_format % (p.fr_decimals, p.feedrate)

    def feedrate_rapid_code(self, p):
        return "F" + self.feedrate_rapid_format % (p.fr_decimals, p.feedrate_rapid)

    def spindle_code(self, p):
        gcode = "M106 P0 S255\n"
        if p.spindlespeed:
            power = power_to_percents(p.spindlespeed)
            gcode += "M3 P%s" % (str(power))
        else:
            gcode += "M3"
        return gcode

    def dwell_code(self, p):
        return ""

    def spindle_stop_code(self, p):
        gcode = "M400\n"
        gcode += "M5\n"
        gcode += "M107 P0\n"
        return gcode
