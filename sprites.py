# sprites.py
import upygame as upg
narwhal_0Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x36\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x36\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x33\x60\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x36\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x06\x66\x66\x66\x33\x60\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x68\x88\x88\x88\x36\x00\x00\x00\x00\
\x06\x06\x00\x00\x00\x06\x88\x88\x88\x88\x60\x00\x00\x00\x00\
\x68\x68\x60\x00\x00\x68\x88\x88\x67\x68\x86\x00\x00\x00\x00\
\x68\x88\x60\x00\x06\x88\x88\x88\x88\x88\x86\x00\x00\x00\x00\
\x06\x86\x00\x00\x68\x88\x88\x88\x88\x88\x86\x00\x00\x00\x00\
\x06\x88\x60\x06\x88\x88\x88\x88\x89\x99\x96\x00\x00\x00\x00\
\x00\x68\x86\x68\x88\x88\x88\x88\x99\x99\x60\x00\x00\x00\x00\
\x00\x06\x88\x88\x89\x99\x88\x99\x99\x96\x00\x00\x00\x00\x00\
\x00\x00\x66\x66\x66\x66\x88\x66\x66\x60\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x66\x06\x60\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x06\x06\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
'
narwhal_1Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x36\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x33\x60\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x33\x66\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x66\x66\x66\x63\x36\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x06\x88\x88\x88\x63\x60\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x68\x88\x88\x88\x86\x60\x00\x00\x00\
\x00\x00\x00\x00\x00\x06\x88\x88\x86\x76\x88\x60\x00\x00\x00\
\x00\x00\x00\x00\x00\x68\x88\x88\x88\x88\x88\x60\x00\x00\x00\
\x06\x60\x00\x00\x06\x88\x88\x88\x88\x88\x88\x60\x00\x00\x00\
\x68\x86\x00\x00\x66\x88\x88\x88\x88\x99\x99\x60\x00\x00\x00\
\x06\x86\x66\x66\x68\x88\x88\x88\x89\x99\x96\x00\x00\x00\x00\
\x68\x88\x88\x88\x88\x99\x98\x89\x99\x99\x60\x00\x00\x00\x00\
\x06\x66\x66\x66\x66\x66\x68\x66\x66\x66\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x66\x60\x66\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
'


narwhal_2Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x66\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x66\x63\x36\
\x00\x00\x00\x00\x00\x00\x00\x66\x66\x66\x66\x66\x33\x36\x60\
\x00\x00\x00\x00\x00\x00\x06\x88\x88\x88\x63\x33\x36\x60\x00\
\x00\x00\x00\x00\x00\x00\x68\x88\x88\x88\x86\x66\x60\x00\x00\
\x00\x00\x00\x00\x00\x06\x88\x88\x86\x76\x88\x60\x00\x00\x00\
\x00\x00\x00\x00\x00\x68\x88\x88\x88\x88\x88\x60\x00\x00\x00\
\x00\x00\x00\x00\x66\x88\x88\x88\x88\x88\x88\x60\x00\x00\x00\
\x00\x00\x00\x66\x88\x88\x88\x88\x88\x99\x99\x60\x00\x00\x00\
\x00\x00\x66\x88\x88\x88\x88\x88\x89\x99\x96\x00\x00\x00\x00\
\x00\x06\x88\x88\x88\x98\x88\x99\x99\x99\x60\x00\x00\x00\x00\
\x00\x68\x86\x66\x66\x68\x89\x66\x66\x66\x00\x00\x00\x00\x00\
\x06\x88\x60\x00\x00\x06\x86\x60\x66\x00\x00\x00\x00\x00\x00\
\x68\x88\x60\x00\x00\x00\x60\x00\x60\x00\x00\x00\x00\x00\x00\
\x68\x68\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
'
narwhal_3Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x66\x66\x66\x66\x66\x66\x66\x66\
\x06\x60\x00\x00\x00\x00\x06\x88\x88\x88\x63\x33\x33\x33\x36\
\x68\x66\x66\x66\x66\x66\x68\x88\x88\x68\x86\x66\x66\x66\x60\
\x06\x88\x88\x88\x88\x86\x88\x88\x86\x76\x88\x60\x00\x00\x00\
\x68\x86\x66\x88\x88\x88\x88\x88\x88\x68\x88\x60\x00\x00\x00\
\x06\x60\x00\x68\x88\x88\x88\x88\x88\x88\x88\x60\x00\x00\x00\
\x00\x00\x00\x06\x88\x88\x88\x88\x88\x99\x99\x60\x00\x00\x00\
\x00\x00\x00\x00\x69\x99\x88\x89\x99\x99\x96\x00\x00\x00\x00\
\x00\x00\x00\x00\x06\x99\x88\x99\x99\x99\x60\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x66\x68\x66\x66\x66\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x03\x00\x66\x60\x66\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\
\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
'


