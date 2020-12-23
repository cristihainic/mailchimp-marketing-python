# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.27
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class BatchWebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def remove(self, batch_webhook_id, **kwargs):  # noqa: E501
        """Delete batch webhook  # noqa: E501

        Remove a batch webhook. Webhooks will no longer be sent to the given URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove(batch_webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_webhook_id: The unique id for the batch webhook. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_with_http_info(batch_webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_with_http_info(batch_webhook_id, **kwargs)  # noqa: E501
            return data

    def remove_with_http_info(self, batch_webhook_id, **kwargs):  # noqa: E501
        """Delete batch webhook  # noqa: E501

        Remove a batch webhook. Webhooks will no longer be sent to the given URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_with_http_info(batch_webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_webhook_id: The unique id for the batch webhook. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_webhook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_webhook_id' is set
        if ('batch_webhook_id' not in params or
                params['batch_webhook_id'] is None):
            raise ValueError("Missing the required parameter `batch_webhook_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_webhook_id' in params:
            path_params['batch_webhook_id'] = params['batch_webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/batch-webhooks/{batch_webhook_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get(self, batch_webhook_id, **kwargs):  # noqa: E501
        """Get batch webhook info  # noqa: E501

        Get information about a specific batch webhook.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get(batch_webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_webhook_id: The unique id for the batch webhook. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: BatchWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_with_http_info(batch_webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(batch_webhook_id, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, batch_webhook_id, **kwargs):  # noqa: E501
        """Get batch webhook info  # noqa: E501

        Get information about a specific batch webhook.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_with_http_info(batch_webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_webhook_id: The unique id for the batch webhook. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: BatchWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_webhook_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_webhook_id' is set
        if ('batch_webhook_id' not in params or
                params['batch_webhook_id'] is None):
            raise ValueError("Missing the required parameter `batch_webhook_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_webhook_id' in params:
            path_params['batch_webhook_id'] = params['batch_webhook_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/batch-webhooks/{batch_webhook_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchWebhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List batch webhooks  # noqa: E501

        Get all webhooks that have been configured for batches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :return: BatchWebhooks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List batch webhooks  # noqa: E501

        Get all webhooks that have been configured for batches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :return: BatchWebhooks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'exclude_fields', 'count', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'count' in params and params['count'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling ``, must be a value less than or equal to `1000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/batch-webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchWebhooks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, batch_webhook_id, body, **kwargs):  # noqa: E501
        """Update batch webhook  # noqa: E501

        Update a webhook that will fire whenever any batch request completes processing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(batch_webhook_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_webhook_id: The unique id for the batch webhook. (required)
        :param BatchWebhook2 body:  (required)
        :return: BatchWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_with_http_info(batch_webhook_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(batch_webhook_id, body, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, batch_webhook_id, body, **kwargs):  # noqa: E501
        """Update batch webhook  # noqa: E501

        Update a webhook that will fire whenever any batch request completes processing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(batch_webhook_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_webhook_id: The unique id for the batch webhook. (required)
        :param BatchWebhook2 body:  (required)
        :return: BatchWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_webhook_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_webhook_id' is set
        if ('batch_webhook_id' not in params or
                params['batch_webhook_id'] is None):
            raise ValueError("Missing the required parameter `batch_webhook_id` when calling ``")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_webhook_id' in params:
            path_params['batch_webhook_id'] = params['batch_webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/batch-webhooks/{batch_webhook_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchWebhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, body, **kwargs):  # noqa: E501
        """Add batch webhook  # noqa: E501

        Configure a webhook that will fire whenever any batch request completes processing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchWebhook1 body:  (required)
        :return: BatchWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add batch webhook  # noqa: E501

        Configure a webhook that will fire whenever any batch request completes processing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchWebhook1 body:  (required)
        :return: BatchWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/batch-webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchWebhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
