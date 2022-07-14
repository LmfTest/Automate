import os
import time
# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#用例文件夹
case_dir = os.path.join(project_path, "API_test_case")

# 报告路径
report_dir = os.path.join(project_path, "report")

# 日志路径
log_dir = os.path.join(project_path, 'log')
##判断日志文件夹不存在就新建一个日志文件夹
def get_logDir(log_dir):
    if os.path.exists(log_dir):
        return log_dir
    else:
        os.mkdir(log_dir)
        return log_dir

log_file = os.path.join(get_logDir(log_dir), '%s.log'%time.strftime('%Y-%m-%d %H-%M-%S'))  # 日志路径
# 配置文件路径

config_dir = os.path.join(project_path,'config')
config_path = os.path.join(config_dir,'config.yaml')