narwhal_sprites = (
    upg.surface.Surface(30, 18, narwhal_0Pixels),
    upg.surface.Surface(30, 18, narwhal_1Pixels),
    upg.surface.Surface(30, 18, narwhal_2Pixels),
    upg.surface.Surface(30, 18, narwhal_3Pixels)
)


coral_0Pixels = b'\
\x00\x60\x00\x06\x60\x00\x06\x60\
\x06\x76\x00\x67\x76\x06\x62\x26\
\x67\x22\x66\x77\x22\x62\x22\x26\
\x06\x72\x22\x22\x22\x22\x22\x60\
\x00\x67\x22\x22\x22\x22\x22\x60\
\x00\x06\x72\x22\x22\x26\x22\x26\
\x00\x67\x72\x22\x22\x62\x22\x60\
\x06\x77\x22\x62\x26\x22\x22\x60\
\x06\x77\x22\x26\x22\x22\x26\x00\
\x06\x72\x22\x22\x62\x22\x22\x60\
\x62\x22\x22\x22\x26\x22\x22\x26\
\x62\x22\x22\x22\x22\x62\x22\x26\
\x06\x22\x22\x22\x26\x22\x22\x60\
\x00\x62\x22\x22\x62\x22\x22\x60\
\x00\x62\x22\x22\x62\x22\x26\x00\
\x00\x06\x22\x26\x22\x22\x26\x00\
\x00\x62\x22\x26\x22\x22\x22\x60\
\x00\x62\x22\x22\x62\x22\x22\x26\
\x00\x62\x22\x22\x26\x22\x22\x26\
\x06\x22\x22\x26\x22\x22\x22\x26\
\x06\x22\x22\x26\x22\x22\x22\x26\
\x67\x22\x22\x62\x22\x22\x22\x60\
\x67\x72\x22\x62\x22\x22\x22\x60\
\x06\x77\x22\x22\x22\x22\x22\x60\
\x06\x77\x22\x22\x22\x22\x22\x60\
\x00\x62\x22\x26\x22\x22\x26\x00\
\x00\x62\x22\x22\x62\x22\x60\x00\
\x06\x22\x22\x22\x62\x22\x26\x00\
\x06\x22\x22\x22\x26\x22\x22\x66\
\x67\x72\x22\x22\x26\x22\x22\x26\
\x67\x22\x22\x22\x22\x22\x22\x60\
\x06\x72\x22\x22\x22\x22\x26\x00\
\x00\x62\x22\x26\x22\x22\x60\x00\
\x00\x62\x22\x26\x22\x22\x60\x00\
\x06\x22\x22\x62\x22\x22\x26\x60\
\x06\x77\x22\x62\x26\x22\x22\x26\
\x00\x62\x22\x22\x22\x66\x22\x26\
\x06\x22\x22\x22\x22\x22\x62\x26\
\x06\x22\x62\x22\x22\x22\x22\x26\
\x67\x26\x22\x22\x22\x26\x22\x60\
\x06\x26\x22\x22\x22\x26\x26\x00\
\x06\x72\x62\x22\x22\x62\x26\x00\
\x06\x72\x26\x22\x22\x62\x22\x60\
\x00\x62\x22\x62\x22\x22\x22\x26\
\x00\x62\x22\x22\x26\x22\x22\x60\
\x00\x62\x22\x22\x62\x22\x22\x60\
\x06\x72\x22\x26\x22\x22\x22\x26\
\x67\x72\x22\x62\x22\x22\x22\x26\
\x67\x72\x26\x22\x22\x22\x22\x26\
\x66\x66\x66\x66\x66\x66\x66\x66\
'

