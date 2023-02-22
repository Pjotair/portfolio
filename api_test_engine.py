from typing import Any, Tuple, Dict
from apiclients.common import ApiClient


class RequestsAction:

    def change_dict(
            self,
            payload_template: dict,
            search_key: str,
            new_value: Any,
    ) -> dict:
        for key, value in payload_template.items():
            if key == search_key:
                payload_template[key] = new_value
            elif isinstance(value, dict):
                self.change_dict(value, search_key, new_value)
        return payload_template

    def build_payload(
            self,
            payload_template: dict,
            payload_keys: list,
            payload_values: list
    ) -> dict:
        payload_values = [payload_values] if len(payload_values) != 1 else payload_values
        new_data_list = zip(payload_keys, payload_values)
        for k, v in new_data_list:
            self.change_dict(payload_template, k, v)
        return payload_template

    @staticmethod
    def qa_get(
            api_url: str,
            api_client: ApiClient,
            endpoint: str
    ) -> Tuple[int, Dict]:
        request_get = api_client.get(
            url="/".join([api_url, endpoint]),
        )
        return request_get.status_code, request_get.json()

    @staticmethod
    def qa_post(
            api_url: str,
            body_payload: dict,
            api_client: ApiClient,
            endpoint: str,
            **param_dict: dict
    ) -> Tuple[int, Dict]:
        request_post = api_client.post(
            url="/".join([api_url, endpoint]),
            params=param_dict.get('param_dict'),
            json=body_payload
        )
        return request_post.status_code, request_post.json()

    @staticmethod
    def qa_patch(
            api_url: str,
            body_payload: dict,
            api_client: ApiClient,
            endpoint: str,
            **param_dict: dict
    ) -> Tuple[int, Dict]:
        request_patch = api_client.patch(
            url="/".join([api_url, endpoint]),
            params=param_dict.get('param_dict'),
            json=body_payload
        )
        return request_patch.status_code, request_patch.json()

    @staticmethod
    def qa_delete(
            api_url: str,
            api_client: ApiClient,
            endpoint: str
    ) -> Tuple[int, Any]:
        request_delete = api_client.delete(
            url="/".join([api_url, endpoint]),
        )
        if request_delete.status_code != 204:
            return request_delete.status_code, request_delete.json()
        else:
            return request_delete.status_code, None

    def check_dict_data_types(
            self,
            response_template: dict,
            response_body: dict
    ):
        for key, value in response_template.items():
            if key not in response_body.keys():
                return False
            if type(response_body[key]) == dict:
                check_result = self.check_dict_data_types(response_template[key], response_body[key])
                if not check_result:
                    return False
            else:
                if not any(issubclass(type(response_body[key]), data_type) for data_type in value):
                    return False
        return True
