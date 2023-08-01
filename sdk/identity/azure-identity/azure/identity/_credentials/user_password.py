# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Any, Dict

from .._internal import InteractiveCredential, wrap_exceptions


class UsernamePasswordCredential(InteractiveCredential):
    """Authenticates a user with a username and password.

    In general, Microsoft doesn't recommend this kind of authentication, because it's less secure than other
    authentication flows.

    Authentication with this credential is not interactive, so it is **not compatible with any form of
    multi-factor authentication or consent prompting**. The application must already have consent from the user or
    a directory admin.

    This credential can only authenticate work and school accounts; Microsoft accounts are not supported.
    See `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/fundamentals/sign-up-organization>`_ for more information about
    account types.

    :param str client_id: The application's client ID
    :param str username: The user's username (usually an email address)
    :param str password: The user's password

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str tenant_id: Tenant ID or a domain associated with a tenant. If not provided, defaults to the
        "organizations" tenant, which supports only Azure Active Directory work or school accounts.
    :keyword cache_persistence_options: Configuration for persistent token caching. If unspecified, the credential
        will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword bool disable_instance_discovery: Determines whether or not instance discovery is performed when attempting
        to authenticate. Setting this to true will completely disable both instance discovery and authority validation.
        This functionality is intended for use in scenarios where the metadata endpoint cannot be reached, such as in
        private clouds or Azure Stack. The process of instance discovery entails retrieving authority metadata from
        https://login.microsoft.com/ to validate the authority. By setting this to **True**, the validation of the
        authority is disabled. As a result, it is crucial to ensure that the configured authority host is valid and
        trustworthy.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_username_password_credential]
            :end-before: [END create_username_password_credential]
            :language: python
            :dedent: 4
            :caption: Create a UsernamePasswordCredential.
    """

    def __init__(self, client_id: str, username: str, password: str, **kwargs: Any) -> None:
        # The base class will accept an AuthenticationRecord, allowing this credential to authenticate silently the
        # first time it's asked for a token. However, we want to ensure this first authentication is not silent, to
        # validate the given password. This class therefore doesn't document the authentication_record argument, and we
        # discard it here.
        kwargs.pop("authentication_record", None)
        super(UsernamePasswordCredential, self).__init__(client_id=client_id, **kwargs)
        self._username = username
        self._password = password

    @wrap_exceptions
    def _request_token(self, *scopes: str, **kwargs: Any) -> Dict:
        app = self._get_app(**kwargs)
        return app.acquire_token_by_username_password(
            username=self._username,
            password=self._password,
            scopes=list(scopes),
            claims_challenge=kwargs.get("claims"),
        )