coral_1Pixels = b'\
\x00\x60\x00\x06\x60\x00\x06\x60\
\x06\x76\x00\x67\x76\x06\x6b\xb6\
\x67\xbb\x66\x77\xbb\x6b\xbb\xb6\
\x06\x7b\xbb\xbb\xbb\xbb\xbb\x60\
\x00\x67\xbb\xbb\xbb\xbb\xbb\x60\
\x00\x06\x7b\xbb\xbb\xb6\xbb\xb6\
\x00\x67\x7b\xbb\xbb\x6b\xbb\x60\
\x06\x77\xbb\x6b\xb6\xbb\xbb\x60\
\x06\x77\xbb\xb6\xbb\xbb\xb6\x00\
\x06\x7b\xbb\xbb\x6b\xbb\xbb\x60\
\x6b\xbb\xbb\xbb\xb6\xbb\xbb\xb6\
\x6b\xbb\xbb\xbb\xbb\x6b\xbb\xb6\
\x06\xbb\xbb\xbb\xb6\xbb\xbb\x60\
\x00\x6b\xbb\xbb\x6b\xbb\xbb\x60\
\x00\x6b\xbb\xbb\x6b\xbb\xb6\x00\
\x00\x06\xbb\xb6\xbb\xbb\xb6\x00\
\x00\x6b\xbb\xb6\xbb\xbb\xbb\x60\
\x00\x6b\xbb\xbb\x6b\xbb\xbb\xb6\
\x00\x6b\xbb\xbb\xb6\xbb\xbb\xb6\
\x06\xbb\xbb\xb6\xbb\xbb\xbb\xb6\
\x06\xbb\xbb\xb6\xbb\xbb\xbb\xb6\
\x67\xbb\xbb\x6b\xbb\xbb\xbb\x60\
\x67\x7b\xbb\x6b\xbb\xbb\xbb\x60\
\x06\x77\xbb\xbb\xbb\xbb\xbb\x60\
\x06\x77\xbb\xbb\xbb\xbb\xbb\x60\
\x00\x6b\xbb\xb6\xbb\xbb\xb6\x00\
\x00\x6b\xbb\xbb\x6b\xbb\x60\x00\
\x06\xbb\xbb\xbb\x6b\xbb\xb6\x00\
\x06\xbb\xbb\xbb\xb6\xbb\xbb\x66\
\x67\x7b\xbb\xbb\xb6\xbb\xbb\xb6\
\x67\xbb\xbb\xbb\xbb\xbb\xbb\x60\
\x06\x7b\xbb\xbb\xbb\xbb\xb6\x00\
\x00\x6b\xbb\xb6\xbb\xbb\x60\x00\
\x00\x6b\xbb\xb6\xbb\xbb\x60\x00\
\x06\xbb\xbb\x6b\xbb\xbb\xb6\x60\
\x06\x77\xbb\x6b\xb6\xbb\xbb\xb6\
\x00\x6b\xbb\xbb\xbb\x66\xbb\xb6\
\x06\xbb\xbb\xbb\xbb\xbb\x6b\xb6\
\x06\xbb\x6b\xbb\xbb\xbb\xbb\xb6\
\x67\xb6\xbb\xbb\xbb\xb6\xbb\x60\
\x06\xb6\xbb\xbb\xbb\xb6\xb6\x00\
\x06\x7b\x6b\xbb\xbb\x6b\xb6\x00\
\x06\x7b\xb6\xbb\xbb\x6b\xbb\x60\
\x00\x6b\xbb\x6b\xbb\xbb\xbb\xb6\
\x00\x6b\xbb\xbb\xb6\xbb\xbb\x60\
\x00\x6b\xbb\xbb\x6b\xbb\xbb\x60\
\x06\x7b\xbb\xb6\xbb\xbb\xbb\xb6\
\x67\x7b\xbb\x6b\xbb\xbb\xbb\xb6\
\x67\x7b\xb6\xbb\xbb\xbb\xbb\xb6\
\x66\x66\x66\x66\x66\x66\x66\x66\
'

