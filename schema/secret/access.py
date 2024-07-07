# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from pydantic import BaseModel
from common import SchemaConfig, LayerOpt, Key, BaseSchema, ProfSchema


#===============================================================================
# Implement
#===============================================================================
@SchemaConfig(minor=1,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class OpenSsh(BaseModel, ProfSchema, BaseSchema):
    pri:Key = ''
    pub:Key = ''


class OpenSsshRequest(BaseModel):
    displayName: str
    rsaBits: int = 4096
