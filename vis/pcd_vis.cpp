//
// Created by Jerry Kougianos on 2019-10-15.
//

#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/console/print.h>
#include <pcl/console/parse.h>
#include <pcl-1.9/pcl/visualization/pcl_visualizer.h>


using namespace pcl;
using namespace pcl::io;
using namespace pcl::console;

int main(int argc, char **argv) {

    if (argc != 2) {
        print_error("Requires pcd file as argument");
        return -1;
    }

    std::vector<int> pcd_file_indices = parse_file_extension_argument(argc, argv, ".pcd");
    if (pcd_file_indices.size() != 1) {
        print_error("Need a single output PCD file to continue.\n");
        return (-1);
    }

    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);

    // Load pcd file
    if (loadPCDFile<pcl::PointXYZ>(argv[pcd_file_indices[0]], *cloud) == -1) {
        PCL_ERROR("Couldn't read pcd file");
    }

    // Visualise
    visualization::PCLVisualizer vis_sampled;
    vis_sampled.addPointCloud<pcl::PointXYZ>(cloud);
    vis_sampled.spin();

    return 0;
}