coral_2Pixels = b'\
\x66\x66\x66\x66\x66\x66\x66\x66\
\x62\x22\x22\x22\x22\x62\x27\x76\
\x62\x22\x22\x22\x26\x22\x27\x76\
\x62\x22\x22\x22\x62\x22\x27\x60\
\x06\x22\x22\x26\x22\x22\x26\x00\
\x06\x22\x22\x62\x22\x22\x26\x00\
\x62\x22\x22\x22\x26\x22\x26\x00\
\x06\x22\x26\x22\x22\x62\x27\x60\
\x00\x62\x26\x22\x22\x26\x27\x60\
\x00\x62\x62\x22\x22\x22\x62\x60\
\x06\x22\x62\x22\x22\x22\x62\x76\
\x62\x22\x22\x22\x22\x26\x22\x60\
\x62\x26\x22\x22\x22\x22\x22\x60\
\x62\x22\x66\x22\x22\x22\x26\x00\
\x62\x22\x22\x62\x26\x22\x77\x60\
\x06\x62\x22\x22\x26\x22\x22\x60\
\x00\x06\x22\x22\x62\x22\x26\x00\
\x00\x06\x22\x22\x62\x22\x26\x00\
\x00\x62\x22\x22\x22\x22\x27\x60\
\x06\x22\x22\x22\x22\x22\x22\x76\
\x62\x22\x22\x62\x22\x22\x27\x76\
\x66\x22\x22\x62\x22\x22\x22\x60\
\x00\x62\x22\x26\x22\x22\x22\x60\
\x00\x06\x22\x26\x22\x22\x26\x00\
\x00\x62\x22\x22\x62\x22\x26\x00\
\x06\x22\x22\x22\x22\x22\x77\x60\
\x06\x22\x22\x22\x22\x22\x77\x60\
\x06\x22\x22\x22\x26\x22\x27\x76\
\x06\x22\x22\x22\x26\x22\x22\x76\
\x62\x22\x22\x22\x62\x22\x22\x60\
\x62\x22\x22\x22\x62\x22\x22\x60\
\x62\x22\x22\x62\x22\x22\x26\x00\
\x62\x22\x22\x26\x22\x22\x26\x00\
\x06\x22\x22\x22\x62\x22\x26\x00\
\x00\x62\x22\x22\x62\x22\x60\x00\
\x00\x62\x22\x26\x22\x22\x26\x00\
\x06\x22\x22\x26\x22\x22\x26\x00\
\x06\x22\x22\x62\x22\x22\x22\x60\
\x62\x22\x26\x22\x22\x22\x22\x26\
\x62\x22\x22\x62\x22\x22\x22\x26\
\x06\x22\x22\x26\x22\x22\x27\x60\
\x00\x62\x22\x22\x62\x22\x77\x60\
\x06\x22\x22\x62\x26\x22\x77\x60\
\x06\x22\x26\x22\x22\x27\x76\x00\
\x62\x22\x62\x22\x22\x27\x60\x00\
\x06\x22\x22\x22\x22\x22\x76\x00\
\x06\x22\x22\x22\x22\x22\x27\x60\
\x62\x22\x26\x22\x77\x66\x22\x76\
\x62\x26\x60\x67\x76\x00\x67\x60\
\x06\x60\x00\x06\x60\x00\x06\x00\
'

