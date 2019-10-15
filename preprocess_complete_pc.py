import os
import concurrent.futures
import subprocess
import logging
import tqdm

# TODO: generalize for datasets/test-training-valid splits/complete-partial
# TODO: fix logging?
executable = "sample/build/mesh_sampling"
src_dataset_dir = "/Volumes/warm_blue/datasets/ShapeNetV2"
model_list_file = "data/shapenet/model_list.txt"
target_data_dir = "data/shapenet/test/complete"
num_threads = 8


def process_mesh(mesh_filepath, target_filepath, exe):
    # logging.info(mesh_filepath + " --> " + target_filepath)
    additional_args = ["-no_vis_result"]  # additional args here ;ike no vis etc...
    command = [exe, mesh_filepath, target_filepath] + additional_args

    print(command)
    subproc = subprocess.Popen(command)
    subproc.wait()


with open(model_list_file) as file:
    model_list = file.read().splitlines()
    file.close()

for i, cat_model_id in tqdm(enumerate(model_list)):

    cat, model_id = cat_model_id.split('/')
    if not os.path.isdir(os.path.join(target_data_dir, cat)):
        os.makedirs(os.path.join(target_data_dir, cat))

    target_mesh_file = os.path.join(target_data_dir, cat, '%s.pcd' % model_id)
    if not os.path.isfile(target_mesh_file):
        mesh_src_file = os.path.join(src_dataset_dir, cat, model_id, 'model.obj')
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(num_threads)) as executor:
            executor.submit(
                process_mesh,
                mesh_src_file,
                target_mesh_file,
                executable
            )

        executor.shutdown()
