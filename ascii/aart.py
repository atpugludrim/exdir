from PIL import Image, ImageOps
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image","-i",required=True)
    args = parser.parse_args()
    im = Image.open(args.image)
    w, h = im.size
    ratio = 5
    new_w = w // ratio
    new_h = h // (ratio*2)
    im = im.resize((new_w, new_h))
    grim = ImageOps.grayscale(im)
    im_arr = np.array(grim)
    ###############################
    #fillers = "M8S%|:.'   "
    # ^ default

    #fillers = "MOX<:.`'   "
    # ^ for avatar.jpg

    fillers = "MO%<:.`'   "
    # ^ linkedin.jpg
    nbuckets = len(fillers)
    hist = np.histogram(range(256), bins=nbuckets)
    mapping = np.digitize(range(256), bins=hist[1]) - 1
    artim = []
    for r in range(im_arr.shape[0]):
        ro = []
        for c in range(im_arr.shape[1]):
            try:
                ro.append(fillers[mapping[im_arr[r,c]]])
            except IndexError:
                ro.append(fillers[mapping[im_arr[r,c]]-1])
        artim.append(ro)
    artim = np.asarray(artim)
    filename = args.image
    filename = filename[:filename.rindex('.')]
    with open("{}.txt".format(filename),"w") as f:
        for row in artim:
            f.write(''.join(row))
            f.write('\n')
    # import pdb;pdb.set_trace()
    # print()

if __name__=="__main__":
    main()