coral_3Pixels = b'\
\x66\x66\x66\x66\x66\x66\x66\x66\
\x6b\xbb\xbb\xbb\xbb\x6b\xb7\x76\
\x6b\xbb\xbb\xbb\xb6\xbb\xb7\x76\
\x6b\xbb\xbb\xbb\x6b\xbb\xb7\x60\
\x06\xbb\xbb\xb6\xbb\xbb\xb6\x00\
\x06\xbb\xbb\x6b\xbb\xbb\xb6\x00\
\x6b\xbb\xbb\xbb\xb6\xbb\xb6\x00\
\x06\xbb\xb6\xbb\xbb\x6b\xb7\x60\
\x00\x6b\xb6\xbb\xbb\xb6\xb7\x60\
\x00\x6b\x6b\xbb\xbb\xbb\x6b\x60\
\x06\xbb\x6b\xbb\xbb\xbb\x6b\x76\
\x6b\xbb\xbb\xbb\xbb\xb6\xbb\x60\
\x6b\xb6\xbb\xbb\xbb\xbb\xbb\x60\
\x6b\xbb\x66\xbb\xbb\xbb\xb6\x00\
\x6b\xbb\xbb\x6b\xb6\xbb\x77\x60\
\x06\x6b\xbb\xbb\xb6\xbb\xbb\x60\
\x00\x06\xbb\xbb\x6b\xbb\xb6\x00\
\x00\x06\xbb\xbb\x6b\xbb\xb6\x00\
\x00\x6b\xbb\xbb\xbb\xbb\xb7\x60\
\x06\xbb\xbb\xbb\xbb\xbb\xbb\x76\
\x6b\xbb\xbb\x6b\xbb\xbb\xb7\x76\
\x66\xbb\xbb\x6b\xbb\xbb\xbb\x60\
\x00\x6b\xbb\xb6\xbb\xbb\xbb\x60\
\x00\x06\xbb\xb6\xbb\xbb\xb6\x00\
\x00\x6b\xbb\xbb\x6b\xbb\xb6\x00\
\x06\xbb\xbb\xbb\xbb\xbb\x77\x60\
\x06\xbb\xbb\xbb\xbb\xbb\x77\x60\
\x06\xbb\xbb\xbb\xb6\xbb\xb7\x76\
\x06\xbb\xbb\xbb\xb6\xbb\xbb\x76\
\x6b\xbb\xbb\xbb\x6b\xbb\xbb\x60\
\x6b\xbb\xbb\xbb\x6b\xbb\xbb\x60\
\x6b\xbb\xbb\x6b\xbb\xbb\xb6\x00\
\x6b\xbb\xbb\xb6\xbb\xbb\xb6\x00\
\x06\xbb\xbb\xbb\x6b\xbb\xb6\x00\
\x00\x6b\xbb\xbb\x6b\xbb\x60\x00\
\x00\x6b\xbb\xb6\xbb\xbb\xb6\x00\
\x06\xbb\xbb\xb6\xbb\xbb\xb6\x00\
\x06\xbb\xbb\x6b\xbb\xbb\xbb\x60\
\x6b\xbb\xb6\xbb\xbb\xbb\xbb\xb6\
\x6b\xbb\xbb\x6b\xbb\xbb\xbb\xb6\
\x06\xbb\xbb\xb6\xbb\xbb\xb7\x60\
\x00\x6b\xbb\xbb\x6b\xbb\x77\x60\
\x06\xbb\xbb\x6b\xb6\xbb\x77\x60\
\x06\xbb\xb6\xbb\xbb\xb7\x76\x00\
\x6b\xbb\x6b\xbb\xbb\xb7\x60\x00\
\x06\xbb\xbb\xbb\xbb\xbb\x76\x00\
\x06\xbb\xbb\xbb\xbb\xbb\xb7\x60\
\x6b\xbb\xb6\xbb\x77\x66\xbb\x76\
\x6b\xb6\x60\x67\x76\x00\x67\x60\
\x06\x60\x00\x06\x60\x00\x06\x00\
'

charge_jarPixels = b'\
\x00\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x00\
\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\
\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\
\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\
\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\
\x00\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x66\x00\
'
charge_jar = upg.surface.Surface(102, 6, charge_jarPixels)

