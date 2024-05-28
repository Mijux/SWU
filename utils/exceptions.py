#!/usr/bin/env python3


class SignatureException(Exception):
    error_code = 403


class GithubException(Exception):
    error_code = 500


class DeployException(Exception):
    error_code = 500


class ConfigurationException(Exception):
    error_code = 500
