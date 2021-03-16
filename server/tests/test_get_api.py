import json
from django.test import TestCase
from server.views import CreateAudioResource, GetAudioResource

class GetAudioResourceTestCase(TestCase):
    """
    End Point: /server/get/<audioFileType>/<audioFileID>/
    Author      : Kamal Mehta
    Created     : 16-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs :
        16-Mar-2021 - Created
    """
    fixtures_data = {
        "audioFileType": "song",
        "audioFileMetadata": {
            "name": "test_song",
            "duration": 500,
            "title": "test_audiobook",
            "author": "test_author",
            "narrator": "narrator_text",
            "host": "test_host",
            "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        },
    }

    def test_delete_001(self):
        """Success Case delete Audio Resource Info with correct audioFileID"""
        data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=data,
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code, 200):
            request = self.client.get(
               "/server/get/song/1/",
            ).wsgi_request
            response = GetAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_delete_002(self):
        """Success Case delete Audio Resource Info with incorrect audioFileID"""
        data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=data,
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code, 200):
            request = self.client.get(
               "/server/get/song/2/",
            ).wsgi_request
            response = GetAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)
    
    def test_delete_003(self):
        """Success Case delete Audio Resource Info with correct audioFileID"""
        data = self.fixtures_data.copy()
        data['audioFileType'] = "podcast"
        request = self.client.post(
            "/server/create/",
            data=data,
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code, 200):
            request = self.client.get(
               "/server/get/podcast/1/",
            ).wsgi_request
            response = GetAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_delete_004(self):
        """Success Case delete Audio Resource Info with incorrect audioFileID"""
        data = self.fixtures_data.copy()
        data['audioFileType'] = "podcast"
        request = self.client.post(
            "/server/create/",
            data=data,
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code, 200):
            request = self.client.get(
               "/server/get/podcast/2/",
            ).wsgi_request
            response = GetAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)
    
    def test_delete_005(self):
        """Success Case delete Audio Resource Info with correct audioFileID"""
        data = self.fixtures_data.copy()
        data['audioFileType'] = "audiobook"
        request = self.client.post(
            "/server/create/",
            data=data,
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code, 200):
            request = self.client.get(
               "/server/get/audiobook/1/",
            ).wsgi_request
            response = GetAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_delete_006(self):
        """Success Case delete Audio Resource Info with incorrect audioFileID"""
        data = self.fixtures_data.copy()
        data['audioFileType'] = "audiobook"
        request = self.client.post(
            "/server/create/",
            data=data,
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code, 200):
            request = self.client.get(
               "/server/get/audiobook/2/",
            ).wsgi_request
            response = GetAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)