jelly_0Pixels = b'\
\x00\x00\x66\x66\x66\x66\x00\x00\
\x06\x66\x5a\xaa\xaa\xaa\x66\x60\
\x65\xaa\xaa\xaa\xaa\xaa\xaa\xa6\
\x65\xaa\xaa\xaa\xaa\xaa\xaa\xa6\
\x65\xaa\xaa\xaa\xaa\xaa\xaa\xa6\
\x6a\xaa\xaa\xaa\xaa\xaa\xaa\xa6\
\x6a\xaa\xaa\xaa\xaa\xaa\xaa\xa6\
\x6a\xaa\xaa\xaa\xaa\xaa\xaa\xa6\
\x06\x66\x5a\xaa\xaa\xaa\x66\x60\
\x00\x00\x66\x66\x66\x66\xa6\x00\
\x00\x06\xa6\xaa\x6a\xa6\xaa\x60\
\x00\x06\xa6\xaa\x6a\xa6\xa6\x60\
\x00\x6a\xa6\xaa\x6a\xa6\xa6\x00\
\x00\x6a\x6a\xaa\x6a\xa6\xa6\x00\
\x00\x6a\x65\xaa\x6a\xa6\xa6\x00\
\x00\x6a\x66\xaa\x6a\xa6\x66\x00\
\x00\x6a\xa6\xaa\x66\xaa\x66\x00\
\x00\x06\xa6\xaa\xa6\xaa\xa6\x00\
\x00\x06\xa6\x5a\xaa\x6a\xa6\x00\
\x00\x06\xaa\x6a\xaa\x6a\xa6\x00\
\x00\x00\x6a\x6a\xaa\x66\xa6\x00\
\x00\x00\x6a\x6a\xaa\xa6\xa6\x00\
\x00\x06\xaa\x6a\xaa\x6a\xa6\x60\
\x00\x06\xaa\x6a\xaa\x6a\xaa\x60\
\x00\x6a\xa6\x5a\x6a\x6a\xaa\x60\
\x00\x6a\xa6\xaa\x6a\x6a\xaa\x60\
\x00\x6a\x6a\xaa\x6a\x6a\xaa\x60\
\x00\x6a\x6a\xaa\x6a\x6a\xaa\x60\
\x00\x6a\xa6\xaa\x6a\x6a\xaa\x60\
\x00\x06\xa6\xaa\x6a\x6a\xaa\x60\
\x00\x06\xaa\x6a\x6a\x66\xaa\x60\
\x00\x00\x6a\x6a\x66\xa6\xaa\x60\
\x00\x00\x6a\xa6\x56\xa6\xa6\x00\
\x00\x00\x06\xa6\x56\xa6\xa6\x00\
\x00\x00\x06\xa6\xa6\xa6\xa6\x00\
\x00\x00\x6a\x6a\xaa\x66\xa6\x00\
\x00\x00\x6a\x6a\xaa\x6a\xa6\x00\
\x00\x06\xaa\x6a\xa6\x6a\xa6\x00\
\x00\x06\xaa\x6a\xa6\xaa\xa6\x00\
\x00\x06\xa6\xaa\xa6\xaa\xaa\x60\
\x00\x06\xa6\xaa\xa6\xaa\xaa\x60\
\x00\x6a\x65\xaa\xaa\x6a\xaa\x60\
\x00\x6a\x65\xaa\xaa\x66\xaa\x60\
\x00\x06\xa6\xaa\xaa\xa6\xaa\x60\
\x00\x06\xa6\x6a\xaa\xaa\x6a\x60\
\x00\x00\x6a\x65\xa6\xaa\x65\x60\
\x00\x00\x6a\x6a\xa6\xaa\xa6\x00\
\x00\x00\x6a\x6a\xa6\xaa\x60\x00\
\x00\x00\x6a\x6a\xa6\xa6\x00\x00\
\x00\x00\x06\x66\x66\x60\x00\x00\
'

