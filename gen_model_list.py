from os import path, listdir

ds = "ShapeNetV2"
thedir = "/Volumes/warm_blue/datasets/" + ds
out_model_list = "data/shapenet/model_list.txt"

cats = [name for name in listdir(thedir) if path.isdir(path.join(thedir, name))]

f = open(out_model_list, "w+")
for cat in cats:
    for model_id in listdir(path.join(thedir, cat)):
        if path.isdir(path.join(thedir, cat, model_id)):
            f.write(cat + "/" + model_id + "\n")

f.close()
