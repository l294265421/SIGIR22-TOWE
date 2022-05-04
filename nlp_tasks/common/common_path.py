import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if sys.platform != 'win32' and sys.platform != 'darwin':
    project_dir = '/data/ceph/yuncongli/AGF-ASOTE/'

original_data_dir = os.path.join(project_dir, 'AGF-ASOTE-data')

common_data_dir = project_dir + '/data/'

common_code_dir = project_dir + '/nlp_tasks/'

stopwords_filepath = original_data_dir + 'common/stopwords.txt'


def get_task_data_dir(task_name: str, is_original=False):
    """

    :param task_name: 子任务名
    :return: 保存子任务的数据的目录
    """
    if not is_original:
        return os.path.join(common_data_dir, task_name) + '/'
    else:
        return os.path.join(original_data_dir, task_name) + '/'
