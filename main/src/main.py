##i test i test wqeqweas
from trclab.utils.RGBColor import RGBColor

if __name__ == '__main__':
    color = RGBColor(30, 60, 158)
    print(color.red())
    print(color.green())
    print(color.blue())
    print(color.serialize())
    color2 = RGBColor(serialize_data=color.serialize())
    print(color2.red())
    print(color2.green())
    print(color2.blue())
    print(color2.serialize())
