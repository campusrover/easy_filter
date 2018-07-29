# Design Notes

* A reference to an array of floats is passed and not copied


def take_pie_slice(timestamp, length, array, from_index, to_index)
  -> updated array and length

def find_smallest(timestamp, length, array)
  -> updated array and length
  -> index of smallest
  -> value of smallest

def 


Main Loop:
  if (too_soon) continue
  create struct with newscan: length, timestamp, data
  if oldscan == nil, oldscan = newscan

  newscan = take_pie_slice(newscan)
  new_smallest_index, new_smallest_value, newscan = find_smallest(newscan)



class LidarPieSlice:  
  def __init__(oldPieSlice, newData):
    oldslice = old_pie_slice
    newslice = make_slice(newData)
  


Subscriber:

  Init:
    old_pie_Slice = LidarDistance()

  Receive data:
    if elapsed time too short, then just throw it out
    new_pie_slice = LidarPieSlice(old_pie_slice, subscribed_data)
    nd = new_pie_slice.new_distance()
    ns = new_pie_slice.new_approach_speed()
    na = new_pie_slice.new_approach_accel()
    publish: lidar_obstacle_detected(nd, ns, na)



Use numpy!


