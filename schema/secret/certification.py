# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from pydantic import BaseModel
from common import SchemaConfig, LayerOpt, Reference, ID, Key, BaseSchema, ProfSchema


#===============================================================================
# Implement
#===============================================================================
class Csr(BaseModel):
    countryName:Key = ''
    stateOrProvinceName:Key = ''
    localityName:Key = ''
    organizationName:Key = ''
    organizationalUnitName:Key = ''
    commonName:Key = ''
    emailAddress:Key = ''


@SchemaConfig(minor=1,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Authority(BaseModel, ProfSchema, BaseSchema):
    csr: Csr
    key: Key
    crt: Key


class AuthorityRequest(BaseModel):
    displayName: str
    csr: Csr
    rsaBits: int = 4096
    expiry: int = 10


@SchemaConfig(minor=1,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Server(BaseModel, ProfSchema, BaseSchema):
    csr: Csr
    ca: Reference
    key: Key
    crt: Key


class ServerRequest(BaseModel):
    authorityId: ID
    displayName: str
    distinguishedName: Key
    rsaBits: int = 4096
    expiry: int = 10
