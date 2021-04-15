# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.40
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class CustomerJourneysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def trigger(self, journey_id, step_id, body, **kwargs):  # noqa: E501
        """Customer Journeys API trigger for a contact  # noqa: E501

        A step trigger in a Customer Journey. To use it, create a starting point or step from the Customer Journey builder in the app using the Customer Journeys API condition. We’ll provide a url during the process that includes the {journey_id} and {step_id}. You’ll then be able to use this endpoint to trigger the condition for the posted contact.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trigger(journey_id, step_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int journey_id: The id for the Journey. (required)
        :param int step_id: The id for the Step. (required)
        :param SubscriberInCustomerJourneysAudience body:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trigger_with_http_info(journey_id, step_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_with_http_info(journey_id, step_id, body, **kwargs)  # noqa: E501
            return data

    def trigger_with_http_info(self, journey_id, step_id, body, **kwargs):  # noqa: E501
        """Customer Journeys API trigger for a contact  # noqa: E501

        A step trigger in a Customer Journey. To use it, create a starting point or step from the Customer Journey builder in the app using the Customer Journeys API condition. We’ll provide a url during the process that includes the {journey_id} and {step_id}. You’ll then be able to use this endpoint to trigger the condition for the posted contact.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trigger_with_http_info(journey_id, step_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int journey_id: The id for the Journey. (required)
        :param int step_id: The id for the Step. (required)
        :param SubscriberInCustomerJourneysAudience body:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['journey_id', 'step_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'journey_id' is set
        if ('journey_id' not in params or
                params['journey_id'] is None):
            raise ValueError("Missing the required parameter `journey_id` when calling ``")  # noqa: E501
        # verify the required parameter 'step_id' is set
        if ('step_id' not in params or
                params['step_id'] is None):
            raise ValueError("Missing the required parameter `step_id` when calling ``")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'journey_id' in params:
            path_params['journey_id'] = params['journey_id']  # noqa: E501
        if 'step_id' in params:
            path_params['step_id'] = params['step_id']  # noqa: E501

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
            '/customer-journeys/journeys/{journey_id}/steps/{step_id}/actions/trigger', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
