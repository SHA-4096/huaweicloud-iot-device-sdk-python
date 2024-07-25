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

from __future__ import absolute_import, annotations
from abc import ABCMeta, abstractmethod

from iot_device_sdk_python.filemanager.url_info import UrlInfo


class FileManagerListener(metaclass=ABCMeta):
    """
    监听文件上传下载事件
    """

    @abstractmethod
    def on_upload_url(self, url_info: UrlInfo):
        """
        接收文件上传url，进行文件上传操作

        Args:
            url_info:   上传参数
        """

    @abstractmethod
    def on_download_url(self, url_info: UrlInfo):
        """
        接收文件下载url,进行文件下载操作

        Args:
            url_info:   下载参数
        """
