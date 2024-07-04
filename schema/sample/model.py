# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import List
from pydantic import BaseModel
from common import SchemaConfig, LayerOpt, Reference, ID, Key, BaseSchema, ProfSchema, TagSchema, MetaSchema


#===============================================================================
# Implement
#===============================================================================
class User(BaseModel, ProfSchema): pass


@SchemaConfig( 1 ,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Blog(BaseModel, MetaSchema, TagSchema, BaseSchema):
    title:Key = ''
    text:str = ''
    owner:User
    subscriptions:List[User] = []


@SchemaConfig( 1 ,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Message(BaseModel, BaseSchema):
    text:str = ''
    owner:User
