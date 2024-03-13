from enum import StrEnum


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
