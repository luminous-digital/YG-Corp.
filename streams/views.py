from wsgiref.util import FileWrapper

from django.conf import settings
from django.http import Http404, HttpResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404
from wagtail.core import hooks
from wagtail.documents.models import document_served, get_document_model
from wagtail.utils import sendfile_streaming_backend
from wagtail.utils.sendfile import sendfile


def serve(request, document_id, document_filename):
    '''
        This function was pasted from wagtail libary and
        override to open documents in new file
    '''
    Document = get_document_model()
    doc = get_object_or_404(Document, id=document_id)

    # We want to ensure that the document filename provided in the URL matches the one associated with the considered
    # document_id. If not we can't be sure that the document the user wants to access is the one corresponding to the
    # <document_id, document_filename> pair.
    if doc.filename != document_filename:
        raise Http404('This document does not match the given filename.')

    for fn in hooks.get_hooks('before_serve_document'):
        result = fn(doc, request)
        if isinstance(result, HttpResponse):
            return result
    # Send document_served signal
    document_served.send(sender=Document, instance=doc, request=request)

    try:
        local_path = doc.file.path
    except NotImplementedError:
        local_path = None
    if local_path:
        # Use wagtail.utils.sendfile to serve the file;
        # this provides support for mimetypes, if-modified-since and django-sendfile backends

        if hasattr(settings, 'SENDFILE_BACKEND'):
            return sendfile(request, local_path, attachment=True, attachment_filename=doc.filename)
        else:
            # Fallback to streaming backend if user hasn't specified SENDFILE_BACKEND
            return sendfile(
                request,
                local_path,
                attachment=False,
                attachment_filename=doc.filename,
                backend=sendfile_streaming_backend.sendfile
            )

    else:
        # We are using a storage backend which does not expose filesystem paths
        # (e.g. storages.backends.s3boto.S3BotoStorage).
        # Fall back on pre-sendfile behaviour of reading the file content and serving it
        # as a StreamingHttpResponse

        wrapper = FileWrapper(doc.file)
        response = StreamingHttpResponse(wrapper, content_type='application/octet-stream')

        response['Content-Disposition'] = 'attachment; filename=%s' % doc.filename
        response['Content-Length'] = doc.file.size

        return response
