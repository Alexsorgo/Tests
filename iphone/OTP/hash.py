# -*- coding: utf-8 -*-
import base64, gzip
from StringIO import StringIO


def enc(data):
    # data = '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'
    data_decoded = base64.b64decode(unicode(data).translate(dict(zip(map(ord, u'-_'), u'+/'))))
    sio = StringIO(data_decoded)
    gzf = gzip.GzipFile(fileobj=sio)
    guff = gzf.read()
    try:
        return guff.decode('windows-1251')
    except:
        return guff


def decd(data):
    zip_text_file = StringIO()
    zipper = gzip.GzipFile(mode='wb', fileobj=zip_text_file)
    zipper.write(data.encode('windows-1251'))
    zipper.close()
    enc_text = base64.b64encode(zip_text_file.getvalue())
    return enc_text



