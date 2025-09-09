import math
import json

def triangle_area(a, h):
    return 1/2*a*h

def rectangle_area(a, b):
    return a*b

def circle_area(R):
    return math.pi*R**2

def start():
    result = {}
    triangle_params = list(map(float, input("Enter triangle parameters: ").replace(',','').split()))
    rectangle_params = list(map(float, input("Enter rectangle parameters: ").split()))
    circle_params = list(map(float, input("Enter circle parameters: ").split()))

    result["triangle"] = triangle_area(*triangle_params)
    result["rectangle"] = rectangle_area(*rectangle_params)
    result["circle"] = circle_area(*circle_params)

    return result



if __name__ == "__main__":
    print(json.dumps(start(), indent=4))