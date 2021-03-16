import json
from django.test import TestCase
from server.views import CreateAudioResource

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

class CreateAudioResourceTestCase(TestCase):
    """
    End Point: /server/create/
    Author      : Kamal Mehta
    Created     : 16-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs :
        16-Mar-2021 - Created
    """
    json_parameters_template = {
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

    def test_create_001(self):
        """Success Case for 'song' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'song'
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_002(self):
        """Success Case for 'podcast' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'podcast'
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_003(self):
        """Success Case for 'audiobook' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'audiobook'
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_004(self):
        """Missing Parameter(s): Case 'audioFileType' for 'song' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'song'
        del(dummy_data['audioFileType'])
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_create_005(self):
        """Missing Parameter(s): Case 'audioFileMetadata' for 'song' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'song'
        del(dummy_data['audioFileMetadata'])
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_create_006(self):
        """Missing Parameter(s): Case 'name' for 'song' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'song'
        del(dummy_data['audioFileMetadata']['name'])
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_007(self):
        """Missing Parameter(s): Case 'name' for 'song' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'song'
        del(dummy_data['audioFileMetadata']['duration'])
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_008(self):
        """Missing Parameter(s): Case 'audioFileType' for 'podcast' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'podcast'
        del(dummy_data['audioFileType'])
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_create_009(self):
        """Missing Parameter(s): Case 'audioFileMetadata' for 'podcast' audio type"""
        dummy_data = self.json_parameters_template.copy()
        dummy_data['audioFileType'] = 'podcast'
        del(dummy_data['audioFileMetadata'])
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_create_010(self):
        """Missing Parameter(s): Case 'name' for 'podcast' audio type"""
        dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "duration": 500,
                "host": "test_host",
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_011(self):
        """Missing Parameter(s): Case 'duration' for 'podcast' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "host": "test_host",
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_012(self):
        """Missing Parameter(s): Case 'duration' for 'podcast' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 500,
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_013(self):
        """Missing Parameter(s): Case 'duration' for 'podcast' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 500,
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_014(self):
        """Failure Case: Participants > 10 for 'podcast' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 500,
                "host": "test_host",
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_015(self):
        """Success Case: Participants < 10 for 'podcast' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 500,
                "host": "test_host",
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_016(self):
        """Success Case: Optional Participants not sent for 'podcast' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 500,
                "host": "test_host",
                "participants": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_017(self):
        """Missing Parameter(s): Case 'duration' for 'audiobook' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "test_audiobook",
                "author": "test_author",
                "narrator": "narrator_text",
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_018(self):
        """Missing Parameter(s): Case 'duration' for 'audiobook' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "duration": 500,
                "author": "test_author",
                "narrator": "narrator_text",
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_019(self):
        """Missing Parameter(s): Case 'duration' for 'audiobook' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "duration": 500,
                "title": "test_audiobook",
                "narrator": "narrator_text",
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_create_020(self):
        """Missing Parameter(s): Case 'duration' for 'audiobook' audio type"""
        dummy_data = dummy_data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "duration": 500,
                "title": "test_audiobook",
                "author": "test_author",
            },
        }
        request = self.client.post(
            path='/server/create/',
            data=json.dumps(dummy_data),
            content_type='application/json'
        ).wsgi_request
        response = CreateAudioResource.as_view()(request)
        self.assertEqual(response.status_code, 400)