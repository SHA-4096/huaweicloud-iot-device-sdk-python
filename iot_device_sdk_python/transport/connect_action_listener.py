# -*- encoding: utf-8 -*-

# Copyright (c) 2023-2024 Huawei Cloud Computing Technology Co., Ltd. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from typing import Optional
from abc import ABCMeta, abstractmethod


class ConnectActionListener(metaclass=ABCMeta):
    """
    连接动作监听器
    """
    @abstractmethod
    def on_success(self, token: int):
        """
        首次建链成功

        Args:
            token:   返回token
        """

    @abstractmethod
    def on_failure(self, token: int, err: Optional[Exception]):
        """
        首次建链失败

        Args:
            token:   返回token
            err:     失败异常
        """
