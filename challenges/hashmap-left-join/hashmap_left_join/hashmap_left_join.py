from hashmap_left_join.hashtable import Hashtable
# from hashtable import Hashtable

def left_join(left_hash,right_hash):
    new = Hashtable(20)
    array = []
    for key in left_hash.keys:
        if right_hash.contains(key):
            new.add(key,[left_hash.get(key),right_hash.get(key)])
        else:
            new.add(key,[left_hash.get(key),'NULL'])
    for key in new.keys:
        subarray = [key, new.get(key)[0],new.get(key)[1]]
        array.append(subarray)
    return array


# def left_join(left_hash,right_hash):
#     array = []
#     for key in left_hash.keys:
#         subarray = [key, left_hash.get(key)]
#         if key in right_hash.keys:
#             subarray.append(right_hash.get(key))
#         else:
#             subarray.append('NULL')
#         array.append(subarray)
#     return array