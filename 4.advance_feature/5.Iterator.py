#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))

#force change iterable tpye to iterator type
print(isinstance(iter([]),Iterator))

