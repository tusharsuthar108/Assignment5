def maximumUnits(boxTypes, truckSize):
  boxTypes.sort(key=lambda x: -x[1])
  total_units = 0
  remaining_truck_size = truckSize

  for num_boxes, units_per_box in boxTypes:
    boxes_to_take = min(num_boxes, remaining_truck_size)
    total_units += boxes_to_take * units_per_box
    remaining_truck_size -= boxes_to_take

    if remaining_truck_size == 0:
      break
  return total_units

boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
max_units = maximumUnits(boxTypes, truckSize)
print("Maximum units that can be put on the truck:", max_units)
