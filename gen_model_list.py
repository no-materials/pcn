from os import path, listdir

split_type = "train"

ds = "ShapeNetV1"
theDir = "/Volumes/warm_blue/datasets/" + ds

if split_type == "test":
    # TODO: For test list I need 200 models from each zach category (200*6=1200 models)
    out_model_list = "data/shapenet/zach_test_list.txt"

    cats = [name for name in listdir(theDir) if path.isdir(path.join(theDir, name))]

    f = open(out_model_list, "w+")
    for cat in cats:
        cnt = 0
        for model_id in listdir(path.join(theDir, cat)):
            if path.isdir(path.join(theDir, cat, model_id)) and cnt < 200:
                f.write(cat + "/" + model_id + "\n")
                cnt = cnt + 1

    # TODO: fill rest with phones or a big category

    f.close()
elif split_type == "train":
    # For train list I need 28974 models
    out_model_list = "data/shapenet/zach_train_list.txt"

    cats = [name for name in listdir(theDir) if path.isdir(path.join(theDir, name))]

    f = open(out_model_list, "w+")
    for cat in cats:
        for model_id in listdir(path.join(theDir, cat)):
            if path.isdir(path.join(theDir, cat, model_id)):
                f.write(cat + "/" + model_id + "\n")

    f.close()
elif split_type == "valid":
    # TODO: For validatio list I need 800 models
    out_model_list = "data/shapenet/zach_valid_list.txt"

    cats = [name for name in listdir(theDir) if path.isdir(path.join(theDir, name))]

    f = open(out_model_list, "w+")
    for cat in cats:
        for model_id in listdir(path.join(theDir, cat)):
            if path.isdir(path.join(theDir, cat, model_id)):
                f.write(cat + "/" + model_id + "\n")

    f.close()
else:
    pass