jelly_1Pixels = b'\
\x00\x00\x66\x66\x66\x66\x00\x00\
\x06\x66\x55\x55\x55\x55\x66\x60\
\x65\x55\x55\x55\x55\x55\x55\x56\
\x65\x55\x55\x55\x55\x55\x55\x56\
\x65\x55\x55\x55\x55\x55\x55\x56\
\x65\x55\x55\x55\x55\x55\x55\x56\
\x65\x55\x55\x55\x55\x55\x55\x56\
\x65\x55\x55\x55\x55\x55\x55\x56\
\x06\x66\x55\x55\x55\x55\x66\x60\
\x00\x00\x66\x66\x66\x66\x56\x00\
\x00\x06\x56\x55\x65\x56\x55\x60\
\x00\x06\x56\x55\x65\x56\x56\x60\
\x00\x65\x56\x55\x65\x56\x56\x00\
\x00\x65\x65\x55\x65\x56\x56\x00\
\x00\x65\x65\x55\x65\x56\x56\x00\
\x00\x65\x66\x55\x65\x56\x66\x00\
\x00\x65\x56\x55\x66\x55\x66\x00\
\x00\x06\x56\x55\x56\x55\x56\x00\
\x00\x06\x56\x55\x55\x65\x56\x00\
\x00\x06\x55\x65\x55\x65\x56\x00\
\x00\x00\x65\x65\x55\x66\x56\x00\
\x00\x00\x65\x65\x55\x56\x56\x00\
\x00\x06\x55\x65\x55\x65\x56\x60\
\x00\x06\x55\x65\x55\x65\x55\x60\
\x00\x65\x56\x55\x65\x65\x55\x60\
\x00\x65\x56\x55\x65\x65\x55\x60\
\x00\x65\x65\x55\x65\x65\x55\x60\
\x00\x65\x65\x55\x65\x65\x55\x60\
\x00\x65\x56\x55\x65\x65\x55\x60\
\x00\x06\x56\x55\x65\x65\x55\x60\
\x00\x06\x55\x65\x65\x66\x55\x60\
\x00\x00\x65\x65\x66\x56\x55\x60\
\x00\x00\x65\x56\x56\x56\x56\x00\
\x00\x00\x06\x56\x56\x56\x56\x00\
\x00\x00\x06\x56\x56\x56\x56\x00\
\x00\x00\x65\x65\x55\x66\x56\x00\
\x00\x00\x65\x65\x55\x65\x56\x00\
\x00\x06\x55\x65\x56\x65\x56\x00\
\x00\x06\x55\x65\x56\x55\x56\x00\
\x00\x06\x56\x55\x56\x55\x55\x60\
\x00\x06\x56\x55\x56\x55\x55\x60\
\x00\x65\x65\x55\x55\x65\x55\x60\
\x00\x65\x65\x55\x55\x66\x55\x60\
\x00\x06\x56\x55\x55\x56\x55\x60\
\x00\x06\x56\x65\x55\x55\x65\x60\
\x00\x00\x65\x65\x56\x55\x65\x60\
\x00\x00\x65\x65\x56\x55\x56\x00\
\x00\x00\x65\x65\x56\x55\x60\x00\
\x00\x00\x65\x65\x56\x56\x00\x00\
\x00\x00\x06\x66\x66\x60\x00\x00\
'

