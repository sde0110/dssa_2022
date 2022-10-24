# 모듈 import 파트
from datetime import datetime
from collections import defaultdict
import csv 


# Test를 위한 Mock Function 파트
'''

# Class 파트
class ForkliftNode(object):
    pass
     
class LinkedListBag():
    def __init__(self, first_node : Node = None) -> None:
        self._head = first_node  
        self._tail = first_node 
        if first_node is not None:
            self._size = 1
        else:
            self._size = 0
        
    def append(self, new_node : Node) -> None:
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1

    def insert(self, index_number : int, new_node : Node) -> bool:
        list_index = 0
        cur_node = self._head
        if index_number == 0:
            self._head = new_node
            new_node.next = cur_node
            self._size += 1
            return True

        while cur_node is not None:
            if list_index == index_number:
                pred_node.next = new_node
                new_node.next = cur_node
                self._size += 1
                return True
            list_index += 1
            pred_node = cur_node 
            cur_node = cur_node.next
        return False

    def remove(self, target_value : int) -> bool:
        cur_node = self._head
        pred_node = cur_node 
        while cur_node is not None:
            if cur_node.data == target_value:
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            pred_node = cur_node 
            cur_node = cur_node.next
        return False        

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)

class _BagIterator():
    def __init__(self, head_node : Node) -> None:
        self._cur_node = head_node
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node
'''
# 실행 함수 파트

def load_dataset(filename : str):
    #파일 열어서 데이터셋 읽어오기

    f = open(filename,'r')
    l = f.readlines()
    data = []
    dataset = defaultdict(list)
    f.close()
    
    for j in l :
        datas = j[0:-1].split(',')
        data.append(datas)

    for i in range(len(data)) :
        temp = data[i][2]
        data[i][2] = data[i][3]
        data[i][3] = data[i][4]
        data[i][4] = temp

    for i in range(len(data)-1) :
        dataset[data[i+1][1]] += [data[i+1][2:]]
    
    return dataset
    

def sort_dataset(dataset : dict):
    sorted_dataset = sorted(dataset.items(),key = lambda x:x[1][3], reverse= False)
    
    return sorted_dataset


"""
    생성된 dataset을 넣었을 때 각 지게차별로 시간을 기준으로 sorting하여 값을 반환한다.

    Args:
        dataset (dict) : load_dataset 으로 생성된 dataset dict 파일

    Returns:
        sorted_dataset (dict) : 각 지게차별로 시간 순으로 정렬된 dataset dict 파일
    
    Example:
    >>> import teamlab_forklift_ds as ds
    >>> filename = "forklist_move.csv"
    >>> dataset = ds.load_dataset(filename)
    >>> sorted_result = ds.sort_dataset(dataset)
    >>> print(sorted_result)
        {'TEAM10054239': [['172978.787361283',
                           '252229.400114715',
                           '2019-06-01 08:30:48.797'],
                          ['172997.753770613',
                           '252211.490703829',
                           '2019-06-01 08:30:48.832'],
                          ['173021.175135472',
                           '252193.887723743',
                           '2019-06-01 08:30:48.860'],
                          ['173031.106644024',
                           '252176.916908881',
                           '2019-06-01 08:30:48.896'],
                          [### 나머지 출력부분은 생략됨]]
"""
    
'''
def build_linkedlistbag(sorted_dataset : dict):
    """이미 sorting된 dataset을 넣었을 때 각 지게차별로 LinkedListBag을 생성하여 반환한다.

    Args:
        dataset (dict) : load_dataset 으로 생성된 dataset dict 파일
                         만일 입력된 데이터셋이 sorting  되지 않았다면, sorting 하여 준다.                       

    Returns:
        linkedlistbag_dict (dict) : 각 지게차별로 생성된 LinkedListBag을 반환한다.
    
    Example:
    >>> sorted_result = ds.sort_dataset(result)
    >>> result = ds.build_linkedlistbag(sorted_result)
    >>> result.keys()
    dict_keys(['TEAM10054239', 'TEAM1007B9625', 'TEAM10083967'])
    >>> for node in result['TEAM10054239']:
            print(node)
        Forklift name : TEAM10054239
        x coordination : 172978.787361283
        y coordination : 252229.400114715
        Timestamp  : 2019-06-01 08:30:48.797000
        Forklift name : TEAM10054239
        x coordination : 172997.753770613
        y coordination : 252211.490703829
        Timestamp  : 2019-06-01 08:30:48.832000
        -------------------------- 생략 --------------
    """

    linkedlist_bag_dict = {}
    return linkedlist_bag_dict
'''
# def main():
#     DATASET_FILENAME = "forkLift_list"
#     dataset = load_dataset(DATASET_FILENAME)
#     print(dataset)

if __name__ == "__main__":
    dataset = load_dataset('forklist_move.csv')
    print(sort_dataset(dataset))
