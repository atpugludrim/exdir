import os
# ffmpeg -i S03E01.mkv -cq 32 -tune hq -c:v h264_nvenc -preset slow S03E01_enc.mkv
# ffmpeg allows encoding using gpu, install nvidia cuda nvcc to support this
files = os.listdir()
for f in files:
    try:
        idx = len(f) - f[::-1].index('.') - 1
    except ValueError:
        of = f + "_enc"
    else:
        container = f[idx:]
        name = f[:idx]
        of = name + "_enc" + container
    runcmd = "ffmpeg -i \"{}\" -cq 35 -tune hq -c:v h264_nvenc -preset slow \"{}\""\
            .format(f, of)
    os.system(runcmd)