jelly_2Pixels = b'\
\x00\x00\x66\x66\x66\x66\x00\x00\
\x06\x66\x52\x22\x22\x22\x66\x60\
\x65\x22\x22\x22\x22\x22\x22\x26\
\x65\x22\x22\x22\x22\x22\x22\x26\
\x65\x22\x22\x22\x22\x22\x22\x26\
\x62\x22\x22\x22\x22\x22\x22\x26\
\x62\x22\x22\x22\x22\x22\x22\x26\
\x62\x22\x22\x22\x22\x22\x22\x26\
\x06\x66\x52\x22\x22\x22\x66\x60\
\x00\x00\x66\x66\x66\x66\x26\x00\
\x00\x06\x26\x22\x62\x26\x22\x60\
\x00\x06\x26\x22\x62\x26\x26\x60\
\x00\x62\x26\x22\x62\x26\x26\x00\
\x00\x62\x62\x22\x62\x26\x26\x00\
\x00\x62\x65\x22\x62\x26\x26\x00\
\x00\x62\x66\x22\x62\x26\x66\x00\
\x00\x62\x26\x22\x66\x22\x66\x00\
\x00\x06\x26\x22\x26\x22\x26\x00\
\x00\x06\x26\x52\x22\x62\x26\x00\
\x00\x06\x22\x62\x22\x62\x26\x00\
\x00\x00\x62\x62\x22\x66\x26\x00\
\x00\x00\x62\x62\x22\x26\x26\x00\
\x00\x06\x22\x62\x22\x62\x26\x60\
\x00\x06\x22\x62\x22\x62\x22\x60\
\x00\x62\x26\x52\x62\x62\x22\x60\
\x00\x62\x26\x22\x62\x62\x22\x60\
\x00\x62\x62\x22\x62\x62\x22\x60\
\x00\x62\x62\x22\x62\x62\x22\x60\
\x00\x62\x26\x22\x62\x62\x22\x60\
\x00\x06\x26\x22\x62\x62\x22\x60\
\x00\x06\x22\x62\x62\x66\x22\x60\
\x00\x00\x62\x62\x66\x26\x22\x60\
\x00\x00\x62\x26\x56\x26\x26\x00\
\x00\x00\x06\x26\x56\x26\x26\x00\
\x00\x00\x06\x26\x26\x26\x26\x00\
\x00\x00\x62\x62\x22\x66\x26\x00\
\x00\x00\x62\x62\x22\x62\x26\x00\
\x00\x06\x22\x62\x26\x62\x26\x00\
\x00\x06\x22\x62\x26\x22\x26\x00\
\x00\x06\x26\x22\x26\x22\x22\x60\
\x00\x06\x26\x22\x26\x22\x22\x60\
\x00\x62\x65\x22\x22\x62\x22\x60\
\x00\x62\x65\x22\x22\x66\x22\x60\
\x00\x06\x26\x22\x22\x26\x22\x60\
\x00\x06\x26\x62\x22\x22\x62\x60\
\x00\x00\x62\x65\x26\x22\x65\x60\
\x00\x00\x62\x62\x26\x22\x26\x00\
\x00\x00\x62\x62\x26\x22\x60\x00\
\x00\x00\x62\x62\x26\x26\x00\x00\
\x00\x00\x06\x66\x66\x60\x00\x00\
'

sharkPixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x06\x60\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x68\x60\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x68\x86\x00\x00\x00\x00\x00\x06\
\x00\x00\x00\x00\x00\x00\x00\x68\x86\x00\x00\x00\x00\x00\x66\
\x00\x00\x00\x00\x00\x06\x66\x88\x86\x00\x00\x00\x00\x06\x86\
\x00\x00\x00\x00\x66\x68\x88\x88\x86\x66\x00\x00\x00\x06\x86\
\x00\x00\x06\x66\x88\x88\x88\x88\x88\x88\x66\x00\x00\x68\x86\
\x00\x66\x68\x88\x88\x88\x88\x88\x88\x88\x88\x66\x66\x88\x60\
\x66\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x60\
\x68\x88\x63\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x60\
\x06\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x86\x68\x88\x60\
\x00\x63\x33\x33\x33\x33\x36\x88\x88\x63\x36\x60\x06\x88\x86\
\x00\x06\x66\x66\x33\x33\x33\x68\x88\x66\x60\x00\x00\x63\x36\
\x00\x00\x00\x00\x66\x66\x66\x66\x86\x00\x00\x00\x00\x06\x36\
\x00\x00\x00\x00\x00\x00\x00\x06\x66\x00\x00\x00\x00\x00\x66\
'



enemies_sprites = (
    upg.surface.Surface(16, 50, coral_0Pixels),
    upg.surface.Surface(16, 50, coral_1Pixels),
    upg.surface.Surface(16, 50, coral_2Pixels),
    upg.surface.Surface(16, 50, coral_3Pixels),
    
    upg.surface.Surface(16, 50, jelly_0Pixels),
    upg.surface.Surface(16, 50, jelly_1Pixels),
    upg.surface.Surface(16, 50, jelly_2Pixels),
    
    upg.surface.Surface(30, 16, sharkPixels)
)
