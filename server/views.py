"""
REST API Module for audio resource management
1. CreateAudioResource
2. UpdateAudioResource
3. GetAudioResource
4. DeleteAudioResource
"""
from django.http.response import (
    HttpResponse, HttpResponseBadRequest,
    HttpResponseServerError, JsonResponse
)
from django.views import View
from .utils import ParseRequest
from .models import Song, Podcast, AudioBook

class CreateAudioResource(View):
    """
    End Point   : /server/create/
    Parameters  : Below dictionary
        {
            'audioFileType': 'song|podcast|audiobook',
            'audioFileMetadata' : {
                'name': 'string',
                'duration': integer
            }
        }
    Author      : Kamal Mehta
    Created     : 15-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs : 
        16-Mar-2021 - Added validations
        15-Mar-2021 - Created
    """
    def post(self, request):
        """HTTP Get Method Override"""
        params = ParseRequest(request).parse()
        if 'audioFileType' not in params or 'audioFileMetadata' not in params:
            return HttpResponseBadRequest("The request is invalid")
        if 'duration' not in params['audioFileMetadata']:
                return HttpResponseBadRequest("The request is invalid")
        
        try:
            if params['audioFileType'].lower() == "song":
                if 'name' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                Song.objects.create(
                    name=params['audioFileMetadata']['name'],
                    duration=int(params['audioFileMetadata']['duration'])
                )
            elif params['audioFileType'].lower() == "podcast":
                if 'name' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                if 'host' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                participants = None
                if 'participants' in params['audioFileMetadata']:
                    participants = params['audioFileMetadata']['participants']
                    if len(participants) > 10:
                        return HttpResponseBadRequest("More than 10 particicpants provided")
                Podcast.objects.create(
                    name=params['audioFileMetadata']['name'],
                    duration=int(params['audioFileMetadata']['duration']),
                    host=params['audioFileMetadata']['host'],
                    participants=participants
                )
            elif params['audioFileType'].lower() == "audiobook":
                if 'title' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                if 'narrator' not in params['audioFileMetadata'] or 'author' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                AudioBook.objects.create(
                    title=params['audioFileMetadata']['title'],
                    author=params['audioFileMetadata']['author'],
                    narrator=params['audioFileMetadata']['narrator'],
                    duration=int(params['audioFileMetadata']['duration'])
                )
        except Exception as err:
            print(err)
            return HttpResponseServerError("Internal Server Error")
        
        return HttpResponse("Action is successful")

class UpdateAudioResource(View):
    """
    End Point   : /server/update/<audioFileType>/<audioFileID>/
    Parameters  : Below dictionary
        {
            'audioFileMetadata' : {
                'name': 'string',
                'duration': integer
            }
        }
    Author      : Kamal Mehta
    Created     : 16-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs : 
        16-Mar-2021 - Created
    """
    def post(self, request, audioFileType, audioFileID):
        """HTTP Get Method Override"""
        params = ParseRequest(request).parse()
        if 'audioFileMetadata' not in params:
            return HttpResponseBadRequest("The request is invalid")
        try:
            if audioFileType.lower() == "song":
                if 'name' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                obj = Song.objects.get(id=audioFileID)
                obj.name=params['audioFileMetadata']['name']
                obj.duration=int(params['audioFileMetadata']['duration'])
                obj.save()
            elif audioFileType.lower() == "podcast":
                if 'name' not in params['audioFileMetadata'] or 'host' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                participants = None
                if 'participants' in params['audioFileMetadata']:
                    participants = params['audioFileMetadata']['participants']
                if len(participants) > 10:
                    return HttpResponseBadRequest("More than 10 particicpants provided")
                obj = Podcast.objects.get(id=audioFileID)
                obj.name=params['audioFileMetadata']['name']
                obj.duration=int(params['audioFileMetadata']['duration'])
                obj.host=params['audioFileMetadata']['host']
                obj.participants=participants
                obj.save()
            elif audioFileType.lower() == "audiobook":
                if 'title' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                if 'narrator' not in params['audioFileMetadata'] or 'author' not in params['audioFileMetadata']:
                    return HttpResponseBadRequest("The request is invalid")
                obj = AudioBook.objects.get(id=audioFileID)
                obj.title=params['audioFileMetadata']['title']
                obj.author=params['audioFileMetadata']['author']
                obj.narrator=params['audioFileMetadata']['narrator']
                obj.duration=int(params['audioFileMetadata']['duration'])
                obj.save()
        except Exception as err:
            print(err)
            return HttpResponseServerError("Internal Server Error")
        return HttpResponse("Action is successful")

class GetAudioResource(View):
    """
    End Point   : /server/get/<audioFileType>/<audioFileID>/
    Parameters  : None
    Author      : Kamal Mehta
    Created     : 16-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs :
        16-Mar-2021 - Created
    """
    def get(self, request, audioFileType, audioFileID):
        """HTTP Get Method Override"""
        if audioFileType.lower() == 'song':
            if audioFileID == '':
                return JsonResponse({'data': list(Song.objects.all().values())})
            else:
                return JsonResponse({'data': list(Song.objects.filter(id=audioFileID).values())})
        elif audioFileType.lower() == 'podcast':
            if audioFileID == '':
                return JsonResponse({'data': list(Podcast.objects.all().values())})
            else:
                return JsonResponse({'data': list(Podcast.objects.filter(id=audioFileID).values())})
        elif audioFileType.lower() == 'audiobook':
            if audioFileID == '':
                return JsonResponse({'data': list(AudioBook.objects.all().values())})
            else:
                return JsonResponse({'data': list(AudioBook.objects.filter(id=audioFileID).values())})
        else:
            return HttpResponseBadRequest("The request is invalid")

class DeleteAudioResource(View):
    """
    End Point   : /server/delete/<audioFileType>/<audioFileID>/
    Parameters  : None
    Author      : Kamal Mehta
    Created     : 16-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs :
        16-Mar-2021 - Created
    """
    def get(self, request, audioFileType, audioFileID):
        """HTTP Get Method Override"""
        if audioFileID == '':
                return HttpResponseBadRequest("The request is invalid")
        try:
            if audioFileType.lower() == 'song':
                Song.objects.get(id=audioFileID).delete()
            elif audioFileType.lower() == 'podcast':
                Podcast.objects.get(id=audioFileID).delete()
            elif audioFileType.lower() == 'audiobook':
                AudioBook.objects.get(id=audioFileID).delete()
            else:
                return HttpResponseBadRequest("The request is invalid")
        except Exception as err:
            print(err)
            return HttpResponseServerError("Internal Server Error")    
        return HttpResponse("Action is successful")