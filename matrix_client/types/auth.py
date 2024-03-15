from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, RootModel


class AuthTypes(StrEnum):
    password = "m.login.password"
    recaptcha = "m.login.recaptcha"
    sso = "m.login.sso"
    email_identity = "m.login.email.identity"
    msisdn = "m.login.msisdn"
    dummy = "m.login.dummy"
    registration_token = "m.login.registration_token"


class IdentifierTypes(StrEnum):
    user = "m.id.user"
    thirdparty = "m.id.thirdparty"
    phone = "m.id.phone"


class UserIdentifier(BaseModel):
    type: Literal["m.id.user"]
    user: str


class ThirdPartyIdentifier(BaseModel):
    type: Literal["m.id.thirdparty"]
    medium: str
    address: str


class PhoneNumberIdentifier(BaseModel):
    type: Literal["m.id.phone"]
    country: str
    phone: str


class PasswordAuth(BaseModel):
    type: Literal["m.login.password"]
    identifier: UserIdentifier | ThirdPartyIdentifier | PhoneNumberIdentifier
    password: str
    session: str


class GoogleReCaptchaAuth(BaseModel):
    type: Literal["m.login.recaptcha"]
    response: str
    session: str


class ThreePIDCreds(BaseModel):
    sid: str
    client_secret: str
    id_server: str
    id_access_token: str


class EmailAuth(BaseModel):
    type: Literal["m.login.email.identity"]
    threepid_creds: ThreePIDCreds
    session: str


class MSISDNAuth(BaseModel):
    type: Literal["m.login.msisdn"]
    threepid_creds: ThreePIDCreds
    session: str


class DummyAuth(BaseModel):
    type: Literal["m.login.dummy"]
    session: str


class TokenAuth(BaseModel):
    type: Literal["m.login.registration_token"]
    token: str
    session: str


class RegistrationTokenValidityResponse(BaseModel):
    valid: bool
