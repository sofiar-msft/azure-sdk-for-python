# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------


from datetime import datetime, timezone
from dateutil.parser import parse


# cSpell:ignore tzinfos
def _convert_str_to_datetime(datetime_as_str: str) -> datetime:
    dt = parse(datetime_as_str, tzinfos=[timezone.utc])
    return dt
