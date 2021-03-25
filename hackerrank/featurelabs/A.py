#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'cacheContents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY callLogs as parameter.
#

MIN_PRIORITY = 0
PRIORITY_INCREMENT_VALUE = 2
PRIORITY_DECREMENT_VALUE = 1

TO_CACHE_THRESHOLD = 6
TO_MAIN_MEMORY_THRESHOLD = 3


class ItemStatus:

    def __init__(self):
        self._last_updated: int = None
        self._priority: int = 0
        self._cached: bool = False

    def _update_priority(self, tick: int) -> None:
        '''
        Sets _priority to actual value on the beginning of the tick
        :param tick: number of tick
        :return: None
        '''
        if self._last_updated >= tick:
            return
        time_elapsed_since_last_access = tick - self._last_updated
        self._priority = max(0, self._priority - time_elapsed_since_last_access * PRIORITY_DECREMENT_VALUE)
        self._last_updated = tick

    def access(self, tick: int) -> None:
        '''
        Changes the item status like if it were accessed at time tick.
        :param tick: time when item is accessed. Can not be less than last_updated. (time can not go backwards)
        :return: None
        '''
        if self._last_updated is None:
            self._priority = PRIORITY_INCREMENT_VALUE
        elif tick < self._last_updated:
            raise AttributeError('Tick parameter: {} is less than last update tick: {} for the Item'.format(
                tick, self._last_updated))
        else:
            self._update_priority(tick - 1)
            self._update_if_needs_to_move_to_main_memory()
            self._priority += PRIORITY_INCREMENT_VALUE
            self._update_if_needs_to_move_to_be_cached()
        self._last_updated = tick

    def is_cached(self, tick: int) -> bool:
        '''
        :param tick: time to check wether an Item is cached
        :return: Wether an Item is cached at time tick
        '''
        self._update_priority(tick)
        self._update_if_needs_to_move_to_main_memory()
        return self._cached

    def _update_if_needs_to_move_to_main_memory(self) -> None:
        if self._priority <= TO_MAIN_MEMORY_THRESHOLD:
            self._cached = False

    def _update_if_needs_to_move_to_be_cached(self) -> None:
        if self._priority >= TO_CACHE_THRESHOLD:
            self._cached = True


def cacheContents(callLogs):
    items = defaultdict(ItemStatus)
    callLogs.sort()
    for call in callLogs:
        tick = call[0]
        item_id = call[1]
        items[item_id].access(tick)

    last_tick = callLogs[-1][0]
    cached_item_ids = []
    for item_id in sorted(items.keys()):
        if items[item_id].is_cached(last_tick):
            cached_item_ids.append(item_id)
    if not cached_item_ids:
        return [-1]
    return cached_item_ids


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    callLogs_rows = int(input().strip())
    callLogs_columns = int(input().strip())

    callLogs = []

    for _ in range(callLogs_rows):
        callLogs.append(list(map(int, input().rstrip().split())))

    result = cacheContents(callLogs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
