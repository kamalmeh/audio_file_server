import json
from django.test import TestCase
from server.views import CreateAudioResource, UpdateAudioResource

#Create API
#Parameters Dictionary
# {
#   "song" : {
#       "001": {
#           "audioFileType": "song",
#           "audioFileMetadata": {
#               "name": "song",
#               "duration": 500
#           },
#       },
#   },
#   "podcast" : {
#       "001": {
#           "audioFileType": "podcast",
#           "audioFileMetadata": {
#               "name": "podcast",
#               "duration": 500,
#               "host": "testHost",
#               "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
#           }
#       },
#   }
#   "audiobook" : {
#       "001": {
#           "audioFileType": "audiobook",
#           "audioFileMetadata": {
#               "title": "audiobook",
#               "duration": 500,
#               "author": "testHost",
#               "narrator": "narrator"
#           }
#       },
#   }
# }

class UpdateAudioResourceTestCase(TestCase):
    """
    End Point: /server/update/<audioFileType>/<audioFileID>/
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

    def test_update_001(self):
        """Success case for "song" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/song/1/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_update_002(self):
        """Failure case(incorrect audio file id) for "song" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/song/2/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)

    def test_update_003(self):
        """Failure case(missing audio file id) for "song" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/song/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)

    def test_update_004(self):
        """Failure case(incorrect audio file type)"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/songs/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)

    def test_update_005(self):
        """Success case for "podcast" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/podcast/1/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_update_006(self):
        """Failure case(incorrect audio file id) for "podcast" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/podcast/2/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)

    def test_update_007(self):
        """Failure case(missing audio file id) for "podcast" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/podcast/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)
    
    def test_update_008(self):
        """Success case for "audiobook" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/audiobook/1/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_update_009(self):
        """Failure case(incorrect audio file id) for "audiobook" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/audiobook/2/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)

    def test_update_010(self):
        """Failure case(missing audio file id) for "audiobook" audio file type"""
        dummy_data = self.fixtures_data.copy()
        request = self.client.post(
            "/server/create/",
            data=json.dumps(dummy_data),
            content_type="application/json"
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        if self.assertEqual(response.status_code,200):
            request = self.client.post(
                "/server/update/audiobook/",
                data=json.dumps(dummy_data),
                content_type="application/json"
            )
            response = UpdateAudioResource.as_view()(request)
            self.assertEqual(response.status_code, 400)